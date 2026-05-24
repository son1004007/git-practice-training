# 10. Conflict 해결 실습

## 1. 목적

Git conflict는 같은 파일의 같은 부분을 서로 다르게 수정했을 때 발생합니다.

이 문서는 conflict를 의도적으로 발생시키고 해결하는 과정을 실습합니다.

---

## 2. 실습 전제

아래 내용을 이미 수행했다고 가정합니다.

- 저장소 clone 완료
- Git Bash 또는 VS Code 사용 가능
- commit, push 기본 실습 완료

---

## 3. 실습 흐름

```text
main 최신화
→ branch A 생성
→ 같은 파일 수정 후 commit
→ main에 merge
→ branch B 생성
→ 같은 파일 같은 위치 수정
→ merge 시 conflict 확인
→ conflict 해결
→ commit
```

---

## 4. 실습 파일

```text
practice/report/analysis_result.md
```

---

## 5. branch A 작업

main을 최신화합니다.

```bash
git switch main
git pull origin main
```

branch A를 생성합니다.

```bash
git switch -c docs/report-summary-a
```

`practice/report/analysis_result.md` 파일의 결과 요약 부분을 수정합니다.

예시:

```markdown
## 결과 요약

- 날짜별 접속 건수를 기준으로 이용 현황을 확인했습니다.
```

commit합니다.

```bash
git add practice/report/analysis_result.md
git commit -m "docs(report): 결과 요약 문구 수정 A"
```

main에 반영합니다.

```bash
git switch main
git merge docs/report-summary-a
```

---

## 6. branch B 작업

branch B를 생성합니다.

```bash
git switch -c docs/report-summary-b
```

같은 파일의 같은 위치를 다르게 수정합니다.

예시:

```markdown
## 결과 요약

- 웹 접속 로그를 기준으로 주요 이용 패턴을 확인했습니다.
```

commit합니다.

```bash
git add practice/report/analysis_result.md
git commit -m "docs(report): 결과 요약 문구 수정 B"
```

---

## 7. conflict 발생시키기

main으로 이동합니다.

```bash
git switch main
```

branch B를 merge합니다.

```bash
git merge docs/report-summary-b
```

같은 파일 같은 위치가 서로 다르면 conflict가 발생합니다.

---

## 8. conflict 파일 확인

파일을 열면 아래와 비슷한 표시가 보입니다.

```text
<<<<<<< HEAD
main 브랜치 내용
=======
병합하려는 브랜치 내용
>>>>>>> docs/report-summary-b
```

의미:

| 표시 | 의미 |
|---|---|
| HEAD | 현재 브랜치 내용 |
| ======= | 변경 내용 구분선 |
| >>>>>>> | 병합하려는 브랜치 내용 |

---

## 9. conflict 해결

둘 중 하나를 선택하거나 두 내용을 합쳐서 최종 문장을 작성합니다.

예시:

```markdown
## 결과 요약

- 날짜별 접속 건수와 웹 접속 로그를 기준으로 주요 이용 현황을 확인했습니다.
```

주의할 점:

- `<<<<<<<` 표시를 제거합니다.
- `=======` 표시를 제거합니다.
- `>>>>>>>` 표시를 제거합니다.
- 최종 문장만 남깁니다.

---

## 10. 해결 후 commit

```bash
git status
git add practice/report/analysis_result.md
git commit -m "fix(conflict): 결과 요약 문구 충돌 해결"
```

---

## 11. VS Code에서 해결하는 방법

VS Code는 conflict 발생 시 아래 버튼을 제공합니다.

| 버튼 | 의미 |
|---|---|
| Accept Current Change | 현재 브랜치 내용 선택 |
| Accept Incoming Change | 병합 대상 브랜치 내용 선택 |
| Accept Both Changes | 두 변경 내용 모두 반영 |
| Compare Changes | 차이 비교 |

초급자는 버튼만 누르기보다 최종 파일 내용을 직접 확인해야 합니다.

---

## 12. 실무 대응 기준

| 상황 | 대응 |
|---|---|
| 문서 문장 충돌 | 의미가 맞도록 최종 문장 재작성 |
| SQL 조건 충돌 | 결과 수치 영향 확인 후 반영 |
| Python 코드 충돌 | 실행 테스트 후 반영 |
| 분석 기준 충돌 | 작성자 또는 담당자에게 기준 확인 |

---

## 13. 실습 완료 기준

아래 commit이 생성되면 conflict 실습이 완료됩니다.

```text
fix(conflict): 결과 요약 문구 충돌 해결
```

---

## 14. 핵심 요약

```text
conflict는 오류가 아니라 Git이 자동으로 판단할 수 없는 변경입니다.
최종 파일 내용을 사람이 직접 결정해야 합니다.
```
