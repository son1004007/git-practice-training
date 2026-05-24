# Git 실습 교육 자료

## 목적

이 저장소는 Git Bash, VS Code, GitHub를 처음 사용하는 구성원이 실무에서 필요한 Git 기본 흐름을 빠르게 익히기 위한 교육용 저장소입니다.

## 교육 대상

- Git 사용 경험이 적은 데이터 분석가
- 분석 산출물, SQL, Python 코드, 보고서를 Git으로 관리해야 하는 실무자
- VS Code 기반으로 GitHub 협업 흐름을 익혀야 하는 구성원

## 최종 목표

교육 완료 후 아래 작업을 스스로 수행할 수 있어야 합니다.

1. Git Bash 설치 및 기본 설정
2. VS Code 설치 및 Git 연동
3. GitHub 개인 저장소 생성
4. 저장소 clone
5. 파일 수정, add, commit, push
6. commit message 작성 규칙 적용
7. branch 생성 및 Pull Request 생성
8. 실무 산출물 변경 이력 관리

## 교육 순서

| 단계 | 문서 | 목표 |
|---:|---|---|
| 1 | docs/00_교육개요.md | 전체 교육 흐름 이해 |
| 2 | docs/01_GitBash_설치.md | Git Bash 설치 및 기본 설정 |
| 3 | docs/02_VSCode_설치_설정.md | VS Code 설치 및 Git 사용 준비 |
| 4 | docs/03_GitHub_개인레포_생성.md | 개인 실습 저장소 생성 |
| 5 | docs/04_clone_commit_push_실습.md | 기본 Git 흐름 실습 |
| 6 | docs/05_branch_PR_실습.md | branch와 Pull Request 실습 |
| 7 | docs/06_commit_message_작성규칙.md | 사내 Git 작성규칙 적용 |
| 8 | docs/07_실무_시나리오_실습.md | SQL, Python, 보고서 변경 관리 실습 |
| 9 | docs/08_자주_발생하는_문제.md | 오류 대응 방법 확인 |

## 추가 문서

| 문서 | 목표 |
|---|---|
| docs/15_GitHub_가입_안내.md | GitHub 가입 안내 |
| docs/16_GitHub_초대메일_가입_흐름.md | 초대 메일 수락 및 저장소 접근 안내 |
| docs/17_PAT_생성_방법.md | GitHub 인증값 생성 및 사용 안내 |
| docs/19_GitHub_가입_안내_메일_템플릿.md | 교육생 안내 메일 예시 |

## 기본 원칙

- `main` 브랜치에 직접 작업하지 않습니다.
- 작업 단위별 브랜치를 생성합니다.
- 하나의 commit에는 하나의 목적만 담습니다.
- commit message는 `type(scope): 변경 내용` 형식을 사용합니다.
- 분석 결과에 영향을 주는 변경은 구체적으로 작성합니다.

## 실습 저장소 구조

```text
git-practice-training/
├── docs/
├── practice/
│   ├── memo/
│   ├── sql/
│   ├── python/
│   └── report/
└── templates/
```

## 권장 진행 방식

처음에는 명령어를 외우는 것보다 아래 흐름을 반복하는 것이 중요합니다.

```text
수정 → 확인 → stage → commit → push → GitHub에서 확인
```

## 참고 문서

- 사내 Git Commit Message 작성 규칙: `type(scope): 변경 내용`
- Conventional Commits 형식 기반
