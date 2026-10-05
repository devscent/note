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

### 2.3 기존 기능 유지 중심의 Web 전환

이번 프로젝트는 **기능 개선 자체보다 Web 기술 전환을 우선**한다.

기존 MARS에서 정상적으로 사용되고 있는 업무 Logic과 기능은 원칙적으로 유지하며, Web 전환 과정에서 불필요하게 기능 범위를 확대하지 않는다.

다만 현행 기능을 분석할 때는 단순히 모든 기능을 1:1로 옮기는 것으로 가정하지 않고, 각 기능을 다음과 같이 분류하여 전환 방향을 판단한다.

| 구분 | 의미 | 이번 Web 전환에서의 기본 원칙 |
|---|---|---|
| 유지 | 현재 기능과 업무 Logic에 특별한 문제가 없음 | **기본 선택**. 기존 기능을 그대로 Web으로 이전 |
| 개선 | 기능은 유지하되 사용성 또는 일부 구조 개선이 필요 | Web 전환에 꼭 필요한 범위만 반영하고, 나머지는 후속 개선 Backlog로 관리 |
| 통합 | 유사·중복 기능이 존재 | 명확한 필요성이 있는 경우에만 검토하고, 원칙적으로 후속 과제로 관리 |
| 재설계 | 업무 Flow 또는 기능 구조 자체의 변경이 필요 | 이번 전환 범위에서는 최소화하고 별도 개선 과제로 분리 |
| 폐기 | 사용성이 낮거나 더 이상 필요하지 않음 | 실제 사용량과 업무 필요성을 확인한 뒤 전환 대상 제외 여부 검토 |

이 분류의 목적은 Web 전환과 동시에 대규모 PI를 수행하기 위한 것이 아니라, **기존 기능을 무조건 1:1 복제하지 않으면서도 전환 범위를 통제하기 위한 판단 기준을 마련하는 것**이다.

WPF와 Web의 UI 기술 및 Interaction 방식이 다르므로, 기존 조작 방식을 그대로 재현하는 것이 비효율적이거나 부자연스러운 경우에는 Web 환경에 적합한 방식으로 조정한다.

예:

- WPF 전용 Control을 Web Component로 대체
- Popup 중심 Flow를 Page / Panel / Dialog 등 Web에 적합한 방식으로 변경
- Grid / Chart Interaction을 Web 사용 방식에 맞게 조정
- Browser URL, Link, Navigation 등 Web의 특성을 활용

이러한 변경은 **업무 기능의 PI가 아니라 기술 플랫폼 변경에 따른 필수적인 UX 적응**으로 본다.

기존 기능에서 개선 필요사항이 발견되는 경우에는 다음 원칙을 적용한다.

| 구분 | 처리 원칙 |
|---|---|
| Web 전환에 반드시 필요한 변경 | 이번 전환에 반영 |
| 기술 Stack 변경에 따른 UI/UX 조정 | 이번 전환에 반영 |
| 명백한 오류 또는 전환을 방해하는 문제 | 필요 시 함께 수정 |
| 업무 Process 또는 기능 Logic의 큰 변경 | 원칙적으로 후속 개선 과제로 분리 |
| 신규 기능 / 대규모 PI | Web 전환 이후 Improvement Backlog로 관리 |

즉, **기존 기능의 안정적인 이전을 Baseline으로 하고, 큰 기능 개선은 Web 전환 완료 이후 단계적으로 추진**한다.

개선 필요사항을 무시하는 것은 아니다. 현행 분석과 Migration 과정에서 발견되는 문제와 개선 아이디어는 체계적으로 기록하고 우선순위를 부여하되, Web 전환 Scope와 분리하여 후속 개선 Roadmap의 입력으로 활용한다.

### 2.4 운영 가능한 시스템 구축

기존 운영 과정에서 반복적으로 발생했던 장애 대응, 데이터 문의, 재현 어려움, VOC 추적 문제를 줄일 수 있도록 시스템 자체에 운영성을 내재화한다.

