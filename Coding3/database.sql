WITH RankedScores AS (
    SELECT 
        s.*,
        DENSE_RANK() OVER (ORDER BY score DESC) as score_rank
    FROM student.score s
)
SELECT 
    r.name,
    r.score,
    c.class
FROM RankedScores r
JOIN student.class c ON r.name = c.name
WHERE r.score_rank = 2;

/*
查詢說明

1. 使用 WITH 子句創建一個 CTE
2. DENSE_RANK() 函數用來給成績排名，按照分數降序排列
3. 透過 JOIN 串 student.class 來取得 class

註：用 DENSE_RANK() 而不是 ROW_NUMBER()是
因為如果有同分的情況，DENSE_RANK() 會給予相同的排名

*/