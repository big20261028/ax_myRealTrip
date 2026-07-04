---
name: audit-listing
description: 마이리얼트립 투어·액티비티 상품 상세페이지를 운영자 관점에서 QA하고, 예약 저해 요소, 정보 누락, CS 유발 요소, 파트너 보완 질문, 상세페이지 개선안을 생성할 때 사용.
---

# Audit Listing

Use this skill for MyRealTrip product operators, partner onboarding managers, content QA reviewers, and CS/operations teams who need to audit a public tour or activity listing before publishing or improving it.

This is not a traveler booking recommendation. The output is an operator QA report that identifies missing listing details, unclear booking conditions, likely CS triggers, partner follow-up questions, and suggested listing copy.

Only use public web sources. Do not use internal APIs, private data, login-only pages, paid APIs, secret logs, or guessed numbers. Every evidence-based claim needs a source URL. If something cannot be confirmed publicly, mark it as `확인 불가`.

## Inputs

- Product name or public product URL.
- City/country.
- Optional: existing product description text.
- Optional: comparable public product URLs.

Process each product separately when multiple products are provided.

## Workflow

1. Normalize product name, URL, destination, operator/platform, and any visible price.
2. Collect public evidence from the listing page, MyRealTrip public pages, public policy pages, destination/venue pages, public reviews, or comparable public listings.
3. Audit six QA axes:
   - `product_information_completeness`: schedule, duration, meeting point, transport, language, inclusions/exclusions, preparation items, age/fitness limits.
   - `booking_condition_clarity`: minimum departure count, confirmation method, rain/weather operation, seasonality, closing days, operating days, schedule-change possibility.
   - `cancellation_refund_clarity`: whether cancellation/refund terms are understandable from listing copy and public policy.
   - `price_cost_transparency`: base price plus entrance fees, meals, tips, local transport, optional costs, and other extra costs.
   - `route_meeting_point_risk`: exact meeting address, accessibility, long-distance routing risk, schedule collision, local transit variables.
   - `review_cs_risk`: public reviews, external reports, crowding, queues, forced shopping, refund complaints, response problems, or signals likely to create customer questions.
4. Convert findings into JSON and run `scripts/score.py`.
5. Produce an operator QA report.

## Findings JSON

Use this shape for `scripts/score.py`. Extra fields are allowed.

```json
{
  "candidate": "Example Paris day tour",
  "city": "Paris",
  "findings": {
    "product_information_completeness": {
      "confidence": 0.8,
      "positive": ["duration is visible", "included guide language is stated"],
      "missing": ["exact meeting point"],
      "unclear": ["fitness requirement"],
      "negative": [],
      "sources": ["https://example.com/listing"],
      "partner_questions": ["정확한 집합 장소 주소와 지도 링크를 제공할 수 있나요?"]
    },
    "booking_condition_clarity": {
      "confidence": 0.7,
      "positive": ["date calendar is visible"],
      "missing": ["minimum departure count", "rain operation policy"],
      "unclear": [],
      "negative": [],
      "sources": ["https://example.com/listing"]
    },
    "cancellation_refund_clarity": {
      "confidence": 0.7,
      "positive": ["public cancellation policy URL exists"],
      "missing": [],
      "unclear": ["listing copy does not summarize refund cutoff"],
      "negative": [],
      "sources": ["https://example.com/cancel"]
    },
    "price_cost_transparency": {
      "confidence": 0.8,
      "positive": ["base price is visible"],
      "missing": ["entrance fee inclusion"],
      "unclear": [],
      "negative": [],
      "sources": ["https://example.com/listing"]
    },
    "route_meeting_point_risk": {
      "confidence": 0.6,
      "positive": ["destinations are public tourist sites"],
      "missing": ["return time"],
      "unclear": ["traffic delay handling"],
      "negative": [],
      "sources": ["https://example.com/map"]
    },
    "review_cs_risk": {
      "confidence": 0.6,
      "positive": [],
      "missing": ["recent review count"],
      "unclear": [],
      "negative": ["public reports mention crowding"],
      "sources": ["https://example.com/reviews"]
    }
  }
}
```

## Score Output

`score.py` returns:

- `axis_scores`
- `overall_score`
- `risk_flags`
- `verdict`: `승인 가능`, `보완 후 게시`, or `게시 보류`
- `verdict_drivers`
- `missing_information`
- `partner_questions`

## Verdict Rules

- `승인 가능`: required information is mostly complete, source-backed evidence exists, and no meaningful risk or unclear item remains.
- `보완 후 게시`: the product itself does not look unsafe, but the listing needs completion or clarification before publishing.
- `게시 보류`: critical negative signals exist, severe refund/operation/customer-harm risk exists, or core required information is missing too broadly to publish.

Do not use `게시 보류` only because public information is sparse. If information is sparse but no severe risk is found, prefer `보완 후 게시` and list the uncertainty.

## Final QA Report

Return:

- Final verdict.
- Overall score.
- Axis-by-axis QA summary with source URLs.
- Missing or unclear information.
- Customer inquiry or booking-dropoff triggers.
- Partner follow-up questions.
- Suggested listing copy or page edits.
- Evidence URLs.
- Items that could not be verified from public sources.