---

## 3. 추진 원칙

### 3.1 메뉴 이관보다 공통 기반을 우선한다

20개 기능을 개별적으로 먼저 개발하지 않는다.

인증, 권한, Logging, Trace, 공통 UI, 사용자 설정, 사용현황 수집, Error 처리 등 모든 기능에서 필요한 기반을 먼저 설계하고 구축한다.

### 3.2 기존 기능 유지와 범위 통제를 원칙으로 한다

기존 기능을 Web으로 안정적으로 옮기는 것을 우선하며, 업무 Logic과 기능 범위의 변경은 최소화한다.

전환 과정에서 확인된 개선사항은 별도의 Improvement Backlog로 관리하여 Web 전환 범위가 지속적으로 확대되지 않도록 한다.

단, Web 기술 특성상 필요한 UI/UX 변경과 공통 운영 기반 구축은 이번 전환 범위에 포함한다.

### 3.3 Pilot 이후 본격 Migration을 진행한다

대표 기능을 먼저 End-to-End로 구현하여 Architecture, 개발 방식, 성능, 운영 구조를 검증한 뒤 전체 기능 전환을 진행한다.

### 3.4 사용자 관점과 운영자 관점을 함께 설계한다

화면 기능뿐 아니라 다음 질문에 답할 수 있도록 한다.

- 사용자는 이 데이터가 왜 이렇게 나왔는지 이해할 수 있는가?
- 문제가 발생했을 때 운영자는 해당 요청을 쉽게 찾고 추적할 수 있는가?
- 사용자가 별도 설명 없이 문제 상황을 전달할 수 있는가?
- 어떤 기능이 실제로 사용되고 있는지 알 수 있는가?
- 향후 기능 개선의 효과를 사용 데이터로 확인할 수 있는가?

### 3.5 기존 WPF 서비스 종료까지를 전환 범위로 본다

Web Open 자체를 프로젝트 완료로 보지 않는다.

일정 기간 병행 운영을 통해 안정성을 확인한 후 기존 WPF 기반 MARS 서비스를 종료하는 단계까지 포함한다.

---

# 4. 전체 추진 구조

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

# 5. Phase 1. 현행 시스템 분석

## 5.1 Feature Inventory 작성

현재 MARS의 전체 메뉴 및 기능을 조사한다.

각 기능에 대해 다음 항목을 정리한다.

| 분석 항목 | 내용 |
|---|---|
| 기능 목적 | 어떤 업무를 지원하는가 |
| 주요 사용자 | 주요 사용자 및 조직 |
| 사용 빈도 | 실제 사용량 |
| 중요도 | 업무 영향도 |
| 입력 조건 | EQP, 기간, Recipe, Parameter 등 |
| 출력 형태 | Grid, Chart, Report, Export 등 |
| 데이터 Source | DB / Table / View / SP |
| 처리 Logic | 주요 계산 및 Business Logic |
| 데이터 규모 | 평균/최대 조회량 |
| 현행 실행 구조 | DataService, DLL, Framework 등 서버측 실행 방식 |
| 외부 의존성 | 파일, 외부 시스템 등 |
| 공통 기능 | 다른 메뉴와 공유되는 Logic/UI |
| VOC | 반복적으로 발생한 문의/불편 |
| 개선 필요사항 | 전환 시 필수 변경 / 후속 개선 Backlog 구분 |
| 난이도 | S / M / L / XL |

## 5.2 Backend 및 DB 구조 분석

- 현행 DataService에서 실행되는 MARS 서버측 기능
- DB 접근 및 Connection 구조
- Stored Procedure 및 주요 Query
- Business Logic 위치
- 기존 Framework / 공통 Library 사용 방식
- 대용량 / 장시간 Query
- 신규 Backend API로 이전해야 할 Logic
- Error / Logging 방식

