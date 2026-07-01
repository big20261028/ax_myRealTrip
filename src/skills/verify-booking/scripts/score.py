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

VERDICT_OK = "\uc9c0\uae08 \uc608\uc57d OK"
VERDICT_CHECK = "\ud655\uc778 \ud6c4 \uc608\uc57d"
VERDICT_BAD = "\ube44\ucd94\ucc9c"
OK_THRESHOLD = 70
NEGATIVE_LIMIT = 4


def clamp(value: float, low: int = 0, high: int = 100) -> int:
    return max(low, min(high, round(value)))


def as_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value]
    return []


def confidence_value(value: Any) -> float:
    if not isinstance(value, (int, float)):
        return 0.0
    return max(0.0, min(1.0, float(value)))


def analyze_axis(name: str, axis: dict[str, Any]) -> dict[str, Any]:
    positive = as_list(axis.get("positive"))
    negative = as_list(axis.get("negative"))
    sources = as_list(axis.get("sources"))
    confidence = confidence_value(axis.get("confidence", 0.0))

    # Evidence raises the score; real negatives lower it; uncertainty is a smaller penalty.
    if isinstance(axis.get("score"), (int, float)):
        axis_score = clamp(float(axis["score"]))
    else:
        axis_score = clamp(55 + 10 * len(positive) - 15 * len(negative) - (1.0 - confidence) * 10 - (0 if sources else 8))

    flags: list[str] = []
    drivers: list[str] = []

    if negative:
        flags.append("negative_signal")
        drivers.append(f"{name}: negative evidence - {'; '.join(negative)}")

    negative_text = " ".join(negative).lower()
    for term in CRITICAL_TERMS:
        if term in negative_text:
            flags.append(f"critical:{term}")
            drivers.append(f"{name}: critical signal '{term}' found")

    if confidence < 0.4:
        flags.append("low_confidence")
        drivers.append(f"{name}: low confidence {confidence:.2f}")
    if not sources:
        flags.append("missing_sources")
        drivers.append(f"{name}: no public source URL provided")

    return {
        "score": axis_score,
        "flags": flags,
        "drivers": drivers,
        "negative_count": len(negative),
        "critical_count": sum(flag.startswith("critical:") for flag in flags),
        "uncertainty_count": flags.count("low_confidence") + flags.count("missing_sources"),
    }


def decide(overall: int, analyses: dict[str, dict[str, Any]]) -> tuple[str, list[str]]:
    critical_count = sum(item["critical_count"] for item in analyses.values())
    negative_count = sum(item["negative_count"] for item in analyses.values())
    uncertainty_count = sum(item["uncertainty_count"] for item in analyses.values())

    drivers = [driver for item in analyses.values() for driver in item["drivers"]]

    if critical_count:
        drivers.append(f"verdict: {critical_count} critical signal(s) found")
        return VERDICT_BAD, drivers
    if negative_count >= NEGATIVE_LIMIT:
        drivers.append(f"verdict: {negative_count} negative signal(s), limit is {NEGATIVE_LIMIT - 1}")
        return VERDICT_BAD, drivers
    if overall >= OK_THRESHOLD and negative_count == 0 and uncertainty_count == 0:
        drivers.append(f"verdict: score {overall} >= {OK_THRESHOLD}, with sources and no negative signals")
        return VERDICT_OK, drivers

    if overall < OK_THRESHOLD:
        drivers.append(f"verdict: score {overall} < {OK_THRESHOLD}")
    if uncertainty_count:
        drivers.append(f"verdict: {uncertainty_count} uncertainty signal(s) need checking")
    if negative_count:
        drivers.append(f"verdict: {negative_count} non-critical negative signal(s) need checking")
    return VERDICT_CHECK, drivers


def score(payload: dict[str, Any]) -> dict[str, Any]:
    findings = payload.get("findings", {})
    analyses: dict[str, dict[str, Any]] = {}

    for name in AXES:
        raw_axis = findings.get(name, {}) if isinstance(findings, dict) else {}
        analyses[name] = analyze_axis(name, raw_axis if isinstance(raw_axis, dict) else {})

    axis_scores = {name: item["score"] for name, item in analyses.items()}
    overall = clamp(sum(axis_scores.values()) / len(AXES))
    verdict, drivers = decide(overall, analyses)

    return {
        "candidate": payload.get("candidate"),
        "city": payload.get("city"),
        "axis_scores": axis_scores,
        "overall_score": overall,
        "risk_flags": [f"{name}:{flag}" for name, item in analyses.items() for flag in item["flags"]],
        "verdict": verdict,
        "verdict_drivers": drivers,
    }


def load_payload(path: str | None) -> dict[str, Any]:
    raw = open(path, encoding="utf-8").read() if path else sys.stdin.read()
    payload = json.loads(raw)
    if not isinstance(payload, dict):
        raise SystemExit("Input JSON must be an object.")
    return payload


def self_test() -> None:
    good_axis = {"confidence": 0.9, "positive": ["recent reviews", "fair price", "clear policy"], "negative": [], "sources": ["https://example.com"]}
    unknown_axis = {"confidence": 0.2, "positive": [], "negative": [], "sources": []}
    bad_axis = {"confidence": 0.8, "positive": [], "negative": ["scam reports", "refund refusal"], "sources": ["https://example.com"]}

    good = score({"findings": {axis: good_axis for axis in AXES}})
    unknown = score({"findings": {axis: unknown_axis for axis in AXES}})
    bad = score({"findings": {axis: (bad_axis if axis in {"review_reliability", "operator_reliability"} else good_axis) for axis in AXES}})

    assert good["verdict"] == VERDICT_OK, good
    assert unknown["verdict"] == VERDICT_CHECK, unknown
    assert bad["verdict"] == VERDICT_BAD, bad
    print("self-test ok")


def main() -> None:
    parser = argparse.ArgumentParser(description="Score travel booking verification findings.")
    parser.add_argument("json_file", nargs="?", help="Findings JSON file. Reads stdin when omitted.")
    parser.add_argument("--self-test", action="store_true", help="Run built-in scorer checks.")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    print(json.dumps(score(load_payload(args.json_file)), ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
