"""접속 로그 집계 예제."""

from collections import Counter

logs = [
    {"access_date": "2026-05-01", "menu": "home"},
    {"access_date": "2026-05-01", "menu": "notice"},
    {"access_date": "2026-05-02", "menu": "home"},
]

counts = Counter(row["access_date"] for row in logs)

for access_date, count in sorted(counts.items()):
    print(access_date, count)
