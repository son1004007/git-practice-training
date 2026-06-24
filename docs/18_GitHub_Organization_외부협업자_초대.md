# 18. GitHub Organization 특정 저장소 외부 협업자 초대

## 1. 목적

Organization 전체 멤버로 가입시키지 않고, 필요한 저장소에만 사용자를 초대하는 방법을 안내합니다.

이 방식으로 추가된 사용자는 **outside collaborator(외부 협업자)**가 되며, 관리자가 지정한 저장소와 권한 범위에만 접근합니다.

---

## 2. 적용 기준

다음 상황에서 outside collaborator 방식을 사용합니다.

- 외부 개발자나 단기 참여자에게 특정 저장소만 공개해야 하는 경우
- Organization의 다른 private 저장소는 보여 주지 않아야 하는 경우
- Organization 팀 구성원으로 관리할 필요가 없는 경우
- 프로젝트 종료 후 저장소 접근 권한만 개별적으로 회수해야 하는 경우

Organization의 여러 저장소와 팀 자원을 지속적으로 사용해야 하는 내부 구성원이라면 Organization 멤버 초대가 더 적합할 수 있습니다.

---

## 3. 사전 조건

- 초대 대상 저장소에 `Admin` 권한이 있어야 합니다.
- Organization 정책에서 outside collaborator 초대를 허용해야 합니다.
- Organization이 2단계 인증을 요구하면 초대 대상자도 초대 수락 전에 2FA를 활성화해야 합니다.
- 초대 대상자의 GitHub username을 미리 확인하는 것이 가장 확실합니다.

> 공개 저장소 문서에는 실제 개인 이메일 주소를 기록하지 않습니다. 이메일 주소는 GitHub 초대 화면에서만 입력하고, 교육 문서에는 `<이메일>` 또는 `<GitHub username>` 같은 자리표시자를 사용합니다.

---

## 4. 권한 선택 기준

| 역할 | 적용 기준 |
|---|---|
| `Read` | 코드와 문서 열람, clone, pull만 필요 |
| `Triage` | 코드 수정 없이 Issue, Discussion, PR 정리 필요 |
| `Write` | branch push, PR 작성·병합 등 일반 개발 참여 필요 |
| `Maintain` | 민감하거나 파괴적인 설정을 제외한 저장소 운영 필요 |
| `Admin` | 접근 권한, 보안 설정, 저장소 삭제 등 전체 관리 필요 |

기본 원칙은 **최소 권한 부여**입니다.

- 코드 확인만 필요하면 `Read`
- 일반 개발 참여가 필요하면 `Write`
- 권한 관리가 필요하지 않다면 `Admin`을 부여하지 않음

---

## 5. 초대 절차

1. GitHub에서 대상 Organization의 **특정 저장소**로 이동합니다.
2. 저장소 상단의 `Settings`를 선택합니다.
3. 왼쪽 메뉴의 `Access` 영역에서 `Collaborators & teams`를 선택합니다.
4. `Manage access` 오른쪽의 `Add people`을 선택합니다.
5. 검색창에 초대 대상자의 `<GitHub username>` 또는 GitHub 계정에 연결된 `<이메일>`을 입력합니다.
6. 검색 결과에서 올바른 계정을 선택합니다.
7. `Choose a role`에서 필요한 저장소 역할을 선택합니다.
8. `Add 사용자명 to 저장소명`을 선택합니다.
9. 상대방에게 GitHub 초대 메일을 확인하고 수락하도록 안내합니다.

### 권장 입력 방식

가능하면 이메일보다 **GitHub username**으로 초대합니다.

- 이메일이 GitHub 계정에 연결되지 않았으면 검색되지 않을 수 있음
- 같은 이름의 계정을 잘못 선택할 위험을 줄일 수 있음
- 초대 대상 계정을 사전에 확인하기 쉬움

---

## 6. Organization 멤버 초대와의 차이

