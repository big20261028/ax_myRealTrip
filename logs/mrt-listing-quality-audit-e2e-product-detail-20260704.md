# MRT Listing Quality Auditor E2E Product Detail - 2026-07-04

## Input Product

- Product name: [1일권] 유니버설 스튜디오 재팬 스마트 콤보(마이리얼트립 포인트 10,000P 증정)
- City/country: Osaka, Japan
- Product URL: https://experiences.myrealtrip.com/products/6083103
- Alternate public URL found from MyRealTrip HTML/canonical data: https://www.myrealtrip.com/offers/179375
- Product type: ticket/activity product, Universal Studios Japan 1-day pass plus MyRealTrip point benefit
- Selection reason: unlike the earlier campaign teaser E2Es, this page is a public product detail page with title, region, price schema, rating/review count, usage sections, inclusions/exclusions, FAQ-like booking conditions, and cancellation/refund copy.

## Candidate Search Notes

| Candidate | URL | Public access | Detail exposure | E2E fit | Decision |
| --- | --- | --- | --- | --- | --- |
| Hong Kong Disneyland Disney Run / Magic Run Festa | https://experiences.myrealtrip.com/products/6056951 | Yes | Full public product page found after inspecting MyRealTrip public HTML; event dates, race types, age rules, and refund warning are visible. | Good, but closely overlaps the prior Hong Kong Disney teaser E2E. | Excluded to avoid repeating the same campaign/theme. |
| Universal Studios Japan smart combo | https://experiences.myrealtrip.com/products/6083103 | Yes | Full product detail page; visible product title, city, rating 4.8, review count 8,501, price schema KRW 93,000, inclusions/exclusions, booking FAQ, refund rule, QR usage, and official USJ links. | Best fit because it is a complete detail page and produces a non-hold operator QA result. | Selected. |
| Universal Studios Japan 1-day ticket | https://www.myrealtrip.com/offers/50211 | Yes | Full product detail page; rating/review count, inclusions/exclusions, refund rule, and related ticket information are visible. | Good, but simpler than the smart combo and less useful for testing promo/benefit clarity. | Excluded in favor of the smart combo. |

Complete detail-page judgment: the selected URL is a public product detail page, not a category page or campaign teaser. It includes product schema, page sections, public copy, price data, review aggregate data, and product-specific booking/refund information.

## Public Source URLs

- https://experiences.myrealtrip.com/products/6083103
- https://www.myrealtrip.com/offers/179375
- https://www.myrealtrip.com/offers/50211
- https://auth.myrealtrip.com/terms/common/cancel
- https://www.usj.co.jp/web/ko/kr/enjoy/numbered-ticket
- https://www.usj.co.jp/web/ko/kr/park-guide/schedule/attraction-closure#202405
- https://www.usj.co.jp/kr/rules/

## Public Evidence Collected

- MyRealTrip public HTML exposed the selected product as a full detail page, including product title, destination, page sections, review aggregate, price schema, and availability schema.
- The selected product page describes a smart combo containing a Universal Studios Japan 1-day pass and MyRealTrip 10,000 point benefit.
- The page says booking is confirmed immediately after payment and the ticket is available in the MyRealTrip app reservation history.
- The page says the ticket is valid only for the selected date and available visit dates are up to two months from purchase.
- The page separates included and excluded items: USJ 1-day pass is included; Express Pass, some seasonal attractions, and Super Nintendo World area entry guarantee are excluded.
- The page states cancellation/refund is unavailable after reservation confirmation and that product-specific refund rules apply.
- The page provides official USJ links for numbered-ticket guidance, attraction closures, and rules/manners.
- The static public text checked here did not expose an exact postal address/map block, exact date-by-date park hours, final checkout option-price variation, or recent review recency/rating distribution.

## Findings JSON

