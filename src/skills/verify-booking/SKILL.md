---
name: verify-booking
description: 여행 상품 예약 전, 도시와 후보 투어/숙소/액티비티를 공개 자료로 신뢰도 검증하고 결정 카드(confidence card)를 생성할 때 사용.
---

# Verify Booking

Use this skill when the user gives a city plus one or more travel booking candidates, such as a tour, stay, activity name, or URL, and asks whether it is safe or sensible to book now.

Only use public web sources. Do not use private APIs, internal data, logged-in-only content, or invented evidence.

## Inputs

- City or travel area.
- One or more candidate products: tour, accommodation, activity name, or URL.
- Optional trip dates, stay location, schedule constraints, budget, or traveler priorities.

Process each candidate separately when multiple candidates are provided.

## Workflow

1. Normalize the candidate name, city, provider, URL, dates, and any known price.
2. Search the web for public evidence. Keep source URLs for every claim.
3. Verify six axes:
   - Review reliability: count, recency, rating distribution, and repeated negative signals such as no-show, refund refusal, misleading photos, or aggressive selling.
   - Price fairness: whether the listed price is unusually cheap or expensive compared with similar public listings.
   - Location and routing: distance between stay and tour/activity, access difficulty, and schedule conflicts.
   - Operator reliability: cancellation/refund policy, recent operation traces, and whether contact channels look usable.
   - Traps and risks: tourist overcharging, forced shopping, bait listing patterns, or bundled upsell pressure.
   - Context: seasonality, opening hours, local holidays, closures, weather-sensitive operation, or date-specific constraints.
4. Put the findings into JSON and run `scripts/score.py` to calculate axis scores, total score, risk flags, verdict drivers, and final decision.
5. Output a confidence card for each candidate.

## Findings JSON

Pass JSON in this shape to `scripts/score.py`. Extra fields are allowed, but do not omit uncertainty.

```json
{
  "candidate": "Example food tour",
  "city": "Bangkok",
  "findings": {
    "review_reliability": {
      "confidence": 0.8,
      "positive": ["500+ reviews", "recent reviews in the last month"],
      "negative": ["some refund complaints"],
      "sources": ["https://example.com/reviews"]
    },
    "price_fairness": {
      "confidence": 0.7,
      "positive": ["price matches similar tours"],
      "negative": [],
      "sources": ["https://example.com/compare"]
    },
    "location_routing": {
      "confidence": 0.6,
      "positive": ["near metro"],
      "negative": ["pickup point not confirmed"],
      "sources": ["https://example.com/map"]
    },
    "operator_reliability": {
      "confidence": 0.7,
      "positive": ["clear cancellation policy"],
      "negative": [],
      "sources": ["https://example.com/policy"]
    },
    "traps_risks": {
      "confidence": 0.5,
      "positive": [],
      "negative": ["shopping stop mentioned"],
      "sources": ["https://example.com/itinerary"]
    },
    "context": {
      "confidence": 0.6,
      "positive": ["open on selected date"],
      "negative": [],
      "sources": ["https://example.com/hours"]
    }
  }
}
```

## Decision Card

Return this structure:

- Verdict: `지금 예약 OK`, `확인 후 예약`, or `비추천`.
- Overall score and confidence level.
- Six-axis summary with evidence bullets and source URLs.
- Risk flags.
- Verdict drivers from `score.py`, so the reason behind the verdict is visible.
- Remaining uncertainty: list every item that could not be verified.
- One-line reason: "그래서 지금 예약해도 되는 이유".

## Missing Information Rule

Never make up evidence. If public evidence is missing, say so, list it under remaining uncertainty, lower confidence, and prefer `확인 후 예약` over `지금 예약 OK`.

Do not turn missing evidence alone into `비추천`. Use `비추천` only when the findings include critical signals such as scam/refund refusal/forced shopping, or many real negative signals. A candidate with low confidence and missing sources but no negative evidence should be `확인 후 예약`.

## Scoring Behavior

`scripts/score.py` is deterministic. The same findings JSON always returns the same axis scores, risk flags, verdict drivers, and verdict.

- `지금 예약 OK`: overall score is at least 70, every axis has source URLs, confidence is not low, and there are no negative signals.
- `확인 후 예약`: evidence is incomplete, the score is below the OK threshold, or there are non-critical concerns that need human checking.
- `비추천`: critical signals are present, or the candidate has many real negative signals.
