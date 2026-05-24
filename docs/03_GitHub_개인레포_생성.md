# 03. GitHub 개인 레포 생성

## 1. 목적

개인 실습용 GitHub 저장소를 생성하고, 로컬 PC에서 실습할 준비를 합니다.

---

## 2. 저장소 생성 절차

1. GitHub에 로그인합니다.
2. 우측 상단의 New repository를 선택합니다.
3. Repository name을 입력합니다.
4. 공개 범위를 선택합니다.
5. Create repository를 선택합니다.

---

## 3. 권장 저장소 이름

```text
git-practice-training
```

또는 개인 이름을 포함해도 됩니다.

```text
git-practice-본인이름
```

---

## 4. 공개 범위 선택 기준

| 구분 | 기준 |
|---|---|
| Public | 교육용, 공개해도 되는 샘플 자료 |
| Private | 업무 자료, 고객 자료, 비공개 분석 자료 |

실무에서는 고객 데이터, 내부 문서, 분석 결과가 포함될 수 있으므로 기본적으로 Private을 권장합니다.

---

## 5. 저장소 주소 확인

저장소 생성 후 Code 버튼을 눌러 저장소 주소를 확인합니다.

예시 형식:

```text
https://github.com/계정명/저장소명.git
```

---

## 6. 로컬 PC로 가져오기

Git Bash 또는 VS Code에서 clone을 수행합니다.

```bash
git clone 저장소주소
```

clone 후 생성된 폴더로 이동합니다.

```bash
cd 저장소명
```

---

## 7. 완료 기준

아래 조건을 만족하면 다음 단계로 이동합니다.

- GitHub 개인 저장소 생성 완료
- 저장소 주소 확인 완료
- 로컬 PC에 clone 완료
- VS Code에서 저장소 폴더 열기 완료