```json
{
  "candidate": "[1일권] 유니버설 스튜디오 재팬 스마트 콤보(마이리얼트립 포인트 10,000P 증정)",
  "city": "Osaka, Japan",
  "product_url": "https://experiences.myrealtrip.com/products/6083103",
  "findings": {
    "product_information_completeness": {
      "confidence": 0.85,
      "positive": [
        "The public MyRealTrip product page exposes a full product title, destination, product type, rating, review count, and product sections such as usage, inclusions/exclusions, operating time, place, refund policy, and reviews",
        "The listing states the product combines a Universal Studios Japan 1-day studio pass with MyRealTrip 10,000 points",
        "The listing states the included item is a Universal Studios Japan 1-day pass",
        "The listing states exclusions: Express Pass, some seasonal attractions, and Super Nintendo World area entry guarantee",
        "The listing states the product is for age 12+ adult tickets and points customers to a child/senior ticket URL"
      ],
      "missing": [],
      "unclear": [],
      "negative": [],
      "sources": [
        "https://experiences.myrealtrip.com/products/6083103",
        "https://www.myrealtrip.com/offers/50211"
      ]
    },
    "booking_condition_clarity": {
      "confidence": 0.82,
      "positive": [
        "The listing marks the product as instant confirmation",
        "The FAQ says booking is confirmed immediately after payment and the ticket can be found in MyRealTrip app reservation history",
        "The listing says the ticket is valid only for the selected date",
        "The listing says available visit dates are within up to two months from purchase",
        "The listing says point codes are sent by Kakao notification and can be registered manually"
      ],
      "missing": [],
      "unclear": [
        "Static public text did not expose exact date-by-date park opening hours, and the listing points customers to official USJ pages for detailed schedules"
      ],
      "negative": [],
      "sources": [
        "https://experiences.myrealtrip.com/products/6083103",
        "https://www.usj.co.jp/web/ko/kr/enjoy/numbered-ticket",
        "https://www.usj.co.jp/web/ko/kr/park-guide/schedule/attraction-closure#202405"
      ]
    },
    "cancellation_refund_clarity": {
      "confidence": 0.86,
      "positive": [
        "The listing has a visible cancellation/refund section",
        "The listing states cancellation and refund are unavailable after reservation confirmation",
        "The listing says a product-specific cancellation/refund rule applies because of product characteristics",
        "MyRealTrip exposes a public common cancellation/refund policy page"
      ],
      "missing": [],
      "unclear": [],
      "negative": [],
      "sources": [
        "https://experiences.myrealtrip.com/products/6083103",
        "https://auth.myrealtrip.com/terms/common/cancel"
      ]
    },
    "price_cost_transparency": {
      "confidence": 0.75,
      "positive": [
        "The product schema exposes priceCurrency KRW and price 93000",
        "The listing says each purchased ticket grants 10,000 MyRealTrip points and states the point validity is 30 days from issuance",
        "The listing separates included and excluded items, including the 1-day pass and excluded Express/Super Nintendo World guarantee items",
        "The listing shows payment benefit information separately from the product description"
      ],
      "missing": [],
      "unclear": [
        "Static public HTML did not confirm whether final option price varies by selected visit date, ticket type, or inventory at checkout"
      ],
      "negative": [],
      "sources": [
        "https://experiences.myrealtrip.com/products/6083103"
      ]
    },
    "route_meeting_point_risk": {
      "confidence": 0.7,
      "positive": [
        "The product is a fixed-venue ticket for Universal Studios Japan rather than a pickup tour",
        "The listing says e-ticket QR code can be scanned directly at the facility gate on the visit day",
        "The listing says printed or mobile presentation is accepted",
        "The listing links to USJ official rules and attraction closure information"
      ],
      "missing": [
        "exact postal address or map link in the checked public text"
      ],
      "unclear": [
        "The extracted public text says location information is in the product detail page, but the static text checked here did not expose a clear address block"
      ],
      "negative": [],
      "sources": [
        "https://experiences.myrealtrip.com/products/6083103",
        "https://www.usj.co.jp/kr/rules/",
        "https://www.usj.co.jp/web/ko/kr/park-guide/schedule/attraction-closure#202405"
      ]
    },
    "review_cs_risk": {
      "confidence": 0.8,
      "positive": [
        "The public product page exposes rating 4.8 and 8,501 reviews",
        "The page exposes many review-photo markers, indicating active customer review content exists publicly",
        "The listing says MyRealTrip is a Korean official partner of Universal Studios Japan",
        "The FAQ addresses QR registration failure and tells users they can use the ticket directly on site without app registration"
      ],
      "missing": [
        "recent review recency and rating distribution"
      ],
      "unclear": [],
      "negative": [],
      "sources": [
        "https://experiences.myrealtrip.com/products/6083103"
      ]
    }
  }
}
```