| 구분 | Outside collaborator | Organization member |
|---|---|---|
| 접근 범위 | 지정한 저장소만 | Organization 정책과 팀 설정에 따라 여러 저장소 |
| 팀 가입 | 불가 | 가능 |
| 권한 관리 | 저장소별 역할 | Organization, 팀, 저장소 권한 조합 |
| 권장 대상 | 외부 인력, 단기 참여자 | 내부 구성원, 장기 협업자 |

특정 저장소만 허용하려는 목적이라면 `Organization → People → Invite member`가 아니라 대상 저장소의 `Settings → Collaborators & teams`에서 초대합니다.

---

## 7. 초대 후 확인

저장소의 `Settings → Collaborators & teams`에서 다음 항목을 확인합니다.

- 대상 계정이 올바른지
- 부여한 역할이 의도한 권한인지
- 초대가 `Pending` 상태인지 또는 수락되었는지
- 사용자가 Organization 멤버가 아니라 outside collaborator로 관리되는지
- 사용자가 저장소에 접근하고 필요한 작업을 수행할 수 있는지

상대방에게는 다음 항목을 확인하도록 요청합니다.

- GitHub 초대 메일 수신
- 초대 수락
- 저장소 화면 접근
- clone 또는 pull 가능
- `Write` 권한이 필요한 경우 branch push 가능

초대받은 사용자의 수락 절차는 [16. GitHub 초대메일 가입 흐름](./16_GitHub_초대메일_가입_흐름.md)을 참고합니다.

---

## 8. 초대가 되지 않을 때

| 증상 | 확인 사항 |
|---|---|
| 이메일 검색 결과가 없음 | GitHub username으로 다시 검색 |
| 초대 메일이 오지 않음 | 스팸함, 입력 주소, GitHub 알림 확인 |
| 초대를 수락할 수 없음 | Organization의 2FA 요구 여부 확인 |
| `Add people`이 보이지 않음 | 저장소 `Admin` 권한과 Organization 정책 확인 |
| 저장소는 보이지만 fork가 보이지 않음 | 필요한 fork에도 별도 접근 권한 부여 |
| push가 거부됨 | 역할이 `Write` 이상인지, branch protection 또는 ruleset 확인 |

---

## 9. 라이선스와 운영 주의사항

- 유료 플랜의 private 저장소에 outside collaborator를 추가하면 유료 라이선스를 사용할 수 있습니다.
- Outside collaborator는 Organization 팀에 추가할 수 없습니다.
- 저장소 fork에도 접근시켜야 한다면 해당 fork에 별도로 권한을 부여해야 합니다.
- 프로젝트 종료일이나 접근 검토일을 별도로 기록하고 불필요한 권한은 즉시 회수합니다.
- 공용 문서, Issue, commit message에 실제 개인 이메일이나 불필요한 개인정보를 남기지 않습니다.

---

## 10. 접근 권한 변경 또는 제거

1. 대상 저장소의 `Settings`로 이동합니다.
2. `Access → Collaborators & teams`를 선택합니다.
3. `Manage access`에서 대상 사용자를 찾습니다.
4. 권한만 변경하려면 `Role` 메뉴에서 새 역할을 선택합니다.
5. 접근을 종료하려면 대상 사용자 옆의 `Remove`를 선택합니다.

권한 제거 후에는 저장소 접근과 push가 차단되었는지 확인합니다.

---

## 11. 관리자 체크리스트

| 확인 항목 | 완료 |
|---|---|
| 대상 저장소 확인 |  |
| 초대 대상 GitHub username 확인 |  |
| 최소 권한 역할 선택 |  |
| 초대 발송 |  |
| 초대 수락 확인 |  |
| 저장소 접근 테스트 |  |
| 프로젝트 종료 또는 권한 검토일 기록 |  |

---

## 12. 공식 문서

- [Adding outside collaborators to repositories in your organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-outside-collaborators/adding-outside-collaborators-to-repositories-in-your-organization)
- [Managing teams and people with access to your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository)
- [Repository roles for an organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)
- [People who consume a license in an organization](https://docs.github.com/en/billing/reference/github-license-users)
