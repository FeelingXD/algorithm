-- 월별 잡은 물고기 수 구하기
SELECT COUNT(*) AS FISH_COUNT,MONTH(TIME) AS MONTH
FROM FISH_INFO
GROUP BY MONTH
ORDER BY MONTH