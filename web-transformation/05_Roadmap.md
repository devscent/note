# MARS Web 전환 - 1년 Roadmap (안)

## 1. 주요 Gate

| Gate | 목표 시점 | 완료 기준 |
|---|---|---|
| G1. Scope / Architecture Baseline | Month 2 | Feature Inventory, 공통 요구사항, Target Architecture 초안 확정 |
| G2. Foundation / Pilot 검증 | Month 4 | 공통 기반과 대표 기능의 End-to-End 동작 검증 |
| G3. 주요 기능 Migration 완료 | Month 10 | Web 전환 대상 기능 개발 및 주요 데이터 검증 완료 |
| G4. Service Transition 완료 | Month 12 | 사용자 검증, 병행 운영, Web 정식 전환 및 기존 WPF 서비스 종료 |

---

## 2. 월별 Roadmap

| Workstream | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 현행 기능 / Backend / DB 분석 | ● | ● |  |  |  |  |  |  |  |  |  |  |
| Product / Operation Requirement | ● | ● |  |  |  |  |  |  |  |  |  |  |
| Target Architecture | ● | ● | ● |  |  |  |  |  |  |  |  |  |
| 공통 Foundation 구축 |  | ● | ● | ● |  |  |  |  |  |  |  |  |
| Pilot 개발 / 검증 |  |  | ● | ● |  |  |  |  |  |  |  |  |
| Pilot Review / Migration 상세계획 |  |  |  | ● | ● |  |  |  |  |  |  |  |
| Migration Wave 1 |  |  |  |  | ● | ● |  |  |  |  |  |  |
| Migration Wave 2 |  |  |  |  |  | ● | ● |  |  |  |  |  |
| Migration Wave 3 |  |  |  |  |  |  | ● | ● | ● |  |  |  |
| Migration Wave 4 / 잔여 기능 |  |  |  |  |  |  |  | ● | ● | ● |  |  |
| 기능 / 데이터 Validation |  |  | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |
| 성능 / 보안 / 운영 검증 |  |  |  | ● | ● |  |  | ● | ● | ● | ● |  |
| UAT / 사용자 Feedback |  |  |  |  |  |  |  |  | ● | ● | ● |  |
| WPF + Web 병행 운영 |  |  |  |  |  |  |  |  |  | ● | ● | ● |
| Web 정식 전환 / WPF 종료 |  |  |  |  |  |  |  |  |  |  |  | ● |
| Improvement Backlog 관리 | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |

---

## 3. 단계별 일정

### Month 1–2
- 현행 분석
- Feature Inventory
- Product / Operation Requirement
- Scope 정의
- Target Architecture 초안

### Month 2–4
- 공통 Foundation
- SSO / 권한
- Logging / Trace
- 공통 UI
- Pilot 개발 및 검증

### Month 5–10
- 기능별 Migration
- Wave 단위 개발
- WPF-Web Data Validation 병행
- 공통 Foundation 보완

### Month 8–11
- 통합 Test
- 성능 / 보안 검증
- UAT
- 운영 준비

### Month 10–12
- WPF / Web 병행 운영
- 사용자 Feedback 반영
- Web 공식 전환
- WPF 서비스 종료

---

## 4. 상세 일정 확정 원칙

```text
현행 Inventory
   ↓
기능별 난이도 / 전환 범위 평가
   ↓
Pilot
   ↓
실제 생산성 확인
   ↓
메뉴별 공수 재산정
   ↓
Migration Wave 상세 일정 확정
```

20개 기능을 동일 크기로 보고 `메뉴 수 × 일정`으로 계산하지 않는다.

전체 1년 Roadmap은 월 단위로 유지하고:

- 다음 2~3개월: 기능 / Wave 단위
- 현재 개발 구간: 주 단위

로 상세화한다.