## score.py Raw Output

```json
{
  "axis_scores": {
    "booking_condition_clarity": 90,
    "cancellation_refund_clarity": 91,
    "price_cost_transparency": 82,
    "product_information_completeness": 98,
    "review_cs_risk": 78,
    "route_meeting_point_risk": 69
  },
  "candidate": "[1일권] 유니버설 스튜디오 재팬 스마트 콤보(마이리얼트립 포인트 10,000P 증정)",
  "city": "Osaka, Japan",
  "missing_information": [
    "booking_condition_clarity: Static public text did not expose exact date-by-date park opening hours, and the listing points customers to official USJ pages for detailed schedules",
    "price_cost_transparency: Static public HTML did not confirm whether final option price varies by selected visit date, ticket type, or inventory at checkout",
    "route_meeting_point_risk: exact postal address or map link in the checked public text",
    "route_meeting_point_risk: The extracted public text says location information is in the product detail page, but the static text checked here did not expose a clear address block",
    "review_cs_risk: recent review recency and rating distribution"
  ],
  "overall_score": 85,
  "partner_questions": [
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: Static public text did not expose exact date-by-date park opening hours, and the listing points customers to official USJ pages for detailed schedules",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: Static public HTML did not confirm whether final option price varies by selected visit date, ticket type, or inventory at checkout",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: exact postal address or map link in the checked public text",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: The extracted public text says location information is in the product detail page, but the static text checked here did not expose a clear address block",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: recent review recency and rating distribution"
  ],
  "risk_flags": [
    "booking_condition_clarity:unclear_information",
    "price_cost_transparency:unclear_information",
    "route_meeting_point_risk:missing_required_information",
    "route_meeting_point_risk:unclear_information",
    "review_cs_risk:missing_required_information"
  ],
  "verdict": "보완 후 게시",
  "verdict_drivers": [
    "booking_condition_clarity: unclear information - Static public text did not expose exact date-by-date park opening hours, and the listing points customers to official USJ pages for detailed schedules",
    "price_cost_transparency: unclear information - Static public HTML did not confirm whether final option price varies by selected visit date, ticket type, or inventory at checkout",
    "route_meeting_point_risk: missing information - exact postal address or map link in the checked public text",
    "route_meeting_point_risk: unclear information - The extracted public text says location information is in the product detail page, but the static text checked here did not expose a clear address block",
    "review_cs_risk: missing information - recent review recency and rating distribution",
    "verdict: 5 missing/unclear item(s) need completion"
  ]
}
```

## Final Operator QA Report

- Final verdict: 보완 후 게시
- Overall score: 85
- Operator judgment: this is a usable public product detail page and does not need a publishing hold, but it still needs small content QA fixes before being treated as fully complete.
- Product information completeness: strong. The page exposes product identity, region, product type, included 1-day pass, excluded Express/Super Nintendo World guarantee items, adult-ticket basis, and child/senior alternative URL.
- Booking condition clarity: strong but not perfect. Instant confirmation, app ticket location, selected-date validity, purchase-date window, and point-code flow are visible. Exact date-by-date opening hours should be made easier to reach.
- Cancellation/refund clarity: strong. The page states confirmation-after refund/cancellation unavailability and references product-specific refund rules; MyRealTrip also has a public refund policy URL.
- Price/cost transparency: good. Public schema exposes KRW 93,000 and the page explains 10,000 points, validity, and included/excluded items. Option/date price variation should be clarified if it changes at checkout.
- Route/meeting point risk: moderate. This is a fixed-venue QR ticket, but exact address/map guidance was not visible in the checked static text.
- Review/CS risk: good. Rating 4.8 and 8,501 reviews are visible, and the QR FAQ reduces likely CS confusion. Review recency and distribution remain unverified.

