# 06. Commit Message 작성규칙

## 1. 목적

commit message는 변경 이력을 설명하는 기록입니다.

나중에 아래 질문에 답할 수 있어야 합니다.

```text
무엇을 바꿨는가?
어디를 바꿨는가?
왜 바꿨는가?
분석 결과에 영향을 주는가?
```

---

## 2. 기본 형식

사내 Git 작성규칙은 아래 형식을 사용합니다.

```text
type(scope): 변경 내용
```

예시:

```text
feat(report): 월별 매출 분석 리포트 추가
fix(sql): 매출 집계 쿼리의 조인 조건 수정
docs(readme): 분석 데이터 출처 설명 추가
chore(env): 분석 환경 패키지 버전 정리
```

---

## 3. 구성 요소

| 항목 | 의미 | 필수 여부 | 예시 |
|---|---|---:|---|
| type | 변경의 성격 | 필수 | feat, fix, docs |
| scope | 변경 대상 | 권장 | sql, report, data |
| description | 실제 변경 내용 | 필수 | 월별 매출 집계 로직 수정 |

---

## 4. 우선 사용할 Type

처음에는 아래 6개만 사용해도 충분합니다.

| Type | 사용 기준 | 예시 |
|---|---|---|
| feat | 새 분석, 새 리포트, 새 지표 추가 | feat(report): 고객 이탈 분석 리포트 추가 |
| fix | 오류 수정 | fix(sql): 취소 주문 제외 조건 수정 |
| docs | 문서 수정 | docs(readme): 실행 방법 설명 추가 |
| chore | 정리, 설정, 유지보수 | chore(folder): 결과 파일 폴더 정리 |
| refactor | 결과 변화 없는 구조 개선 | refactor(preprocess): 전처리 로직 함수화 |
| test | 검증 코드 추가 또는 수정 | test(data): 매출 음수값 검증 로직 추가 |

---

## 5. 추가 Type

필요 시 아래 Type을 사용할 수 있습니다.

| Type | 사용 기준 | 예시 |
|---|---|---|
| perf | 실행 속도 또는 성능 개선 | perf(sql): 월별 매출 집계 쿼리 성능 개선 |
| build | 의존성, 패키지, 실행 환경 변경 | build(deps): pandas 버전 업데이트 |
| ci | 자동화, CI/CD 설정 변경 | ci(actions): 데이터 검증 워크플로우 추가 |

---

## 6. 권장 Scope

| Scope | 사용 상황 |
|---|---|
| sql | SQL 쿼리 변경 |
| notebook | Jupyter Notebook 변경 |
| report | 분석 리포트 변경 |
| dashboard | 대시보드 변경 |
| data | 데이터 정의, 샘플 데이터, 데이터 설명 변경 |
| preprocess | 전처리 로직 변경 |
| model | 모델 학습, 예측, 평가 코드 변경 |
| metric | 지표 정의, 계산식 변경 |
| env | 분석 환경 변경 |
| readme | README 변경 |
| config | 설정 파일 변경 |
| pipeline | 데이터 파이프라인 변경 |
| memo | 업무 메모 변경 |

---

## 7. 좋은 예시

```text
feat(metric): 재구매율 지표 추가
fix(sql): 주문 취소 건 제외 조건 수정
docs(data): 고객 테이블 컬럼 설명 추가
chore(env): 분석용 패키지 버전 정리
refactor(preprocess): 날짜 변환 로직 공통 함수로 분리
perf(sql): 월별 매출 집계 쿼리 성능 개선
test(data): 고객 ID 중복 검증 로직 추가
```

---

## 8. 나쁜 예시

```text
수정
업데이트
분석 추가
코드 변경
쿼리 수정
최종 수정
리포트 작업
```

나쁜 예시는 변경 목적과 대상을 알 수 없습니다.

---

## 9. 작성 규칙

### 규칙 1. 한글 사용 가능

팀 내 공유 목적이라면 한글 commit message를 사용해도 됩니다.

```text
fix(sql): 매출 집계 기준일 오류 수정
```

중요한 것은 언어가 아니라 형식의 일관성입니다.

### 규칙 2. description은 간결하게 작성

권장:

```text
fix(sql): 매출 집계 기준일 오류 수정
feat(report): 월별 매출 리포트 추가
docs(data): 고객 테이블 설명 추가
```

비권장:

```text
fix(sql): 매출 집계를 수정함
feat(report): 리포트를 만들었음
docs(data): 설명을 추가했음
```

### 규칙 3. 하나의 commit에는 하나의 목적만 포함

권장:

```text
fix(sql): 매출 집계 조인 조건 수정
docs(report): 매출 분석 기준 설명 추가
```

비권장:

```text
fix(sql): 매출 쿼리 수정 및 README 수정 및 패키지 업데이트
```

### 규칙 4. 분석 결과에 영향을 주는 변경은 구체적으로 작성

```text
fix(metric): 재구매율 계산 기준 수정
fix(sql): 취소 주문 제외 조건 추가
fix(preprocess): 결측 고객 연령 처리 방식 수정
```

---

## 10. 헷갈리는 기준

### feat vs fix

| 구분 | 기준 | 예시 |
|---|---|---|
| feat | 없던 것을 새로 추가 | feat(metric): 구매전환율 지표 추가 |
| fix | 잘못된 것을 수정 | fix(metric): 구매전환율 계산식 오류 수정 |

### docs vs chore

| 구분 | 기준 | 예시 |
|---|---|---|
| docs | 문서 내용 수정 | docs(readme): 실행 방법 추가 |
| chore | 관리성 작업 | chore(folder): 결과 파일 폴더 정리 |

### fix vs refactor

| 구분 | 기준 | 예시 |
|---|---|---|
| fix | 결과 오류 수정 | fix(preprocess): 결측치 처리 오류 수정 |
| refactor | 결과는 같고 구조만 개선 | refactor(preprocess): 결측치 처리 로직 함수화 |

---

## 11. 최종 요약

```text
1. commit message는 type(scope): 변경 내용 형식으로 작성합니다.
2. type은 변경의 성격입니다.
3. scope는 변경 대상입니다.
4. description은 무엇을 바꿨는지 간결하게 작성합니다.
5. 하나의 commit에는 하나의 목적만 담습니다.
6. 분석 결과에 영향을 주는 변경은 반드시 구체적으로 작성합니다.
```

---

## 12. 참고

이 문서는 사내 Git Commit Message 작성 규칙 문서를 교육용으로 요약한 것입니다.
