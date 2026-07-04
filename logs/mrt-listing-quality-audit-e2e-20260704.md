# mrt-listing-quality-auditor E2E log - 2026-07-04

## Input product

- Candidate: MyRealTrip Vivid Sydney tour/cruise/ticket campaign listing
- City: Sydney, Australia
- MyRealTrip public source: https://www.myrealtrip.com/main/experiences
- Purpose: operator QA before publishing or expanding a campaign teaser into a sellable listing

## Public source URLs

- https://www.myrealtrip.com/main/experiences
- https://www.myrealtrip.com/
- https://auth.myrealtrip.com/terms/common/cancel
- https://www.vividsydney.com/
- https://www.vividsydney.com/visit/access-and-inclusion
- https://www.theguardian.com/culture/article/2024/jun/10/vivid-festival-sydney-crowd-crush-fears-nsw-premier-chris-minns

## Findings JSON

```json
{
  "candidate": "MyRealTrip Vivid Sydney tour/cruise/ticket campaign listing",
  "city": "Sydney, Australia",
  "findings": {
    "product_information_completeness": {
      "confidence": 0.55,
      "positive": [
        "MyRealTrip public tour-ticket page exposes a Vivid Sydney campaign/listing teaser",
        "The teaser says tour, cruise, and admission-ticket products are gathered"
      ],
      "missing": [
        "exact product or ticket type",
        "duration",
        "included and excluded items",
        "guide or language information",
        "age, accessibility, or physical restrictions"
      ],
      "unclear": [],
      "negative": [],
      "sources": ["https://www.myrealtrip.com/main/experiences"]
    },
    "booking_condition_clarity": {
      "confidence": 0.6,
      "positive": [
        "Vivid Sydney official page publishes 2026 festival dates and a 2027 return window",
        "Vivid official access page publishes event-specific travel and crowd planning guidance"
      ],
      "missing": [
        "reservation confirmation method",
        "weather or cancellation operation policy",
        "specific operating date and time for the purchasable product"
      ],
      "unclear": [],
      "negative": [],
      "sources": [
        "https://www.myrealtrip.com/main/experiences",
        "https://www.vividsydney.com/",
        "https://www.vividsydney.com/visit/access-and-inclusion"
      ]
    },
    "cancellation_refund_clarity": {
      "confidence": 0.65,
      "positive": ["MyRealTrip public footer links to a cancellation and refund policy"],
      "missing": [],
      "unclear": ["product-specific refund cutoff and no-show treatment are not visible in the checked public listing teaser"],
      "negative": [],
      "sources": [
        "https://www.myrealtrip.com/main/experiences",
        "https://auth.myrealtrip.com/terms/common/cancel"
      ]
    },
    "price_cost_transparency": {
      "confidence": 0.45,
      "positive": [],
      "missing": [
        "base price",
        "whether cruise or ticket fees are included",
        "local transport cost responsibility",
        "optional add-on cost"
      ],
      "unclear": [],
      "negative": [],
      "sources": ["https://www.myrealtrip.com/main/experiences"]
    },
    "route_meeting_point_risk": {
      "confidence": 0.75,
      "positive": [
        "Vivid official page says public transport is the best way to get around",
        "Vivid official page gives walking, train, light rail, ferry, road closure, and crowd guidance"
      ],
      "missing": ["exact MyRealTrip meeting point or pickup method"],
      "unclear": ["how the listing handles road closures, ferry crowding, and return transport after shows"],
      "negative": ["Vivid official page warns of road closures, high pedestrian volumes, busy ferries, and limited viewing space"],
      "sources": ["https://www.vividsydney.com/visit/access-and-inclusion"]
    },
    "review_cs_risk": {
      "confidence": 0.7,
      "positive": ["Vivid Sydney is an established public festival owned, managed, and produced by Destination NSW"],
      "missing": ["recent MyRealTrip product review count and rating distribution"],
      "unclear": [],
      "negative": ["Guardian reporting described crowd bottleneck and crowd-crush concerns at Vivid Sydney in 2024"],
      "sources": [
        "https://www.vividsydney.com/",
        "https://www.theguardian.com/culture/article/2024/jun/10/vivid-festival-sydney-crowd-crush-fears-nsw-premier-chris-minns"
      ]
    }
  }
}
```

## score.py raw output

