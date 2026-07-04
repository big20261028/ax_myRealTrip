# MRT Listing Quality Auditor E2E Detail Attempt - 2026-07-04

## Input Product

- Candidate: MyRealTrip Hong Kong Disneyland Disney Run / Magic Run Festa campaign listing
- City: Hong Kong
- MyRealTrip public page checked: https://www.myrealtrip.com/main/experiences

## Public Source URLs

- https://www.myrealtrip.com/main/experiences
- https://auth.myrealtrip.com/terms/common/cancel
- https://www.hongkongdisneyland.com/calendars/day/
- https://www.hongkongdisneyland.com/guest-services/guests-with-disabilities/
- https://en.wikipedia.org/wiki/Hong_Kong_Disneyland

## Public Evidence Collected

- MyRealTrip public tour-ticket page showed a Hong Kong Disneyland Disney Run / Magic Run Festa teaser and campaign period `5.27 - 10.4`.
- MyRealTrip public footer linked to the cancellation/refund policy page.
- Hong Kong Disneyland public pages stated that guests need a valid park reservation for visits and should refer to the park calendar for opening hours and show times.
- Hong Kong Disneyland public accessibility page listed disability support services and guest support locations.
- Public information on Hong Kong Disneyland noted historical overcrowding/capacity criticism, so event-day crowd and access guidance should be explicit.

## Findings JSON

```json
{
  "candidate": "MyRealTrip Hong Kong Disneyland Disney Run / Magic Run Festa campaign listing",
  "city": "Hong Kong",
  "findings": {
    "product_information_completeness": {
      "confidence": 0.5,
      "positive": [
        "MyRealTrip public tour-ticket page exposes a Hong Kong Disneyland Disney Run / Magic Run Festa campaign teaser",
        "The teaser identifies it as a Hong Kong Disneyland run/festival participation offer"
      ],
      "missing": [
        "exact race or ticket product type",
        "race distance/category",
        "start time and duration",
        "included and excluded items",
        "participant age or fitness restrictions"
      ],
      "unclear": [],
      "negative": [],
      "sources": [
        "https://www.myrealtrip.com/main/experiences"
      ]
    },
    "booking_condition_clarity": {
      "confidence": 0.5,
      "positive": [
        "MyRealTrip public teaser exposes a campaign period of 5.27 - 10.4"
      ],
      "missing": [
        "reservation confirmation method",
        "event date versus sale campaign date distinction",
        "weather or event cancellation policy",
        "capacity or registration closing condition"
      ],
      "unclear": [],
      "negative": [],
      "sources": [
        "https://www.myrealtrip.com/main/experiences"
      ]
    },
    "cancellation_refund_clarity": {
      "confidence": 0.6,
      "positive": [
        "MyRealTrip public footer links to a cancellation and refund policy"
      ],
      "missing": [],
      "unclear": [
        "product-specific refund cutoff, transferability, and event cancellation handling are not visible in the checked public teaser"
      ],
      "negative": [],
      "sources": [
        "https://www.myrealtrip.com/main/experiences",
        "https://auth.myrealtrip.com/terms/common/cancel"
      ]
    },
    "price_cost_transparency": {
      "confidence": 0.35,
      "positive": [],
      "missing": [
        "base price",
        "what the registration fee includes",
        "whether Hong Kong Disneyland admission is included",
        "onsite pickup or delivery fee",
        "optional merchandise or add-on cost"
      ],
      "unclear": [],
      "negative": [],
      "sources": [
        "https://www.myrealtrip.com/main/experiences"
      ]
    },
    "route_meeting_point_risk": {
      "confidence": 0.55,
      "positive": [
        "Hong Kong Disneyland requires park reservations for visits and publishes daily park hours",
        "Hong Kong Disneyland publishes accessibility services and guest support information"
      ],
      "missing": [
        "exact meeting or check-in location",
        "packet pickup method",
        "arrival buffer time",
        "post-event exit guidance"
      ],
      "unclear": [],
      "negative": [],
      "sources": [
        "https://www.myrealtrip.com/main/experiences",
        "https://www.hongkongdisneyland.com/calendars/day/",
        "https://www.hongkongdisneyland.com/guest-services/guests-with-disabilities/"
      ]
    },
    "review_cs_risk": {
      "confidence": 0.5,
      "positive": [
        "Hong Kong Disneyland is an established public attraction"
      ],
      "missing": [
        "recent MyRealTrip product review count and rating distribution",
        "partner/operator response history"
      ],
      "unclear": [],
      "negative": [
        "public information notes Hong Kong Disneyland has had historical overcrowding/capacity criticism, so event-day crowd and access guidance should be explicit"
      ],
      "sources": [
        "https://www.myrealtrip.com/main/experiences",
        "https://en.wikipedia.org/wiki/Hong_Kong_Disneyland"
      ]
    }
  }
}
```

