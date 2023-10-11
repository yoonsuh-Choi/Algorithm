# -- 코드를 입력하세요
SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY, PRICE) IN (
                            SELECT CATEGORY, MAX(PRICE)
                            FROM FOOD_PRODUCT
                            WHERE CATEGORY IN ('국', '김치', '식용유', '과자')
                            GROUP BY CATEGORY
)
ORDER BY MAX_PRICE DESC
;
# 마조유, 김치찌개, 허니버터칩, 배추김치