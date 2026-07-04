#!/usr/bin/env python3
"""Score public QA findings for MyRealTrip listing audits."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any


AXES = (
    "product_information_completeness",
    "booking_condition_clarity",
    "cancellation_refund_clarity",
    "price_cost_transparency",
    "route_meeting_point_risk",
    "review_cs_risk",
)

CRITICAL_TERMS = (
    "refund refusal",
    "forced shopping",
    "scam",
    "fraud",
    "no-show",
    "unsafe",
    "illegal",
    "cancelled without notice",
)

VERDICT_APPROVE = "\uc2b9\uc778 \uac00\ub2a5"
VERDICT_COMPLETE = "\ubcf4\uc644 \ud6c4 \uac8c\uc2dc"
VERDICT_HOLD = "\uac8c\uc2dc \ubcf4\ub958"
APPROVE_THRESHOLD = 80
NEGATIVE_LIMIT = 3
MISSING_HOLD_LIMIT = 8


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


def question_for(item: str) -> str:
    return f"다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: {item}"


def analyze_axis(name: str, axis: dict[str, Any]) -> dict[str, Any]:
    positive = as_list(axis.get("positive"))
    missing = as_list(axis.get("missing")) + as_list(axis.get("missing_information"))
    unclear = as_list(axis.get("unclear"))
    negative = as_list(axis.get("negative"))
    sources = as_list(axis.get("sources"))
    confidence = confidence_value(axis.get("confidence", 0.0))

    if isinstance(axis.get("score"), (int, float)):
        axis_score = clamp(float(axis["score"]))
    else:
        axis_score = clamp(
            60
            + 8 * len(positive)
            - 12 * len(missing)
            - 8 * len(unclear)
            - 15 * len(negative)
            - (1.0 - confidence) * 10
            - (0 if sources else 8)
        )

    flags: list[str] = []
    drivers: list[str] = []

    if missing:
        flags.append("missing_required_information")
        drivers.append(f"{name}: missing information - {'; '.join(missing)}")
    if unclear:
        flags.append("unclear_information")
        drivers.append(f"{name}: unclear information - {'; '.join(unclear)}")
    if negative:
        flags.append("negative_signal")
        drivers.append(f"{name}: negative signal - {'; '.join(negative)}")

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

    questions = as_list(axis.get("partner_questions")) or [question_for(item) for item in missing + unclear]

    return {
        "score": axis_score,
        "flags": flags,
        "drivers": drivers,
        "missing": [f"{name}: {item}" for item in missing + unclear],
        "questions": questions,
        "negative_count": len(negative),
        "critical_count": sum(flag.startswith("critical:") for flag in flags),
        "missing_count": len(missing) + len(unclear),
        "uncertainty_count": flags.count("low_confidence") + flags.count("missing_sources"),
    }


def decide(overall: int, analyses: dict[str, dict[str, Any]]) -> tuple[str, list[str]]:
    critical_count = sum(item["critical_count"] for item in analyses.values())
    negative_count = sum(item["negative_count"] for item in analyses.values())
    missing_count = sum(item["missing_count"] for item in analyses.values())
    uncertainty_count = sum(item["uncertainty_count"] for item in analyses.values())

    drivers = [driver for item in analyses.values() for driver in item["drivers"]]

    if critical_count:
        drivers.append(f"verdict: {critical_count} critical signal(s) found")
        return VERDICT_HOLD, drivers
    if negative_count >= NEGATIVE_LIMIT:
        drivers.append(f"verdict: {negative_count} negative signal(s), limit is {NEGATIVE_LIMIT - 1}")
        return VERDICT_HOLD, drivers
    if missing_count >= MISSING_HOLD_LIMIT:
        drivers.append(f"verdict: {missing_count} missing/unclear item(s), hold limit is {MISSING_HOLD_LIMIT - 1}")
        return VERDICT_HOLD, drivers
    if overall >= APPROVE_THRESHOLD and missing_count == 0 and negative_count == 0 and uncertainty_count == 0:
        drivers.append(f"verdict: score {overall} >= {APPROVE_THRESHOLD}, with no missing information or risk signals")
        return VERDICT_APPROVE, drivers

    if overall < APPROVE_THRESHOLD:
        drivers.append(f"verdict: score {overall} < {APPROVE_THRESHOLD}")
    if missing_count:
        drivers.append(f"verdict: {missing_count} missing/unclear item(s) need completion")
    if uncertainty_count:
        drivers.append(f"verdict: {uncertainty_count} uncertainty signal(s) need checking")
    if negative_count:
        drivers.append(f"verdict: {negative_count} non-critical negative signal(s) need checking")
    return VERDICT_COMPLETE, drivers


def score(payload: dict[str, Any]) -> dict[str, Any]:
    findings = payload.get("findings", {})
    analyses: dict[str, dict[str, Any]] = {}

    for name in AXES:
        raw_axis = findings.get(name, {}) if isinstance(findings, dict) else {}
        analyses[name] = analyze_axis(name, raw_axis if isinstance(raw_axis, dict) else {})

    axis_scores = {name: item["score"] for name, item in analyses.items()}
    overall = clamp(sum(axis_scores.values()) / len(AXES))
    verdict, drivers = decide(overall, analyses)

    missing_information = [item for analysis in analyses.values() for item in analysis["missing"]]
    partner_questions = [item for analysis in analyses.values() for item in analysis["questions"]]

    return {
        "candidate": payload.get("candidate"),
        "city": payload.get("city"),
        "axis_scores": axis_scores,
        "overall_score": overall,
        "risk_flags": [f"{name}:{flag}" for name, item in analyses.items() for flag in item["flags"]],
        "verdict": verdict,
        "verdict_drivers": drivers,
        "missing_information": missing_information,
        "partner_questions": partner_questions,
    }


def load_payload(path: str | None) -> dict[str, Any]:
    raw = open(path, encoding="utf-8").read() if path else sys.stdin.read()
    payload = json.loads(raw)
    if not isinstance(payload, dict):
        raise SystemExit("Input JSON must be an object.")
    return payload


def self_test() -> None:
    good_axis = {"confidence": 0.9, "positive": ["duration clear", "source backed", "policy visible"], "missing": [], "unclear": [], "negative": [], "sources": ["https://example.com"]}
    complete_axis = {"confidence": 0.7, "positive": ["base copy visible"], "missing": ["meeting point"], "unclear": ["rain operation"], "negative": [], "sources": ["https://example.com"]}
    hold_axis = {"confidence": 0.8, "positive": [], "missing": ["meeting point", "duration", "inclusions"], "unclear": [], "negative": ["refund refusal and forced shopping complaints"], "sources": ["https://example.com"]}
    unknown_axis = {"confidence": 0.2, "positive": [], "missing": [], "unclear": [], "negative": [], "sources": []}

    good = score({"findings": {axis: good_axis for axis in AXES}})
    complete = score({"findings": {axis: (complete_axis if axis in {"product_information_completeness", "booking_condition_clarity"} else good_axis) for axis in AXES}})
    hold = score({"findings": {axis: (hold_axis if axis in {"product_information_completeness", "review_cs_risk"} else good_axis) for axis in AXES}})
    unknown = score({"findings": {axis: unknown_axis for axis in AXES}})

    assert good["verdict"] == VERDICT_APPROVE, good
    assert complete["verdict"] == VERDICT_COMPLETE, complete
    assert hold["verdict"] == VERDICT_HOLD, hold
    assert unknown["verdict"] == VERDICT_COMPLETE, unknown
    print("self-test ok")


def main() -> None:
    parser = argparse.ArgumentParser(description="Score MyRealTrip listing QA findings.")
    parser.add_argument("json_file", nargs="?", help="Findings JSON file. Reads stdin when omitted.")
    parser.add_argument("--self-test", action="store_true", help="Run built-in scorer checks.")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    print(json.dumps(score(load_payload(args.json_file)), ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
