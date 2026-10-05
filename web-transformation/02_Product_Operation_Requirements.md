# MARS Web 전환 - Product / Operation Requirements

## 1. 목적

개별 메뉴 기능과 별개로 Web MARS 전체가 공통적으로 가져야 할 사용자·운영 기반을 정의한다.

---

## 2. Data Explainability

사용자가 조회 결과의 생성 과정과 조건을 이해할 수 있도록 한다.

검토 항목:

- 조회 기준 및 적용 조건
- 데이터 최신화 시각
- Filter / 제외 조건
- 계산 Logic
- Raw → Filter → Result 건수
- 주요 지표 정의
- Data Source / Lineage 정보

목표:

> "왜 이 데이터가 이렇게 나왔는가?"라는 질문을 시스템 자체에서 최대한 설명할 수 있도록 한다.

---

## 3. Traceability / Observability

사용자 요청부터 DB 처리까지 하나의 Trace로 연결한다.

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

Trace에 연결할 주요 정보:

- User
- Menu / URL
- 발생 시각
- 조회 조건
- API
- Backend 처리
- DB Query
- 처리시간
- Error
- Application Version

---

## 4. Error Reporting / Support

사용자가 문제를 신고할 때 시스템이 가능한 많은 Context를 자동으로 함께 전달하도록 한다.

예:

- User
- Menu / URL
- 조회조건
- 화면 State
- Trace ID
- 발생 시각
- Browser
- Frontend / Backend Version
- 최근 Error
- 필요 시 Screenshot

---

## 5. VOC Management

VOC 분류 예:

- Bug
- Data Question
- How-to
- Performance
- Improvement
- Feature Request
- Access / Permission

관리 정보:

- Menu
- User
- Time
- Trace ID
- Severity
- Status
- Root Cause
- Resolution

목표는 VOC 대응뿐 아니라 반복 VOC와 Root Cause를 분석하여 제품 개선으로 연결하는 것이다.

---

## 6. User Preference / Personalization

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

Global Preference와 Feature별 Preference를 구분한다.

---

## 7. Collaboration / Share

현재 분석 상태를 다른 사용자와 공유할 수 있도록 한다.

예:

- 현재 View URL 공유
- 조회조건 포함 Link
- Saved View
- Snapshot
- 특정 사용자에게 공유

원칙:

> 공유는 권한을 전달하지 않고 View State만 전달한다.

---

## 8. Usage Analytics

Event 예:

- PAGE_VIEW
- QUERY_EXECUTED
- EXPORT_EXCEL
- SHARE_CREATED
- ERROR_OCCURRED
- FAVORITE_ADDED
- 주요 Chart Interaction

활용 예:

- DAU / MAU
- 메뉴별 사용량
- 신규 기능 Adoption
- Excel Export 사용량
- Error 발생량
- 평균 Query 시간
- 사용되지 않는 기능

---

## 9. Authorization

기본 구조:

```text
User
 ↓
Role
 ↓
Permission
```

예:

- ParameterTrend.View
- ParameterTrend.Export
- ParameterTrend.Share
- RawData.View
- Admin.UserManagement
- Admin.PermissionManagement

향후 필요 시 Data Scope 확장:

- 조직
- FAB
- 공정
- Equipment
- 특정 데이터 종류

---

## 10. Localization

초기 서비스 언어가 제한적이어도 Resource 기반 구조를 적용한다.

예:

```text
menu.parameterTrend.title
button.search
label.equipment
```

---

## 11. AI Ready Operation

AI 기능 자체보다 먼저 구조화된 운영 데이터를 확보한다.

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
