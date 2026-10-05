# MARS Web 전환 - Migration / Validation

## 1. 기능별 Migration

기본 원칙은 **기존 업무 기능과 결과를 유지하는 것**이다.

예:

| 기능 | 중요도 | 사용량 | Web 전환 방식 | 필수 UX 적응 | 후속 개선 Backlog | 난이도 |
|---|---:|---:|---|---|---|---|
| A | High | High | 동일 기능 전환 | 없음 | 없음 | S |
| B | High | High | 동일 기능 전환 | Grid Interaction 변경 | 검색 UX 개선 | M |
| C | Medium | Medium | 동일 기능 전환 | Popup → Panel | 기능 통합 검토 | L |
| D | High | High | 동일 기능 전환 | Chart Library 변경 | 분석 기능 개선 | XL |

---

## 2. Migration Wave

예:

- Wave 1: 기본 조회 기능
- Wave 2: 주요 Grid / Chart 분석 기능
- Wave 3: 대용량 / 고복잡도 기능
- Wave 4: 특수 기능 / 잔여 기능

각 Wave는 다음 흐름으로 진행한다.

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

---

## 3. Functional / Data Validation

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

---

## 4. Performance / Load Test

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

---

## 5. Security

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

---

## 6. UAT

- 기존 업무 수행 가능 여부
- 기능 누락
- 데이터 결과
- 사용성
- Web 환경 적응 변경사항
- 성능
- 브라우저 환경
- 권한

---

## 7. 병행 운영 및 전환

일정 기간 WPF와 Web을 병행 운영한다.

```text
           ┌─ MARS WPF
User ──────┤
           └─ MARS Web
```

병행 운영 기간에:

- Web 사용 확대
- 사용자 Feedback
- 기능 누락 확인
- 장애 대응
- 데이터 정합성 확인
- 성능 확인

안정성이 확보되면 Web을 공식 서비스로 전환하고 기존 WPF 서비스를 종료한다.
