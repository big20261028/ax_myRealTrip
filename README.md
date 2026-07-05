# MRT Listing Quality Auditor

## 개요

`mrt-listing-quality-auditor`는 마이리얼트립 투어·액티비티 상품 상세페이지를 공개 자료 기반으로 감사하는 Codex 플러그인입니다.

상품 상세페이지와 공개 정책, 공식 관광지·행사·시설 안내를 근거로 6개 기준의 축별 점수와 종합 판정, 판단 근거, 부족 항목, 파트너 보완 질문, 상세페이지 수정 제안을 생성합니다.

이 플러그인은 고객에게 여행상품을 추천하거나 예약 결정을 대신하는 도구가 아닙니다. 상품 운영자와 콘텐츠 QA 담당자가 게시 전 또는 개선 전 상세페이지의 정보 완결성을 점검하기 위한 운영자용 QA 도구입니다.

## 해결하려는 문제

마이리얼트립의 투어·액티비티 상품 상세페이지는 예약 전 고객이 구매 판단을 내릴 때 보는 정보 묶음입니다. 상품명과 가격뿐 아니라 포함/불포함, 이용안내, 필수확인사항, 취소·환불, 후기, 외부 공식 안내처럼 서로 다른 정보가 함께 들어갑니다.

신규 상품을 게시하거나 기존 상품을 개선할 때 운영자는 고객이 이 설명만 보고 예약 조건을 오해하지 않을지, 파트너에게 어떤 정보를 더 받아야 할지 확인해야 합니다. 포함/불포함, 이용안내, 취소·환불, 운영시간, 위치, 추가 비용, 이용 제한 조건이 불명확하면 상세페이지 보완 항목이 남습니다.

이 플러그인은 상품을 추천하는 것이 아니라, 게시 전 상품 상세페이지가 예약 판단에 필요한 정보를 충분히 갖췄는지 6축 기준으로 일관되게 검증하는 운영 QA 문제를 해결합니다.

## 사용자

- 상품 운영자
- 파트너 온보딩 담당자
- 콘텐츠 QA 담당자
- 고객지원/운영 담당자

## 사용 상황

- 신규 투어·액티비티 상품 게시 전
- 기존 상품 상세페이지 개선 전
- 파트너에게 보완 요청을 보내기 전
- 상품 상세페이지의 포함/불포함, 취소·환불, 운영시간, 위치, 추가 비용, 이용 제한 조건이 충분한지 점검할 때

## 공개 자료 기반 원칙

- 공개 상품 페이지, 공개 정책 페이지, 공식 관광지·행사·시설 페이지 등 공개 자료만 사용합니다.
- 내부 API, 로그인 필요 데이터, 비공개 자료, 유료 API, 고객 개인정보는 사용하지 않습니다.
- 공개 자료로 확인되지 않는 내용은 `확인 불가`로 표시합니다.
- 출처 URL이 없는 사실은 단정하지 않습니다.
- 공개 자료로 확인한 사실과 synthetic sample 또는 테스트용 예시는 구분합니다.

E2E 검증에서 사용한 공개 URL 예시는 다음과 같습니다.

- https://www.myrealtrip.com/
- https://www.myrealtrip.com/main/experiences
- https://experiences.myrealtrip.com/products/6083103
- https://auth.myrealtrip.com/terms/common/cancel
- https://www.usj.co.jp/web/ko/kr/enjoy/numbered-ticket
- https://www.usj.co.jp/web/ko/kr/park-guide/schedule/attraction-closure#202405
- https://www.usj.co.jp/kr/rules/

## 작동 방식

1. 사용자가 마이리얼트립 상품명 또는 공개 URL을 제공합니다.
2. Codex가 공개 상품 페이지, 공개 정책, 공식 시설·행사 안내, 공개 후기 등 확인 가능한 자료를 조사합니다.
3. 6축 기준으로 findings JSON을 작성합니다.
4. `src/skills/audit-listing/scripts/score.py`가 같은 입력에 대해 항상 같은 점수와 판정을 계산합니다.
5. 축별 점수, 종합 점수, 최종 판정, 판정 근거, 부족 항목, 파트너 보완 질문, 상세페이지 수정 제안을 출력합니다.

## 일반 Codex 질문과의 차이

- 자유로운 여행 추천이 아니라 고정된 QA 기준을 사용합니다.
- `score.py`를 통해 결정론적 점수와 판정을 생성합니다.
- 공개 출처 URL 기반으로 근거를 표시합니다.
- 부족한 정보는 추측하지 않고 missing information으로 분리합니다.
- 파트너에게 물어볼 질문을 자동 생성합니다.
- 최종 출력은 고객용 추천 카드가 아니라 운영자용 QA 리포트입니다.

## 6축 감사 기준

축 이름은 `score.py`와 동일하게 유지합니다.

1. `product_information_completeness`: 상품명, 대상 지역, 기본 구성, 이용 가능 범위 등 상품 정보가 충분한지 확인합니다.
2. `booking_condition_clarity`: 예약 확정 방식, 이용일, 인원, 옵션, 이용 제한 조건이 명확한지 확인합니다.
3. `cancellation_refund_clarity`: 취소·환불 조건, 환불 불가 시점, 예외 조건이 명확한지 확인합니다.
4. `price_cost_transparency`: 가격, 포함/불포함, 현장 추가 비용, 옵션별 가격 차이가 투명한지 확인합니다.
5. `route_meeting_point_risk`: 집합 장소, 주소, 지도, 이동 동선, 운영시간 확인 방법이 충분한지 확인합니다.
6. `review_cs_risk`: 공개 후기나 공개 정보에서 고객 문의로 이어질 수 있는 불명확성이 있는지 확인합니다.