## 5.3 운영 이슈 분석

기존 운영 과정에서 반복적으로 발생한 VOC와 장애 대응 경험을 정리한다.

예:

- 데이터가 조회되지 않는 이유를 사용자가 알기 어려움
- 특정 값이 계산된 근거를 확인하기 어려움
- 사용자 문제 상황 재현이 어려움
- 장애 발생 시 정확한 조회조건/시간을 다시 물어봐야 함
- 사용자별 환경 및 설정이 유지되지 않음
- 실제 기능 사용량을 정확히 파악하기 어려움
- VOC가 비정형 형태로 남아 반복 문제 분석이 어려움

이 결과를 Phase 2의 Product / Operation Requirement로 연결한다.

---

# 6. Phase 2. Product / Operation Requirement 정의

Web MARS가 기본적으로 가져야 할 공통적인 제품·운영 요구사항을 정의한다.

이 단계는 개별 메뉴 개발과 별도로 수행한다.

여기서 정의하는 Logging, Trace, 권한, 사용자 설정, 공유, 사용현황 등의 기능은 **개별 업무 기능의 PI가 아니라 Web MARS 전체가 공통적으로 가져야 할 플랫폼·운영 기반**으로 본다.

## 6.1 Data Explainability

사용자가 조회 결과의 생성 과정과 조건을 이해할 수 있도록 한다.

검토 항목:

- 조회 기준 및 적용 조건 표시
- 데이터 기준 시각 / 최신화 시각
- Filter 적용 내역
- 제외 조건
- 계산 Logic 설명
- Raw → Filter → Result 데이터 건수
- 주요 지표 정의
- 데이터 Source 또는 Data Lineage 정보

목표:

> "왜 이 데이터가 이렇게 나왔는가?"라는 질문을 시스템 자체에서 최대한 설명할 수 있도록 한다.

---

## 6.2 Traceability / Observability

사용자 요청부터 DB 처리까지 전체 흐름을 추적할 수 있도록 한다.

예:

```text
User Action
   ↓
Frontend
   ↓
API Request
   ↓
Backend Logic
   ↓
DB Query
```

공통 Trace ID 또는 Request ID를 부여하여 다음 정보를 연결한다.

- 사용자
- 메뉴 / 화면
- 발생 시각
- 조회 조건
- API
- Backend 처리
- DB Query
- 처리시간
- Error
- Application Version

목표:

> 사용자가 문제를 제보했을 때 최소한의 정보만으로 해당 실행 내역을 확인할 수 있도록 한다.

---

## 6.3 Error Reporting / Support

사용자가 문제 상황을 쉽게 전달할 수 있는 기능을 검토한다.

예:

**문제 신고 / Feedback**

사용자가 신고 시 시스템이 자동으로 다음 정보를 수집할 수 있도록 설계한다.

- User
- 현재 메뉴 / URL
- 조회조건
- 화면 State
- Trace ID
- 발생 시각
- Browser
- Frontend / Backend Version
- 최근 Error 정보

필요 시 Screenshot 또는 사용자 설명을 추가한다.

목표:

```text
"Parameter Trend가 안 됩니다"
```

형태의 VOC를

```text
Issue + Trace ID + 조회조건 + Error Context
```

형태의 재현 가능한 정보로 전환한다.

---

## 6.4 VOC Management

VOC를 비정형 메시지로만 관리하지 않고 구조화한다.

예시 분류:

- Bug
- Data Question
- How-to
- Performance
- Improvement
- Feature Request
- Access / Permission

추가 관리 항목:

- Menu
- User
- Time
- Trace ID
- Severity
- Status
- Root Cause
- Resolution

이를 기반으로 반복 VOC, 기능별 문의량, Root Cause 등을 분석할 수 있도록 한다.

---

## 6.5 User Preference / Personalization

사용자별 설정을 저장할 수 있는 공통 구조를 설계한다.

예:

- Language
- Theme
- Timezone
- Favorite Menu
- Favorite Equipment
- 최근 선택 조건
- Default Date Range
- Grid Column
- Page Size
- Chart Option
- Holiday 제외 여부

Global Preference와 Feature별 Preference를 구분하여 관리한다.

---

## 6.6 Collaboration / Share

현재 분석 상태를 다른 사용자와 공유할 수 있는 기능을 검토한다.

예:

- 현재 View URL 공유
- 조회조건 포함 Link
- Saved View
- Snapshot
- 특정 사용자에게 공유

공유 시 다음 원칙을 적용한다.

> 공유는 권한 자체를 전달하지 않고 View State만 전달한다.

수신자는 자신의 권한 범위 내에서만 공유된 내용을 확인할 수 있도록 한다.

---

## 6.7 Usage Analytics

사용자가 MARS를 실제로 어떻게 사용하는지 Event 기반으로 수집한다.

예:

- PAGE_VIEW
- QUERY_EXECUTED
- EXPORT_EXCEL
- SHARE_CREATED
- ERROR_OCCURRED
- FAVORITE_ADDED
- 주요 Chart Interaction

이를 기반으로 다음을 분석한다.

- DAU / MAU
- 메뉴별 사용자 수
- 메뉴별 사용빈도
- 기능 Adoption
- Excel Export 사용량
- Error 발생량
- 평균 Query 시간
- 사용되지 않는 기능
- 신규 기능 도입 효과

Usage Data는 향후 기능 개선, 투자 우선순위 및 기능 유지 여부 판단의 근거로 활용한다.

---

## 6.8 Authorization

단순 로그인 여부가 아닌 세밀한 권한 구조를 설계한다.

기본 구조:

```text
User
 ↓
Role
 ↓
Permission
```

Permission은 필요 시 메뉴보다 세부적인 기능 단위까지 확장 가능하도록 한다.

예:

- ParameterTrend.View
- ParameterTrend.Export
- ParameterTrend.Share
- RawData.View
- Admin.UserManagement
- Admin.PermissionManagement

향후 필요 시 다음 Data Scope를 적용할 수 있도록 구조를 고려한다.

- 조직
- FAB
- 공정
- Equipment
- 특정 데이터 종류

---

## 6.9 Localization / 다국어

초기 서비스 언어가 제한적이더라도 다국어 확장이 가능하도록 Resource 기반 구조를 적용한다.

화면 문자열을 코드에 직접 작성하지 않고 Resource Key 기반으로 관리한다.

예:

```text
menu.parameterTrend.title
button.search
label.equipment
```

---

## 6.10 AI Ready Operation

AI 기능 자체를 우선 개발하기보다 AI가 활용할 수 있는 운영 데이터를 먼저 구조화한다.

기반 데이터:

- Error Log
- Trace
- VOC
- Usage Event
- Performance Metric
- Data Processing Metadata
- 운영 문서

향후 활용 예:

- 반복 VOC 자동 분류
- 유사 장애 검색
- Error 원인 분석 지원
- 주간 VOC 요약
- 성능 이상 탐지 보조
- 데이터 결과 설명 지원
- 운영 Knowledge 검색

원칙:

> AI 기능보다 먼저 신뢰할 수 있는 구조화된 운영 데이터를 확보한다.

---

# 7. Phase 3. Target Architecture 및 공통 기반 설계

## 7.1 기본 구조

```text
Browser
   │
   ▼
MARS Web Frontend
   │
   ▼
MARS Backend / API
   │
   ▼
MARS MSSQL
```

## 7.2 주요 설계 항목

### Frontend

- Framework
- Routing
- Layout / Navigation
- 상태 관리
- API 호출
- Error 처리
- 공통 Component
- 다국어
- 사용자 Preference
- 공유 가능한 화면 State

### Backend

- API 구조
- Business Logic Layer
- Data Access Layer
- DB Connection
- Validation
- Authorization
- Logging
- Trace
- Configuration
- Background Processing
- 대용량 데이터 처리

