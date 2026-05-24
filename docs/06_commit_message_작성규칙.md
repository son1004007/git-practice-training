# Git Commit Message 요약본

## 1. 기본 형식

```text
type(scope): 변경 내용(한글 가능)
```

예시:

```text
fix(sql): 매출 집계 조건 오류 수정
feat(report): 월별 매출 분석 리포트 추가
docs(data): 고객 테이블 컬럼 설명 추가

```

---

## 2. Type 선택 기준

| Type       | 외우는 기준              | 예시                                       |
| ---------- | ------------------------ | ------------------------------------------ |
| `feat`     | 새로 추가                | `feat(report): 월별 매출 리포트 추가`      |
| `fix`      | 오류 수정                | `fix(sql): 취소 주문 제외 조건 수정`       |
| `docs`     | 문서 수정                | `docs(data): 주문 테이블 설명 추가`        |
| `chore`    | 정리/설정                | `chore(env): 패키지 버전 정리`             |
| `refactor` | 결과 변화 없는 구조 개선 | `refactor(preprocess): 전처리 로직 함수화` |
| `test`     | 검증 코드                | `test(data): 고객 ID 중복 검증 추가`       |

---

## 3. 빠른 선택법

```text
새로 추가했다       → feat
잘못된 것을 고쳤다  → fix
문서만 바꿨다       → docs
정리/설정 작업이다   → chore
결과는 같고 구조 개선 → refactor
검증 코드를 추가했다  → test
```

---

## 4. 자주 쓰는 scope

```text
sql
report
dashboard
notebook
data
metric
preprocess
model
env
readme
config
```

---

## 5. 작성 예시

```text
feat(metric): 고객 재구매율 지표 추가
fix(sql): 매출 집계 조인 조건 수정
docs(readme): 실행 방법 설명 추가
chore(env): requirements.txt 정리
refactor(preprocess): 날짜 변환 로직 공통 함수화
test(data): 매출 음수값 검증 로직 추가
```

---

## 6. 금지 예시

```text
수정
작업
업데이트
최종
진짜 최종
```

---

## 7. 한 줄로 기억하기

```text
무엇을 했는지(type), 어디를 바꿨는지(scope), 무엇이 바뀌었는지(description)를 쓴다.
```
