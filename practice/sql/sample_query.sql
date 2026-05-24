-- 사용자 접속 통계 예제
-- 목적: 날짜별 접속 건수 집계

SELECT
    access_date,
    COUNT(*) AS access_count
FROM access_log
GROUP BY access_date
ORDER BY access_date;