### Authentication / Authorization

- 사내 SSO 연계
- 사용자 Identity
- Role / Permission
- 관리자 기능
- Data Scope 확장성

### 운영

- Logging
- Health Check
- Monitoring
- Application Metric
- CI/CD
- Rollback
- 환경별 Configuration

---

# 8. Phase 4. Product & Operation Foundation 구축

개별 메뉴 개발 전에 다음 공통 기반을 우선 구축한다.

## 필수 Foundation

- Application Layout / Navigation
- SSO
- Authorization Framework
- 공통 API / Error 규칙
- DB Access
- Logging
- Trace ID
- Error Report / Feedback 기본 구조
- Usage Event 수집
- User Preference Framework
- i18n Framework
- Health Check
- Monitoring
- CI/CD

## 공통 UI Component

MARS의 반복 패턴을 중심으로 구성한다.

- Equipment Selector
- Date / Time Selector
- Recipe Selector
- Parameter Selector
- Data Grid
- Chart
- Loading / Empty State
- Dialog
- Tooltip
- Tab
- Excel / CSV Export

---

# 9. Phase 5. Pilot 개발

대표 기능을 선정하여 End-to-End 전환을 수행한다.

Pilot은 단순한 화면 하나를 만드는 것이 아니라 전체 Architecture를 검증하는 단계로 정의한다.

## Pilot 선정 기준

가능하면 다음 요소를 포함한 기능을 선택한다.

- 검색 조건
- DB Query
- 대용량 데이터
- Grid
- Chart
- 사용자 Interaction
- Export
- 권한
- Error / Trace
- Usage Event

## Pilot 검증 항목

- Frontend / Backend 구조
- API / DB Access
- 성능
- 공통 Component 재사용성
- 인증 / 인가
- Logging / Trace
- Error Reporting
- Usage Analytics
- 배포 / Rollback
- 기존 WPF와 데이터 정합성

Pilot 결과를 기반으로 Architecture와 Foundation을 보완한 뒤 본격 Migration을 진행한다.

---

# 10. Phase 6. 기능별 Migration

현행 분석 및 Pilot 결과를 기반으로 기능별 전환 범위와 난이도를 확정한다.

기본 원칙은 **기존 업무 기능과 결과를 유지하는 것**이며, Web 기술 특성상 필요한 변경만 전환 범위에 포함한다.

예:

| 기능 | 중요도 | 사용량 | Web 전환 방식 | 필수 UX 적응 | 후속 개선 Backlog | 난이도 |
|---|---:|---:|---|---|---|---|
| A | High | High | 동일 기능 전환 | 없음 | 없음 | S |
| B | High | High | 동일 기능 전환 | Grid Interaction 변경 | 검색 UX 개선 | M |
| C | Medium | Medium | 동일 기능 전환 | Popup → Panel | 기능 통합 검토 | L |
| D | High | High | 동일 기능 전환 | Chart Library 변경 | 분석 기능 개선 | XL |

전환 과정에서 발견된 개선 아이디어는 원칙적으로 Web 전환 범위에 즉시 추가하지 않고 Improvement Backlog로 관리한다.

단, 다음 항목은 예외적으로 이번 전환에 포함할 수 있다.

- Web 환경에서 기존 기능을 그대로 구현하기 어려운 경우
- 기존 기능의 명백한 오류가 확인된 경우
- 그대로 이전할 경우 사용자 업무 수행에 문제가 발생하는 경우
- 공통 Component 또는 운영 기반과 함께 처리하는 것이 현저히 효율적인 경우

기능은 중요도, 난이도 및 기술적 공통성을 고려하여 여러 Migration Wave로 나누어 단계적으로 이전한다.

예:

- Wave 1: 기본 조회 기능
- Wave 2: 주요 Grid / Chart 분석 기능
- Wave 3: 대용량 / 고복잡도 기능
- Wave 4: 특수 기능 및 잔여 기능

