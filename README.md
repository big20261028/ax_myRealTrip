# AX_myrealtrip

## mrt-listing-quality-auditor

`mrt-listing-quality-auditor` is a Codex plugin for MyRealTrip listing operations, not a general traveler recommendation tool. It helps product operators, partner onboarding managers, content QA reviewers, and CS/operations teams audit public tour and activity listing pages before publishing or improving them.

The plugin uses public evidence to find missing information, unclear booking conditions, likely CS triggers, conversion blockers, and partner follow-up questions. It then produces an operator QA report and suggested listing copy.

## Problem

Tour and activity listings often lose bookings or create repeated CS questions because key details are missing or unclear: meeting point, duration, rain policy, minimum departure count, entrance-fee inclusion, cancellation terms, route risk, or crowding risk. These checks are repetitive, evidence-driven, and need a consistent rubric.

## Public Evidence

This plugin is designed around public evidence, not internal MyRealTrip data. MyRealTrip operates public tour, ticket, and activity pages, and visible listing details can affect customer booking decisions. Public policy pages such as the MyRealTrip cancellation/refund policy can be used to check whether a product page clearly connects customers to refund rules.

External event or venue pages can also expose operating dates, access constraints, transport guidance, crowding, safety notes, and other details that tour/activity listings should reflect. Public articles or reviews may be used as supporting signals for CS risk such as crowding, waiting, accessibility issues, refund complaints, or unclear operations.

Example public sources used in E2E checks:

- https://www.myrealtrip.com/
- https://www.myrealtrip.com/main/experiences
- https://auth.myrealtrip.com/terms/common/cancel
- https://www.vividsydney.com/
- https://www.vividsydney.com/visit/access-and-inclusion
- https://www.theguardian.com/culture/article/2024/jun/10/vivid-festival-sydney-crowd-crush-fears-nsw-premier-chris-minns
- https://www.hongkongdisneyland.com/calendars/day/
- https://www.hongkongdisneyland.com/guest-services/guests-with-disabilities/
- https://en.wikipedia.org/wiki/Hong_Kong_Disneyland

## Users

- Product operators
- Partner onboarding managers
- Content QA reviewers
- CS/operations teams

## When To Use

- Before publishing a new tour or activity listing.
- When improving an existing listing page.
- When a product repeatedly causes CS questions.
- Before sending a completion request to a partner.

## How It Works

1. Collect public evidence from product pages, policy pages, venue pages, public reviews, or comparable public listings.
2. Audit six QA axes:
   - `product_information_completeness`
   - `booking_condition_clarity`
   - `cancellation_refund_clarity`
   - `price_cost_transparency`
   - `route_meeting_point_risk`
   - `review_cs_risk`
3. Run `src/skills/audit-listing/scripts/score.py`.
4. Produce a QA report with verdict, scores, missing information, risk drivers, partner questions, and listing copy suggestions.

## Difference From A Generic Codex Question

- Fixed QA rubric instead of free-form advice.
- Deterministic score and verdict from `score.py`.
- Public source URLs required for evidence.
- Missing evidence is marked as uncertainty instead of invented.
- Partner follow-up questions are generated from missing or unclear fields.
- Output is an operator QA report, not a customer booking card.

## Verdicts

- `승인 가능`: enough required information, source-backed evidence, and no meaningful risk.
- `보완 후 게시`: listing needs completion or clarification before publishing.
- `게시 보류`: critical negative signals or too many required details are missing.

## Install

The repo-local marketplace is configured at `.agents/plugins/marketplace.json`:

```json
{
  "name": "ax-myrealtrip-local",
  "plugins": [
    {
      "name": "mrt-listing-quality-auditor",
      "source": {
        "source": "local",
        "path": "./src"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Travel"
    }
  ]
}
```

Install with Codex CLI:

```powershell
codex plugin marketplace add C:\Users\traz1\Desktop\AX_hackathon\AX_myrealtrip
codex plugin add mrt-listing-quality-auditor@ax-myrealtrip-local
```

Start a new Codex thread after installing, then trigger:

```text
@audit-listing 마이리얼트립 공개 투어 상품 하나를 운영자 관점에서 QA하고, 보완 후 게시가 필요한 항목과 파트너 질문을 정리해줘.
```

## Test

Use the bundled Python runtime or any Python 3.12+:

```powershell
python -m py_compile .\src\skills\audit-listing\scripts\score.py
python .\src\skills\audit-listing\scripts\score.py --self-test
Get-Content .\examples\listing-findings.json | python .\src\skills\audit-listing\scripts\score.py
```

## Example Output

```json
{
  "axis_scores": {
    "booking_condition_clarity": 53,
    "cancellation_refund_clarity": 65,
    "price_cost_transparency": 54,
    "product_information_completeness": 62,
    "review_cs_risk": 41,
    "route_meeting_point_risk": 56
  },
  "overall_score": 55,
  "risk_flags": [
    "product_information_completeness:missing_required_information",
    "booking_condition_clarity:missing_required_information",
    "price_cost_transparency:missing_required_information",
    "route_meeting_point_risk:unclear_information",
    "review_cs_risk:negative_signal"
  ],
  "verdict": "보완 후 게시",
  "verdict_drivers": [
    "product_information_completeness: missing information - exact meeting point",
    "booking_condition_clarity: missing information - minimum departure count",
    "price_cost_transparency: missing information - entrance fee inclusion",
    "route_meeting_point_risk: unclear information - traffic delay handling",
    "review_cs_risk: negative signal - public reports mention crowding",
    "verdict: score 55 < 80"
  ],
  "missing_information": [
    "product_information_completeness: exact meeting point",
    "booking_condition_clarity: minimum departure count",
    "price_cost_transparency: entrance fee inclusion",
    "route_meeting_point_risk: traffic delay handling"
  ],
  "partner_questions": [
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: exact meeting point",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: minimum departure count",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: entrance fee inclusion",
    "다음 항목을 확인하고 상세페이지에 반영할 문구를 제공해 주세요: traffic delay handling"
  ]
}
```

## Submission ZIP

Include at minimum:

- `src/`
- `README.md`
- `logs/` as the full original log folder

Also include when useful:

- `examples/`
- `.agents/plugins/marketplace.json`

Do not exclude, edit, summarize, or delete original work logs. In particular, keep:

- `logs/codex/*.jsonl`
- pre-pivot conversation logs
- failed-attempt logs
- previous-direction reference logs
- original Codex conversation logs

You may exclude generated or local environment files:

- `.git/`
- `.codex/`
- `__pycache__/`
- `*.pyc`
- `.venv/`
- `node_modules/`
- cache/temp files
- OS/editor temp files