## Partner Follow-up Questions

- 날짜별 파크 운영시간 확인 경로를 상세페이지에 더 직접적으로 연결하거나, "방문 전 공식 운영시간을 확인해 주세요" 문구를 넣을 수 있나요?
- 선택 날짜, 권종, 재고에 따라 최종 결제 가격이 달라지는지 확인하고 상세페이지에 안내할 수 있나요?
- 유니버설 스튜디오 재팬의 정확한 주소 또는 지도 링크를 이용장소 영역에 노출할 수 있나요?
- 리뷰 최신성, 최근 불만 키워드, 평점 분포를 운영자가 확인할 수 있나요?
- QR 등록 실패 시 바로 현장 사용 가능하다는 FAQ를 구매 전 필수확인사항에도 짧게 반복할 수 있나요?

## Suggested Listing Copy / Page Edits

```text
방문 전 확인
- 본 티켓은 선택한 날짜에만 사용할 수 있습니다.
- 유니버설 스튜디오 재팬 운영시간과 어트랙션 운휴 정보는 방문 전 공식 홈페이지에서 확인해 주세요.

포함/불포함
- 포함: 유니버설 스튜디오 재팬 1일 입장권, 마이리얼트립 10,000P 혜택
- 불포함: 익스프레스 패스, 슈퍼 닌텐도 월드 에어리어 입장 확약권, 일부 시즌 한정 어트랙션

이용 장소
- 이용 장소: 유니버설 스튜디오 재팬
- 주소/지도: [정확한 주소와 지도 링크 입력 필요]
- 입장 방법: 이용 당일 e티켓의 QR코드를 시설 입구에서 제시해 주세요. 모바일 또는 출력본 제시가 가능합니다.

취소/환불
- 본 상품은 예약 확정 후 취소 및 환불이 불가합니다. 구매 전 방문일과 권종을 반드시 확인해 주세요.

포인트 혜택
- 구매 1장당 마이리얼트립 10,000P가 지급됩니다.
- 포인트 유효기간은 발급일로부터 30일입니다.
- 포인트 코드는 카카오 알림톡으로 발송되며 직접 등록 후 사용할 수 있습니다.
```

## Unverified Items

- Exact postal address or map link in the checked public static text: 확인 불가
- Exact date-by-date park operating hours on the MyRealTrip page itself: 확인 불가
- Whether final option price changes by selected visit date, ticket type, or inventory at checkout: 확인 불가
- Recent review recency and rating distribution beyond aggregate 4.8 / 8,501 reviews: 확인 불가
- Whether all dynamic in-page tabs expose more location detail after client-side interaction: 확인 불가

## What This Test Verified

- The plugin can audit a genuine public MyRealTrip product detail page, not only a campaign teaser.
- The six-axis QA rubric can produce a useful non-hold verdict (`보완 후 게시`) when most listing information is present.
- `score.py` surfaces narrow content gaps through `missing_information`, `risk_flags`, `verdict_drivers`, and Korean default `partner_questions`.
- Public schema and visible page copy can be converted into deterministic findings without using internal APIs, login-only data, or paid APIs.

## Limitations

- This run used public HTML/text extraction and public URLs only.
- No login-only checkout flow, internal MyRealTrip admin data, private API, paid API, or secret data was used.
- Dynamic UI content may expose additional address or option details that were not visible in the checked static public text.
- Product review details were not deeply sampled; only aggregate rating/review count and visible review-photo markers were used.
