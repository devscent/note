# MARS Web 전환 추진 계획

## 1. 추진 배경

MARS는 현재 Windows 기반 WPF Application으로 운영되고 있으며, 서버측 데이터 처리 기능은 EES의 DataService 환경에서 실행되고 있다.

향후 MARS의 사용자 환경을 Web 기반으로 전환하고, Frontend와 Backend API를 중심으로 하는 새로운 서비스 구조로 재구성한다.

본 과제의 1차 목적은 **기존 MARS의 업무 기능과 데이터 결과를 안정적으로 Web 환경으로 이전하는 것**이다. 동시에 장기간의 운영 경험에서 확인된 공통적인 운영·지원 문제를 개선할 수 있도록 Logging, Trace, 사용자 설정, 권한, 사용현황 수집 등 차세대 운영 기반을 함께 설계한다.

---

## 2. 추진 목표

### 2.1 Web 기반 MARS 구축
- 별도 Client 설치 없이 Browser를 통한 서비스 제공
- Web Frontend + MARS Backend API 구조 구축
- 기존 서버측 데이터 처리 기능을 신규 Backend 구조에 맞게 이전
- 자체 배포, 운영, 모니터링 체계 확보

### 2.2 기존 기능의 안정적 전환
- 기존 MARS 주요 기능의 Web 전환
- 기존 계산 Logic 및 데이터 결과의 정합성 확보
- 대용량 분석 기능의 성능 유지 또는 개선

### 2.3 기존 기능 유지 중심의 전환
이번 프로젝트는 **기능 개선 자체보다 Web 기술 전환을 우선**한다.

현행 기능은 다음 기준으로 분류하되, 기본값은 `유지`로 한다.

| 구분 | 기본 방향 |
|---|---|
| 유지 | 기존 기능과 업무 Logic을 유지하여 Web으로 이전 |
| 개선 | Web 전환에 꼭 필요한 범위만 반영, 나머지는 후속 Backlog |
| 통합 | 명확한 필요성이 있는 경우에만 검토 |
| 재설계 | 원칙적으로 후속 개선 과제로 분리 |
| 폐기 | 실제 사용량과 업무 필요성 확인 후 전환 제외 여부 판단 |

WPF와 Web의 기술적 차이로 인해 필요한 UI/Interaction 변경은 기능 PI가 아니라 **Web 환경 적응**으로 본다.

### 2.4 운영 가능한 시스템 구축
화면 기능뿐 아니라 다음을 함께 고려한다.

- 사용자 문제를 쉽게 추적할 수 있는가
- 데이터 결과의 생성 과정을 설명할 수 있는가
- 사용자가 문제 상황을 쉽게 전달할 수 있는가
- 실제 사용현황을 파악할 수 있는가
- 권한과 사용자 설정을 확장 가능하게 관리할 수 있는가

---

## 3. 추진 원칙

1. **메뉴 이관보다 공통 기반을 우선한다.**
2. **기존 기능 유지와 Scope 통제를 원칙으로 한다.**
3. **대표 기능 Pilot 이후 본격 Migration을 진행한다.**
4. **사용자 관점과 운영자 관점을 함께 설계한다.**
5. **기능 개발과 데이터 검증을 병행한다.**
6. **Web 안정화 후 기존 WPF 서비스를 종료한다.**

---

## 4. 전체 추진 단계

```text
Phase 1. 현행 분석
        │
        ▼
Phase 2. Product / Operation Requirement 정의
        │
        ▼
Phase 3. Target Architecture 및 공통 기반 설계
        │
        ▼
Phase 4. 공통 Foundation 구축
        │
        ▼
Phase 5. Pilot 개발 및 검증
        │
        ▼
Phase 6. 기능별 Migration
        │
        ▼
Phase 7. 통합 / 데이터 / 성능 / 사용자 검증
        │
        ▼
Phase 8. 병행 운영 및 Web 정식 전환
        │
        ▼
Phase 9. 기존 WPF 서비스 종료
```

---

## 5. 주요 산출물

| 영역 | 주요 산출물 |
|---|---|
| 현행 분석 | Feature Inventory / Backend·DB 분석 / 기존 VOC 분석 |
| 요구사항 | Product & Operation Requirement |
| Architecture | Target Architecture / 권한 모델 / API 기준 |
| Foundation | 공통 Framework / 공통 UI Component |
| Pilot | Pilot 결과 / Architecture Review |
| Migration | 메뉴별 전환 전략 / Migration Wave |
| Validation | WPF-Web Data Validation 결과 |
| Operation | Logging / Trace / Monitoring / 장애대응 기준 |
| Transition | 병행운영 / Web 전환 / WPF 종료 계획 |
| Improvement | Web 전환 이후 개선 Backlog |

---

## 6. 완료 기준

다음 조건을 충족하는 시점을 Web 전환 완료로 정의한다.

- 대상 기능 Web 전환 완료
- 기존 MARS와 데이터 정합성 확보
- 성능 및 안정성 검증
- 인증 / 인가 적용
- Logging / Trace / Monitoring 적용
- Error Reporting 및 운영 기반 구축
- Usage Analytics 기반 구축
- 사용자 검증 완료
- Web 공식 서비스 전환
- 기존 WPF 서비스 종료
- Architecture / 운영 문서 최신화 완료

---

## 7. 관련 세부 문서

- `01_Current_State_and_Scope.md`  
  현행 분석, Feature Inventory, Scope 관리 기준

- `02_Product_Operation_Requirements.md`  
  Data Explainability, Trace, Error Reporting, VOC, 사용자 설정, 공유, Usage Analytics, 권한, 다국어, AI 활용 기반

- `03_Architecture_and_Foundation.md`  
  Target Architecture, Frontend/Backend 구조, 공통 Foundation, Pilot 기준

- `04_Migration_and_Validation.md`  
  기능별 Migration 방식, Wave, Data Validation, 성능, UAT, 병행 운영

- `05_Roadmap.md`  
  1년 추진 일정, Gate, 월별 Roadmap, 일정 상세화 원칙