## score.py Raw Output

```json
{
  "axis_scores": {
    "booking_condition_clarity": 15,
    "cancellation_refund_clarity": 56,
    "price_cost_transparency": 0,
    "product_information_completeness": 11,
    "review_cs_risk": 24,
    "route_meeting_point_risk": 24
  },
  "candidate": "MyRealTrip Hong Kong Disneyland Disney Run / Magic Run Festa campaign listing",
  "city": "Hong Kong",
  "missing_information": [
    "product_information_completeness: exact race or ticket product type",
    "product_information_completeness: race distance/category",
    "product_information_completeness: start time and duration",
    "product_information_completeness: included and excluded items",
    "product_information_completeness: participant age or fitness restrictions",
    "booking_condition_clarity: reservation confirmation method",
    "booking_condition_clarity: event date versus sale campaign date distinction",
    "booking_condition_clarity: weather or event cancellation policy",
    "booking_condition_clarity: capacity or registration closing condition",
    "cancellation_refund_clarity: product-specific refund cutoff, transferability, and event cancellation handling are not visible in the checked public teaser",
    "price_cost_transparency: base price",
    "price_cost_transparency: what the registration fee includes",
    "price_cost_transparency: whether Hong Kong Disneyland admission is included",
    "price_cost_transparency: onsite pickup or delivery fee",
    "price_cost_transparency: optional merchandise or add-on cost",
    "route_meeting_point_risk: exact meeting or check-in location",
    "route_meeting_point_risk: packet pickup method",
    "route_meeting_point_risk: arrival buffer time",
    "route_meeting_point_risk: post-event exit guidance",
    "review_cs_risk: recent MyRealTrip product review count and rating distribution",
    "review_cs_risk: partner/operator response history"
  ],
  "overall_score": 22,
  "partner_questions": [
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: exact race or ticket product type",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: race distance/category",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: start time and duration",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: included and excluded items",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: participant age or fitness restrictions",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: reservation confirmation method",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: event date versus sale campaign date distinction",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: weather or event cancellation policy",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: capacity or registration closing condition",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: product-specific refund cutoff, transferability, and event cancellation handling are not visible in the checked public teaser",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: base price",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: what the registration fee includes",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: whether Hong Kong Disneyland admission is included",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: onsite pickup or delivery fee",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: optional merchandise or add-on cost",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: exact meeting or check-in location",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: packet pickup method",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: arrival buffer time",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: post-event exit guidance",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: recent MyRealTrip product review count and rating distribution",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: partner/operator response history"
  ],
  "risk_flags": [
    "product_information_completeness:missing_required_information",
    "booking_condition_clarity:missing_required_information",
    "cancellation_refund_clarity:unclear_information",
    "price_cost_transparency:missing_required_information",
    "price_cost_transparency:low_confidence",
    "route_meeting_point_risk:missing_required_information",
    "review_cs_risk:missing_required_information",
    "review_cs_risk:negative_signal"
  ],
  "verdict": "게시 보류",
  "verdict_drivers": [
    "product_information_completeness: missing information - exact race or ticket product type; race distance/category; start time and duration; included and excluded items; participant age or fitness restrictions",
    "booking_condition_clarity: missing information - reservation confirmation method; event date versus sale campaign date distinction; weather or event cancellation policy; capacity or registration closing condition",
    "cancellation_refund_clarity: unclear information - product-specific refund cutoff, transferability, and event cancellation handling are not visible in the checked public teaser",
    "price_cost_transparency: missing information - base price; what the registration fee includes; whether Hong Kong Disneyland admission is included; onsite pickup or delivery fee; optional merchandise or add-on cost",
    "price_cost_transparency: low confidence 0.35",
    "route_meeting_point_risk: missing information - exact meeting or check-in location; packet pickup method; arrival buffer time; post-event exit guidance",
    "review_cs_risk: missing information - recent MyRealTrip product review count and rating distribution; partner/operator response history",
    "review_cs_risk: negative signal - public information notes Hong Kong Disneyland has had historical overcrowding/capacity criticism, so event-day crowd and access guidance should be explicit",
    "verdict: 21 missing/unclear item(s), hold limit is 7"
  ]
}
```