각 Wave에서 새롭게 확인된 공통 패턴은 Foundation에 반영하여 이후 기능에서 재사용한다.

---

# 11. Phase 7. 통합 검증

## 11.1 Functional / Data Validation

동일한 조건에서 WPF와 Web 결과를 비교한다.

- 조회 결과
- Row Count
- Aggregation
- Average / Median
- 시간 계산
- Wafer / Lot Mapping
- Null / Missing Data
- Sorting / Filtering
- Chart
- Excel Export

Web 전환 과정에서 불가피하게 동작이 변경된 경우에는 변경사항과 사유를 명시적으로 관리한다.

## 11.2 Performance / Load Test

- 화면 응답시간
- API Response Time
- DB Query Time
- 동시 사용자
- Connection Pool
- Backend CPU / Memory
- 대용량 Response
- Chart Rendering
- Excel Export
- Timeout
- 장시간 Query

## 11.3 Security

- HTTPS
- SSO
- Authorization
- Session / Token
- Secret 관리
- DB Credential
- API 접근제어
- 사용자 입력 Validation
- Error 정보 노출
- Audit

## 11.4 UAT

실제 사용자 기준으로 다음을 검증한다.

- 기존 업무 수행 가능 여부
- 기능 누락
- 데이터 결과
- 사용성
- Web 환경 적응 변경사항
- 성능
- 브라우저 환경
- 권한

---

# 12. Phase 8. 병행 운영 및 Web 정식 전환

Web 안정성이 확인될 때까지 일정 기간 WPF와 Web을 병행 운영한다.

```text
           ┌─ MARS WPF
User ──────┤
           └─ MARS Web
```

병행 운영 기간에 다음을 수행한다.

- Web 사용 확대
- 사용자 Feedback
- 기능 누락 확인
- 장애 대응
- 데이터 정합성 확인
- 성능 확인
- VOC 분석

안정성 확보 후 Web을 공식 서비스로 전환한다.

---

# 13. Phase 9. 기존 WPF 서비스 종료

Web 전환 완료 후 일정 기간 병행 운영을 통해 안정성을 확인하고 기존 WPF 기반 MARS 서비스를 종료한다.

주요 항목:

- 신규 기능 개발은 Web을 기준으로 수행
- WPF 배포 및 운영 종료
- 사용자 Web 전환 완료 확인
- 기존 WPF Source 및 운영 자료 Archive
- 운영 / Architecture 문서 최신화


---

# 14. 프로젝트 관리 시 별도 관리해야 할 항목

## 14.1 Scope 관리

Web 전환에 필요한 변경과 후속 기능 개선을 구분하여 관리한다.

전환 과정에서 발생한 개선 요구는 즉시 Scope에 포함하지 않고 Improvement Backlog로 관리하는 것을 원칙으로 한다.

## 14.2 Legacy Change Control

Web 전환 기간 중 WPF가 계속 변경되면 Migration 대상이 지속적으로 움직이게 된다.

따라서 일정 시점 이후 기존 WPF에 대해 다음 원칙을 검토한다.

- 장애 수정: 허용
- 필수 업무 변경: 제한적으로 허용
- 일반 기능 개선: 원칙적으로 Web 전환 이후 검토
- 신규 기능: 긴급성이 없는 경우 Web 전환 이후 검토

## 14.3 Decision Log

Architecture, 전환 범위, 기능 변경 등 주요 의사결정과 이유를 기록한다.

## 14.4 Risk / Issue

- 기술 리스크
- 일정 리스크
- DB / 성능 리스크
- 운영 리스크
- 외부 시스템 의존성
- 사용자 전환 리스크

를 지속적으로 관리한다.

---

# 15. 주요 산출물