## 판정 기준

`score.py`는 축별 관측치와 신뢰도, 출처 URL, 누락·불명확·부정 신호를 기반으로 점수를 계산합니다.

- `승인 가능`: 핵심 정보가 충분하고 공개 출처가 확인되며 의미 있는 누락·불명확·위험 신호가 없습니다.
- `보완 후 게시`: 게시 자체를 막을 정도는 아니지만 누락 정보, 불명확한 조건, 출처 보완, 파트너 확인 질문이 필요합니다.
- `게시 보류`: critical signal, negative signal 다수, 또는 핵심 정보 다수 누락으로 고객이 예약 조건을 오해할 가능성이 큽니다.

## 출력 결과

플러그인은 운영자용 QA 리포트에 다음 항목을 포함하도록 설계되어 있습니다.

- 축별 점수
- 종합 점수
- 최종 판정
- 판정 근거
- 위험 플래그
- 부족하거나 불명확한 항목
- 공개 출처 URL
- 파트너 보완 질문
- 상세페이지 수정 제안

`score.py`의 JSON 출력에는 다음 필드가 포함됩니다.

```json
{
  "axis_scores": {},
  "overall_score": 85,
  "risk_flags": [],
  "verdict": "보완 후 게시",
  "verdict_drivers": [],
  "missing_information": [],
  "partner_questions": []
}
```

## 예시 사용 흐름

마이리얼트립 공개 상품 `[1일권] 유니버설 스튜디오 재팬 스마트 콤보`를 감사한 E2E 예시가 `logs/mrt-listing-quality-audit-e2e-product-detail-20260704.md`에 있습니다.

공개 상세페이지, 마이리얼트립 환불 정책, USJ 공식 안내를 근거로 감사한 결과 종합 85점, `보완 후 게시`가 나왔습니다. 상품명, 가격, QR 입장, 즉시확정, 포함/불포함, 환불 불가 고지는 확인됐지만, 주소와 지도 정보의 충분성, 날짜별 운영시간, 옵션별 최종 가격 변동, 후기 정보의 최신성·분포 확인은 보완 항목으로 남았습니다.

Codex에서 사용할 때는 다음처럼 요청할 수 있습니다.

```text
@audit-listing 마이리얼트립 공개 투어 상품 하나를 운영자 관점에서 QA하고, 보완 후 게시가 필요한 항목과 파트너 질문을 정리해줘.
```

## 설치 방법

저장소 로컬 마켓플레이스는 `.agents/plugins/marketplace.json`에 설정되어 있습니다.

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

Codex CLI에서 설치합니다.

```powershell
codex plugin marketplace add C:\Users\traz1\Desktop\AX_hackathon\AX_myrealtrip
codex plugin add mrt-listing-quality-auditor@ax-myrealtrip-local
```

설치 후 새 Codex 스레드에서 `@audit-listing` 또는 `mrt-listing-quality-auditor:audit-listing` 스킬을 호출합니다.

## 테스트 방법

기본 테스트 명령은 다음과 같습니다.

```powershell
python -m py_compile .\src\skills\audit-listing\scripts\score.py
python .\src\skills\audit-listing\scripts\score.py --self-test
Get-Content .\examples\listing-findings.json | python .\src\skills\audit-listing\scripts\score.py
```

현재 환경에서 `python`이 PATH에 없다면 Codex bundled Python을 사용할 수 있습니다.

```powershell
C:\Users\traz1\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -m py_compile .\src\skills\audit-listing\scripts\score.py
C:\Users\traz1\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe .\src\skills\audit-listing\scripts\score.py --self-test
C:\Users\traz1\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe .\src\skills\audit-listing\scripts\score.py .\examples\listing-findings.json
```

## 제출 ZIP 구성

제출 ZIP에는 최소한 다음 항목을 포함합니다.

```text
src/
README.md
logs/
examples/
.agents/plugins/marketplace.json
```

선택 항목입니다.

```text
research/  # 실제 폴더가 있을 때만
```

다음 항목은 제출 ZIP에서 제외합니다.

```text
.git/
.codex/
__pycache__/
*.pyc
.venv/
node_modules/
cache/temp files
OS/editor temp files
submission.zip
```

중요 원칙은 다음과 같습니다.

- `logs/` 전체 원본은 포함해야 합니다.
- `logs/codex/*.jsonl` 원본 로그를 제외하면 안 됩니다.
- 기존 로그를 수정·삭제·요약하지 않습니다.
- 기존 `submission.zip`을 새 zip 내부에 중첩 포함하지 않습니다.

## 한계

- 공개 자료 기반 감사이므로 내부 운영 기준, 실제 고객 문의 데이터, 비공개 파트너 계약 조건은 확인할 수 없습니다.
- 공개 상세페이지와 외부 공식 자료에 없는 정보는 `확인 불가`로 표시합니다.
- 최종 법무·정책·운영 판단을 대신하지 않습니다.
- 고객에게 특정 상품을 추천하거나 예약 결정을 대신하지 않습니다.