```json
{
  "axis_scores": {
    "booking_condition_clarity": 36,
    "cancellation_refund_clarity": 56,
    "price_cost_transparency": 6,
    "product_information_completeness": 12,
    "review_cs_risk": 38,
    "route_meeting_point_risk": 38
  },
  "candidate": "MyRealTrip Vivid Sydney tour/cruise/ticket campaign listing",
  "city": "Sydney, Australia",
  "missing_information": [
    "product_information_completeness: exact product or ticket type",
    "product_information_completeness: duration",
    "product_information_completeness: included and excluded items",
    "product_information_completeness: guide or language information",
    "product_information_completeness: age, accessibility, or physical restrictions",
    "booking_condition_clarity: reservation confirmation method",
    "booking_condition_clarity: weather or cancellation operation policy",
    "booking_condition_clarity: specific operating date and time for the purchasable product",
    "cancellation_refund_clarity: product-specific refund cutoff and no-show treatment are not visible in the checked public listing teaser",
    "price_cost_transparency: base price",
    "price_cost_transparency: whether cruise or ticket fees are included",
    "price_cost_transparency: local transport cost responsibility",
    "price_cost_transparency: optional add-on cost",
    "route_meeting_point_risk: exact MyRealTrip meeting point or pickup method",
    "route_meeting_point_risk: how the listing handles road closures, ferry crowding, and return transport after shows",
    "review_cs_risk: recent MyRealTrip product review count and rating distribution"
  ],
  "overall_score": 31,
  "partner_questions": [
    "Please confirm and provide listing copy for: exact product or ticket type",
    "Please confirm and provide listing copy for: duration",
    "Please confirm and provide listing copy for: included and excluded items",
    "Please confirm and provide listing copy for: guide or language information",
    "Please confirm and provide listing copy for: age, accessibility, or physical restrictions",
    "Please confirm and provide listing copy for: reservation confirmation method",
    "Please confirm and provide listing copy for: weather or cancellation operation policy",
    "Please confirm and provide listing copy for: specific operating date and time for the purchasable product",
    "Please confirm and provide listing copy for: product-specific refund cutoff and no-show treatment are not visible in the checked public listing teaser",
    "Please confirm and provide listing copy for: base price",
    "Please confirm and provide listing copy for: whether cruise or ticket fees are included",
    "Please confirm and provide listing copy for: local transport cost responsibility",
    "Please confirm and provide listing copy for: optional add-on cost",
    "Please confirm and provide listing copy for: exact MyRealTrip meeting point or pickup method",
    "Please confirm and provide listing copy for: how the listing handles road closures, ferry crowding, and return transport after shows",
    "Please confirm and provide listing copy for: recent MyRealTrip product review count and rating distribution"
  ],
  "risk_flags": [
    "product_information_completeness:missing_required_information",
    "booking_condition_clarity:missing_required_information",
    "cancellation_refund_clarity:unclear_information",
    "price_cost_transparency:missing_required_information",
    "route_meeting_point_risk:missing_required_information",
    "route_meeting_point_risk:unclear_information",
    "route_meeting_point_risk:negative_signal",
    "review_cs_risk:missing_required_information",
    "review_cs_risk:negative_signal"
  ],
  "verdict": "게시 보류",
  "verdict_drivers": [
    "product_information_completeness: missing information - exact product or ticket type; duration; included and excluded items; guide or language information; age, accessibility, or physical restrictions",
    "booking_condition_clarity: missing information - reservation confirmation method; weather or cancellation operation policy; specific operating date and time for the purchasable product",
    "cancellation_refund_clarity: unclear information - product-specific refund cutoff and no-show treatment are not visible in the checked public listing teaser",
    "price_cost_transparency: missing information - base price; whether cruise or ticket fees are included; local transport cost responsibility; optional add-on cost",
    "route_meeting_point_risk: missing information - exact MyRealTrip meeting point or pickup method",
    "route_meeting_point_risk: unclear information - how the listing handles road closures, ferry crowding, and return transport after shows",
    "route_meeting_point_risk: negative signal - Vivid official page warns of road closures, high pedestrian volumes, busy ferries, and limited viewing space",
    "review_cs_risk: missing information - recent MyRealTrip product review count and rating distribution",
    "review_cs_risk: negative signal - Guardian reporting described crowd bottleneck and crowd-crush concerns at Vivid Sydney in 2024",
    "verdict: 16 missing/unclear item(s), hold limit is 7"
  ]
}
```

## Final operator QA report

- Verdict: 게시 보류
- Overall score: 31
- Reason: the public MyRealTrip teaser proves the campaign exists, but it is not complete enough to publish as a sellable tour/activity listing. Core information such as exact ticket/product type, price, inclusions, operating date/time, refund cutoff, meeting/pickup method, and crowd/transport handling is missing or unclear.
- Main CS/booking-dropoff triggers:
  - Customers cannot tell what they are buying: tour, cruise, admission ticket, or bundled package.
  - Price and included costs are not visible in the checked public listing teaser.
  - Vivid Sydney has high pedestrian volume, road closure, ferry crowding, and limited viewing-space risks.
  - Product-specific cancellation/refund cutoff is not visible.

## Partner completion questions

1. What exact product is being sold: guided tour, cruise, admission ticket, or bundle?
2. What is the duration, start time, end time, and operating date range?
3. What is included and excluded: ticket, cruise fare, guide, food, local transport, insurance?
4. What is the base price and what optional costs can customers pay on site?
5. What is the exact meeting point or pickup method?
6. How will the product handle Vivid road closures, ferry congestion, and return transport?
7. What is the product-specific cancellation/refund cutoff and no-show rule?
8. Are there age, accessibility, or physical restrictions?
9. Do recent MyRealTrip reviews exist, and are there recurring CS issues?

## Suggested listing copy

```text
상품 유형: [가이드 투어/크루즈/입장권/패키지 중 선택]
운영 일정: [운영 날짜], [시작 시간] - [종료 시간]
집합 장소: [정확한 주소] ([Google Maps 링크])
포함 사항: [예: 크루즈 티켓, 가이드, 입장권]
불포함 사항: [예: 식사, 개인 교통비, 여행자보험]
교통/혼잡 안내: Vivid Sydney 기간에는 도로 통제와 보행자 혼잡이 예상됩니다. 대중교통 이용과 여유 있는 이동 시간을 권장합니다.
취소/환불: [무료 취소 가능 시점], [부분 환불 여부], [노쇼 처리 기준]
```

## Could not verify

- Exact MyRealTrip product detail page URL.
- Product-specific price and availability.
- Recent product reviews and rating distribution.
- Partner/operator name.
- Product-specific refund cutoff.

## What this test verified

- The new scorer detects an operator QA failure rather than producing a traveler booking recommendation.
- Missing required listing information is surfaced as `missing_information`.
- Partner completion questions are generated from the missing/unclear fields.
- Public evidence is enough to justify a hold decision for an incomplete campaign/listing teaser.

## Limitations

- The checked public MyRealTrip page exposed a campaign/listing teaser, not a full detail page.
- No login-only MyRealTrip data, internal API, private logs, or secret metrics were used.
