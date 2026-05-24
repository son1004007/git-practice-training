"""접속 로그 데이터 검증 예제."""

required_columns = {"access_date", "menu"}

sample_row = {
    "access_date": "2026-05-01",
    "menu": "home",
}

missing_columns = required_columns - set(sample_row.keys())

if missing_columns:
    raise ValueError(f"필수 컬럼 누락: {missing_columns}")

print("데이터 검증 완료")