| 단계 | 주요 산출물 |
|---|---|
| 현행 분석 | Feature Inventory / Dependency Map / VOC 분석 |
| Product Requirement | Product & Operation Requirement |
| Architecture | Target Architecture / 권한 모델 / API 기준 |
| Foundation | 공통 Framework / UI Component |
| Pilot | Pilot 결과 / Architecture Review |
| Migration | 메뉴별 전환 전략 / Migration Wave |
| Improvement | Web 전환 이후 개선 Backlog |
| Validation | WPF-Web Data Validation 결과 |
| Performance | 성능 / 부하 Test 결과 |
| Operation | Logging / Monitoring / 장애대응 기준 |
| Transition | Cut-over / 병행운영 / 기존 WPF 서비스 종료 계획 |

---

# 16. 완료 기준

MARS Web 전환은 Web 화면 개발 완료만으로 종료하지 않는다.

다음 조건을 충족하는 시점을 완료로 정의한다.

- 대상 기능 Web 전환 완료
- 기존 MARS와 데이터 정합성 확보
- 성능 및 안정성 검증
- 인증 / 인가 적용
- Logging / Trace / Monitoring 적용
- Error Reporting 및 운영 기반 구축
- Usage Analytics 기반 구축
- 사용자 검증 완료
- Web 공식 서비스 전환
- WPF 운영 종료
- Architecture / 운영 문서 최신화 완료

---

# 17. 1년 추진 일정(안)

본 일정은 전체 프로젝트의 **초기 Roadmap**이며, 개별 메뉴별 상세 개발 일정은 현행 분석과 Pilot 결과를 기준으로 보정하여 확정한다.

초기부터 20개 메뉴의 완료일을 고정하기보다는 다음 4개의 주요 Gate를 기준으로 프로젝트를 관리한다.

| Gate | 목표 시점 | 완료 기준 |
|---|---|---|
| G1. Scope / Architecture Baseline | Month 2 | Feature Inventory, 공통 요구사항, Target Architecture 초안 확정 |
| G2. Foundation / Pilot 검증 | Month 4 | 공통 기반과 대표 기능의 End-to-End 동작 검증 |
| G3. 주요 기능 Migration 완료 | Month 10 | Web 전환 대상 기능 개발 및 주요 데이터 검증 완료 |
| G4. Service Transition 완료 | Month 12 | 사용자 검증, 병행 운영, Web 정식 전환 및 기존 WPF 서비스 종료 |

## 17.1 월별 Roadmap

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

> `●`는 해당 업무가 집중적으로 수행되는 기간을 의미한다.  
> 기능 Migration, Validation, Foundation 개선은 실제 진행 과정에서 일부 중첩하여 수행한다.

## 17.2 단계별 주요 내용

### Month 1–2: 현행 분석 및 기준 수립

- 전체 Feature Inventory 작성
- 메뉴별 사용량 / 중요도 / 난이도 조사
- Backend / DB / 공통 Logic 분석
- 기존 VOC 및 운영 이슈 정리
- Product / Operation Requirement 정의
- Web 전환 Scope와 후속 Improvement Backlog 구분
- Target Architecture 초안 수립

**주요 결과물**

- Feature Inventory
- Dependency / Backend 구조
- Product & Operation Requirement
- 전환 Scope
- Target Architecture 초안

---

### Month 2–4: Foundation 및 Pilot

- Web Frontend / Backend 기본 구조 구축
- SSO / Authorization
- 공통 Layout / Navigation
- API / DB Access / Error 처리
- Logging / Trace
- User Preference / i18n 기본 Framework
- Usage Event / Feedback 기본 구조
- 공통 Grid / Chart / Selector 등 핵심 Component
- 대표 메뉴 Pilot 구현

Pilot을 통해 실제 개발 방식, 재사용성, 데이터 처리, 성능 및 운영 구조를 검증한다.

**주요 결과물**

- Web 공통 Foundation
- 대표 기능 Pilot
- 개발 / 배포 기본 Flow
- Pilot Review 결과
- Migration 상세계획 보정

