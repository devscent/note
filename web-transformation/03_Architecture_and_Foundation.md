# MARS Web 전환 - Architecture / Foundation

## 1. Target Architecture

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

---

## 2. Frontend 설계 항목

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

---

## 3. Backend 설계 항목

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

---

## 4. Authentication / Authorization

- 사내 SSO 연계
- 사용자 Identity
- Role / Permission
- 관리자 기능
- Data Scope 확장성

---

## 5. 운영 기반

- Logging
- Health Check
- Monitoring
- Application Metric
- CI/CD
- Rollback
- 환경별 Configuration

---

## 6. 공통 Foundation

### 필수
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

### 공통 UI
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

## 7. Pilot

대표 기능 하나를 선정해 End-to-End로 구현한다.

선정 시 포함하면 좋은 요소:

- 검색 조건
- DB Query
- 대용량 데이터
- Grid
- Chart
- Interaction
- Export
- 권한
- Error / Trace
- Usage Event

Pilot에서 검증할 항목:

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
