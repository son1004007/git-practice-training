# 01. Git Bash 설치

## 목적

Windows PC에서 Git 명령어를 실행할 수 있도록 Git Bash를 설치합니다.

---

## 다운로드 링크

아래 링크에서 Windows용 Git 설치 파일을 다운로드합니다.

```text
https://git-scm.com/install/windows
```

---

## 설치 순서

1. 위 다운로드 링크에 접속합니다.
2. Git for Windows 설치 파일을 다운로드합니다.
3. 설치 파일을 실행합니다.
4. 기본 옵션으로 설치합니다.
5. Git Bash를 실행합니다.
6. Git 버전을 확인합니다.

---

## 설치 확인

```bash
git --version
```

버전 정보가 표시되면 설치가 완료된 것입니다.

---

## 최초 설정

아래 항목을 본인 정보에 맞게 설정합니다.

```bash
git config --global user.name "본인 이름"
git config --global user.email "GitHub 이메일"
git config --global init.defaultBranch main
git config --global core.autocrlf true
```

---

## 설정 확인

```bash
git config --global --list
```

---

## 완료 기준

아래 두 명령어가 정상 동작하면 다음 단계로 이동합니다.

```bash
git --version
git config --global --list
```