---

### Month 5–10: 본격 기능 Migration

Pilot에서 확정한 방식과 공통 Component를 이용하여 기능을 여러 Wave로 나누어 전환한다.

```text
Wave 1
  ↓
Wave 2
  ↓
Wave 3
  ↓
Wave 4 / 잔여 기능
```

각 Wave에서는 개발 완료만을 기준으로 하지 않고 다음 과정을 함께 수행한다.

```text
기능 개발
   ↓
기존 WPF 결과 비교
   ↓
오류 / 차이 수정
   ↓
공통 Component 보완
   ↓
다음 Wave
```

전환 과정에서 발견되는 기능 개선 아이디어는 원칙적으로 Improvement Backlog에 기록하고, Web 전환 Scope 확대를 최소화한다.

---

### Month 8–11: 통합 검증 및 사용자 검증

기능 Migration 후반부터 검증 작업을 병렬로 강화한다.

- WPF / Web Data Validation
- Integration Test
- Regression Test
- Performance / Load Test
- Security 검토
- 운영 / 장애 대응 검증
- 실제 사용자 UAT
- 주요 VOC 반영
- 사용자 전환 준비

---

### Month 10–12: 병행 운영 및 서비스 전환

일정 기간 WPF와 Web을 병행 운영하면서 실제 사용 환경에서 안정성을 확인한다.

- Web 사용 확대
- 기능 누락 / 데이터 차이 확인
- 운영 장애 및 성능 확인
- 사용자 Feedback 반영
- 주요 문제 해결

안정성이 확인되면 Web을 공식 MARS 서비스로 전환하고 기존 WPF 서비스를 종료한다.

---

# 18. 일정 상세화 원칙

초기 계획에서는 전체 Phase와 주요 Milestone을 정의하고, 메뉴별 상세 일정은 다음 순서로 확정한다.

```text
현행 Inventory 작성
      ↓
기능별 난이도 / Web 전환 범위 평가
      ↓
Target Architecture 결정
      ↓
Pilot 수행
      ↓
Pilot 실제 생산성 확인
      ↓
메뉴별 예상 공수 재산정
      ↓
Migration Wave 및 상세 일정 확정
```

특히 20개 기능을 단순히 동일한 크기로 간주하여 `메뉴 수 × 일정`으로 산정하지 않는다.

기능별로 다음 요소를 고려한다.

- UI 복잡도
- Backend Logic 복잡도
- DB Query / 데이터량
- 공통 Component 재사용 가능성
- 기존 WPF와의 데이터 검증 난이도
- Web 환경 적응이 필요한 정도
- 외부 의존성
- 운영 중요도

Pilot 완료 시점에 실제 개발 생산성을 기준으로 전체 Migration 일정을 한 차례 재검토한다.

---

# 19. 일정 관리 원칙

## 19.1 계획은 Rolling 방식으로 구체화한다

전체 1년 Roadmap은 유지하되, 상세 계획은 가까운 기간일수록 구체적으로 관리한다.

예:

- 전체 프로젝트: 월 단위
- 다음 2~3개월: 기능 / Wave 단위
- 현재 개발 구간: 주 단위

## 19.2 개발 완료와 검증 완료를 구분한다

메뉴 개발이 끝났더라도 기존 WPF와의 데이터 정합성 및 주요 Test가 완료되지 않으면 해당 기능을 완료로 처리하지 않는다.

## 19.3 Migration 후반에 검증을 몰아두지 않는다

각 Wave 개발과 동시에 Validation을 수행하여 후반부에 대량의 검증 작업이 누적되지 않도록 한다.

## 19.4 일정 Buffer를 확보한다

대용량 분석 기능, 기존 Logic 분석, 예상하지 못한 데이터 차이, 기존 시스템 운영 이슈 등에 대응할 수 있도록 후반 일정에 안정화 기간을 확보한다.
