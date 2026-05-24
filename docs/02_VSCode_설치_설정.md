# 02. VS Code 설치 및 설정

## 1. 목적

VS Code에서 Git 저장소를 열고, 변경사항 확인, stage, commit, push를 수행할 수 있도록 설정합니다.

---

## 2. 설치 절차

1. VS Code 공식 사이트에 접속합니다.
2. Windows용 설치 파일을 다운로드합니다.
3. 설치 파일을 실행합니다.
4. 기본 옵션으로 설치합니다.
5. VS Code를 실행합니다.

---

## 3. 권장 확장 프로그램

| 확장 | 목적 |
|---|---|
| GitLens | commit 이력과 변경자 확인 |
| Markdown All in One | Markdown 문서 작성 보조 |
| Prettier | 문서와 코드 포맷 정리 |
| Korean Language Pack | 한글 UI 사용 |

---

## 4. Git 저장소 열기

1. VS Code 실행
2. File 메뉴 선택
3. Open Folder 선택
4. clone 받은 Git 저장소 폴더 선택
5. 왼쪽 Source Control 아이콘 확인

---

## 5. Source Control 기본 사용법

| 작업 | 설명 |
|---|---|
| Changes | 수정된 파일 목록 확인 |
| Stage Changes | commit 대상에 포함 |
| Commit | 변경 이력 저장 |
| Sync Changes | 원격 저장소와 동기화 |

---

## 6. 실습 흐름

```text
파일 수정
→ Source Control에서 변경 확인
→ Stage Changes
→ commit message 입력
→ Commit
→ Push
→ GitHub에서 반영 확인
```

---

## 7. 완료 기준

아래 작업이 가능하면 다음 단계로 이동합니다.

- VS Code에서 저장소 폴더 열기
- Source Control 메뉴 확인
- 변경 파일 확인
- stage 수행
- commit 수행
- push 수행
