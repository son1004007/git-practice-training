# 18. SQLTools PostgreSQL 사용법

## 1. 목적

VS Code에서 SQLTools 확장을 사용하여 PostgreSQL DB에 접속하고 SQL 파일을 실행합니다.

---

## 2. 필요한 확장 프로그램

아래 확장 프로그램을 설치합니다.

| 확장 프로그램 | 목적 |
|---|---|
| SQLTools | DB 연결, SQL 실행, 결과 확인 |
| SQLTools PostgreSQL/Cockroach Driver | PostgreSQL 접속 드라이버 |

---

## 3. SQLTools 기본 설정

SQLTools가 Node 런타임 문제로 실행되지 않는 경우 아래 설정을 사용합니다.

1. VS Code에서 `Ctrl + ,` 입력
2. `sqltools use node runtime` 검색
3. `SQLTools: Use Node Runtime` 체크 해제

`settings.json`에서는 아래처럼 설정합니다.

```json
{
  "sqltools.useNodeRuntime": false
}
```

---

## 4. PostgreSQL 연결 추가

1. 왼쪽 사이드바에서 SQLTools 아이콘 선택
2. Add New Connection 선택
3. PostgreSQL 선택
4. 접속 정보 입력
5. Test Connection 선택
6. 연결 성공 시 Save Connection 선택

예시:

```text
Connection name: onycom-postgresql
Server Address: dev.openankus.org
Port: 5432
Database: DB명
Username: onycom
Password: 접속 비밀번호
SSL: enabled 또는 required
```

비밀번호는 가능하면 설정 파일에 직접 저장하지 않고, 접속할 때 입력하도록 설정합니다.

---

## 5. SQL 파일 실행

`.sql` 파일을 열고 SQLTools 연결을 선택한 뒤 SQL을 실행합니다.

예시 SQL:

```sql
SELECT current_database(), current_user, now();
```

파일마다 연결을 지정해두면 매번 연결을 선택하지 않아도 됩니다.

1. `.sql` 파일에서 우클릭
2. SQLTools: Attach Connection To This File 선택
3. 사용할 DB 연결 선택

---

## 6. 단축키 설정

기본 단축키가 동작하지 않거나 더 편한 실행 단축키가 필요하면 직접 설정합니다.

1. `Ctrl + Shift + P` 입력
2. Preferences: Open Keyboard Shortcuts (JSON) 선택
3. 아래 설정 추가

```json
[
  {
    "key": "ctrl+enter",
    "command": "sqltools.executeCurrentQuery",
    "when": "editorTextFocus && editorLangId == sql"
  },
  {
    "key": "ctrl+shift+enter",
    "command": "sqltools.executeQueryFromFile",
    "when": "editorTextFocus && editorLangId == sql"
  }
]
```

| 단축키 | 실행 내용 |
|---|---|
| Ctrl + Enter | 현재 커서 위치의 SQL 실행 |
| Ctrl + Shift + Enter | 현재 SQL 파일 전체 실행 |

---

## 7. SQL 자동 저장 및 정렬

자동 저장은 `.sql` 파일에도 동일하게 적용됩니다.

```json
{
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000
}
```

SQLTools의 SQL 정렬 기능도 사용할 수 있습니다.

| 작업 | 방법 |
|---|---|
| 선택한 SQL 정렬 | 우클릭 후 Format Selected Query For Any Document |
| 선택한 SQL 정렬 단축키 | Ctrl + E, Ctrl + B |

SQL 정렬 옵션 예시:

```json
{
  "sqltools.formatLanguages": ["sql"],
  "sqltools.format": {
    "reservedWordCase": "upper",
    "linesBetweenQueries": 1
  }
}
```

---

## 8. 완료 기준

아래 작업이 가능하면 다음 단계로 이동합니다.

- SQLTools 연결 생성
- PostgreSQL Test Connection 성공
- `.sql` 파일에 DB 연결 지정
- `Ctrl + Enter`로 현재 SQL 실행
- SQL 실행 결과 확인