## Final Operator QA Report

- Verdict: 게시 보류
- Overall score: 22
- Main reason: the checked MyRealTrip public page is only a campaign/listing teaser, not a complete product detail page. Core publish-required details are missing across product info, booking conditions, price transparency, route/check-in guidance, and review/CS evidence.
- Product information completeness: missing race or ticket type, distance/category, start time, duration, inclusions/exclusions, and restrictions.
- Booking condition clarity: missing reservation confirmation method, distinction between sale period and event date, weather/cancellation behavior, and capacity/closing condition.
- Cancellation/refund clarity: generic MyRealTrip policy link is visible from the public page, but product-specific refund cutoff and event-cancellation handling are not visible.
- Price/cost transparency: no checked public source confirmed base price, included items, park admission inclusion, onsite fees, or add-on costs.
- Route/meeting point risk: Hong Kong Disneyland publishes park reservation and accessibility information, but the listing teaser does not expose check-in location, packet pickup, arrival buffer, or exit guidance.
- Review/CS risk: historical crowd/capacity criticism creates a customer guidance risk; no MyRealTrip review count or partner response history was publicly confirmed.

## Partner Follow-up Questions

- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: exact race or ticket product type
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: race distance/category
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: start time and duration
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: included and excluded items
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: participant age or fitness restrictions
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: reservation confirmation method
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: event date versus sale campaign date distinction
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: weather or event cancellation policy
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: capacity or registration closing condition
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: product-specific refund cutoff, transferability, and event cancellation handling are not visible in the checked public teaser
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: base price
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: what the registration fee includes
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: whether Hong Kong Disneyland admission is included
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: onsite pickup or delivery fee
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: optional merchandise or add-on cost
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: exact meeting or check-in location
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: packet pickup method
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: arrival buffer time
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: post-event exit guidance
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: recent MyRealTrip product review count and rating distribution
- 다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: partner/operator response history

## Suggested Listing Copy / Page Edits

- 상품명 아래에 실제 상품 유형을 명시: 예) 홍콩 디즈니랜드 러닝 이벤트 참가권 / 패키지 / 입장권 포함 여부.
- 캠페인 기간 `5.27 - 10.4`와 실제 행사일, 예약 가능일, 참가 마감일을 분리해서 표기.
- 포함/불포함 항목에 디즈니랜드 입장권 포함 여부, 참가비 포함 범위, 현장 추가 비용, 굿즈/보험/식사 포함 여부를 분리해서 표기.
- 예약 확정 방식, 바우처 수령 방식, 참가권 또는 패킷 픽업 방식을 예약 전 안내 영역에 추가.
- 비/악천후, 주최 측 취소, 고객 개인 사정 취소, 양도 가능 여부를 취소/환불 섹션에 상품별로 요약.
- 체크인 장소, 권장 도착 시간, 이동 동선, 행사 종료 후 퇴장/대중교통 안내를 지도 또는 텍스트로 추가.
- 혼잡 가능성이 있는 이벤트형 상품임을 안내하고, 유아/고령자/장애인 동반 시 참고할 접근성 정보를 연결.

## Unverified Items

- Complete MyRealTrip product detail URL: 확인 불가
- Exact race category and distance: 확인 불가
- Event date and start time: 확인 불가
- Included and excluded items: 확인 불가
- Base price and add-on costs: 확인 불가
- Product-specific refund cutoff: 확인 불가
- MyRealTrip review count/rating distribution: 확인 불가
- Partner/operator response history: 확인 불가

## What This Test Verified

- `score.py` accepts a realistic public-evidence findings JSON for an operator listing QA workflow.
- The scorer produces Korean default `partner_questions` when the input does not provide custom partner questions.
- A teaser-only public listing with broad missing core details is deterministically classified as `게시 보류`.
- The output exposes the judgment reasons through `risk_flags`, `verdict_drivers`, `missing_information`, and `partner_questions`.

## Limitations

- A complete MyRealTrip product detail URL for this campaign could not be found through the public web search/opened HTML used in this run.
- No internal API, login-only page, paid API, private data, or guessed commercial metric was used.
- Because the checked MyRealTrip page was a campaign teaser, this is a detail-page approximation rather than proof that a complete detail page was audited.
- The Wikipedia source is used only as a public supporting risk signal for historical crowd/capacity criticism, not as product-specific MyRealTrip evidence.
