#!/usr/bin/env python3
"""Score public travel-booking verification findings."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any


AXES = (
    "review_reliability",
    "price_fairness",
    "location_routing",
    "operator_reliability",
    "traps_risks",
    "context",
)

CRITICAL_TERMS = (
    "no-show",
    "refund refusal",
    "scam",
    "fake",
    "bait",
    "forced shopping",
    "closed",
    "cancelled",
)


def clamp(value: float, low: int = 0, high: int = 100) -> int:
    return max(low, min(high, round(value)))


def as_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value]
    return []


def axis_score(axis: dict[str, Any]) -> tuple[int, list[str]]:
    """Deterministic heuristic: evidence helps, risks hurt, uncertainty hurts."""
    if isinstance(axis.get("score"), (int, float)):
        base = float(axis["score"])
    else:
        base = 50 + 8 * len(as_list(axis.get("positive"))) - 12 * len(as_list(axis.get("negative")))

    confidence = axis.get("confidence", 0.0)
    if not isinstance(confidence, (int, float)):
        confidence = 0.0
    confidence = max(0.0, min(1.0, float(confidence)))

    score = clamp(base - (1.0 - confidence) * 20)
    flags: list[str] = []

    if confidence < 0.4:
        flags.append("low_confidence")
    if not as_list(axis.get("sources")):
        flags.append("missing_sources")

    negatives = " ".join(as_list(axis.get("negative"))).lower()
    for term in CRITICAL_TERMS:
        if term in negatives:
            flags.append(f"critical:{term}")

    return score, flags


def decide(overall: int, flags: list[str]) -> str:
    critical_count = sum(":critical:" in flag for flag in flags)
    uncertainty_count = sum(flag.endswith(":low_confidence") or flag.endswith(":missing_sources") for flag in flags)

    # Hard risk beats average score; weak evidence blocks "book now".
    if critical_count >= 2 or overall < 55:
        return "비추천"
    if critical_count or uncertainty_count >= 2 or overall < 75:
        return "확인 후 예약"
    return "지금 예약 OK"


def score(payload: dict[str, Any]) -> dict[str, Any]:
    findings = payload.get("findings", {})
    axis_scores: dict[str, int] = {}
    flags: list[str] = []

    for name in AXES:
        raw_axis = findings.get(name, {})
        axis = raw_axis if isinstance(raw_axis, dict) else {}
        axis_scores[name], axis_flags = axis_score(axis)
        flags.extend(f"{name}:{flag}" for flag in axis_flags)

    overall = clamp(sum(axis_scores.values()) / len(AXES))
    return {
        "candidate": payload.get("candidate"),
        "city": payload.get("city"),
        "axis_scores": axis_scores,
        "overall_score": overall,
        "risk_flags": flags,
        "verdict": decide(overall, flags),
    }


def load_payload(path: str | None) -> dict[str, Any]:
    raw = open(path, encoding="utf-8").read() if path else sys.stdin.read()
    payload = json.loads(raw)
    if not isinstance(payload, dict):
        raise SystemExit("Input JSON must be an object.")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Score travel booking verification findings.")
    parser.add_argument("json_file", nargs="?", help="Findings JSON file. Reads stdin when omitted.")
    args = parser.parse_args()
    print(json.dumps(score(load_payload(args.json_file)), ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
