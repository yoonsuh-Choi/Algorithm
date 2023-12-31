-- 코드를 입력하세요
SELECT A.PRODUCT_ID, A.PRODUCT_NAME, SUM(B.AMOUNT*A.PRICE) AS TOTAL_SALES
FROM FOOD_ORDER B
INNER JOIN FOOD_PRODUCT A
ON A.PRODUCT_ID = B.PRODUCT_ID
WHERE PRODUCE_DATE LIKE '2022-05-%'
GROUP BY B.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID