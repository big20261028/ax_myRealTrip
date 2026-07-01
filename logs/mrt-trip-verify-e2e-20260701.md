# mrt-trip-verify E2E log - 2026-07-01

## Target

- Candidate: 지베르니+베르사유+고흐마을 투어
- City: Paris
- Product source: https://www.myrealtrip.com/
- Rule: public web sources only

## Public evidence used

- MyRealTrip public homepage: product name, visible rank, price, support, business/footer notices.
- MyRealTrip experiences page: public tour-ticket category and support footer.
- MyRealTrip cancellation policy URL: public policy endpoint.
- Palace of Versailles public reference page.
- Auvers-sur-Oise public reference page.
- Fondation Monet in Giverny public reference page.
- Le Monde public reporting on Giverny crowding/overtourism.

## Findings JSON

```json
{
  "candidate": "지베르니+베르사유+고흐마을 투어",
  "city": "Paris",
  "findings": {
    "review_reliability": {
      "confidence": 0.35,
      "positive": [
        "MyRealTrip public homepage lists this as a Paris tour product and ranks it #2 in the visible Paris section"
      ],
      "negative": [],
      "sources": [
        "https://www.myrealtrip.com/"
      ]
    },
    "price_fairness": {
      "confidence": 0.75,
      "positive": [
        "MyRealTrip lists this product at 98,100 KRW after 10% discount",
        "same public Paris section lists similar guided day-tour products at 132,050 KRW and 143,100 KRW, so the price is discounted but not obviously implausible",
        "same page labels broader Paris tour-ticket area as promotion-heavy, making a visible discount plausible"
      ],
      "negative": [],
      "sources": [
        "https://www.myrealtrip.com/",
        "https://www.myrealtrip.com/main/experiences"
      ]
    },
    "location_routing": {
      "confidence": 0.45,
      "positive": [
        "The product is a bundled bus-style day-tour candidate from the Paris area, which fits dispersed destinations better than self-transfer",
        "Versailles is a major destination west of Paris and Auvers-sur-Oise is northwest of Paris; both are plausible day-trip stops"
      ],
      "negative": [],
      "sources": [
        "https://www.myrealtrip.com/",
        "https://en.wikipedia.org/wiki/Palace_of_Versailles",
        "https://en.wikipedia.org/wiki/Auvers-sur-Oise"
      ]
    },
    "operator_reliability": {
      "confidence": 0.75,
      "positive": [
        "MyRealTrip public page lists 24/7 chat support and phone support 09:00-18:00",
        "MyRealTrip footer publishes cancellation/refund policy link and company/tourism registration information",
        "The platform states it has tourism association guarantee insurance"
      ],
      "negative": [
        "MyRealTrip states it is an intermediary and not the direct transaction party, so final operator-specific reliability still needs the product detail page"
      ],
      "sources": [
        "https://www.myrealtrip.com/",
        "https://auth.myrealtrip.com/terms/common/cancel"
      ]
    },
    "traps_risks": {
      "confidence": 0.45,
      "positive": [
        "No public evidence found in the checked pages of forced shopping, no-show, or bait listing language for this exact visible product",
        "The price is visible before login on the public MyRealTrip page"
      ],
      "negative": [],
      "sources": [
        "https://www.myrealtrip.com/"
      ]
    },
    "context": {
      "confidence": 0.65,
      "positive": [
        "Fondation Monet/Giverny is a seasonal visitor site commonly open April to November, matching summer travel better than winter travel",
        "Versailles and Auvers-sur-Oise are established public tourist destinations"
      ],
      "negative": [
        "Recent public reporting describes Giverny overtourism and crowd pressure, so high-season crowding and exact operating dates should be checked"
      ],
      "sources": [
        "https://en.wikipedia.org/wiki/Fondation_Monet_in_Giverny",
        "https://www.lemonde.fr/en/economy/article/2025/09/21/giverny-s-thriving-business-around-monet-s-gardens-risks-oversaturation_6745602_19.html",
        "https://en.wikipedia.org/wiki/Palace_of_Versailles",
        "https://en.wikipedia.org/wiki/Auvers-sur-Oise"
      ]
    }
  }
}
```

## score.py output

```json
{
  "axis_scores": {
    "context": 56,
    "location_routing": 70,
    "operator_reliability": 68,
    "price_fairness": 82,
    "review_reliability": 58,
    "traps_risks": 70
  },
  "candidate": "지베르니+베르사유+고흐마을 투어",
  "city": "Paris",
  "overall_score": 67,
  "risk_flags": [
    "review_reliability:low_confidence",
    "operator_reliability:negative_signal",
    "context:negative_signal"
  ],
  "verdict": "확인 후 예약",
  "verdict_drivers": [
    "review_reliability: low confidence 0.35",
    "operator_reliability: negative evidence - MyRealTrip states it is an intermediary and not the direct transaction party, so final operator-specific reliability still needs the product detail page",
    "context: negative evidence - Recent public reporting describes Giverny overtourism and crowd pressure, so high-season crowding and exact operating dates should be checked",
    "verdict: score 67 < 70",
    "verdict: 1 uncertainty signal(s) need checking",
    "verdict: 2 non-critical negative signal(s) need checking"
  ]
}
```

## Decision card

- Verdict: 확인 후 예약
- Overall score: 67
- Risk flags:
  - review_reliability:low_confidence
  - operator_reliability:negative_signal
  - context:negative_signal
- Remaining uncertainty:
  - Exact review count, recency, and rating distribution for this product were not exposed in the checked public static page.
  - Exact meeting point, start/end time, stop duration, included entrance fees, and guide language should be confirmed on the product detail/checkout page before booking.
- 그래서 지금 예약해도 되는 이유:
  - 공개 가격과 플랫폼 운영 신호는 양호하지만, 리뷰·상세 일정·현지 혼잡 리스크 확인이 남아 있어 결제 전 확인이 필요하다.
