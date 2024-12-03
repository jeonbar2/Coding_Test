-- 코드를 입력하세요
select a.product_id, a.product_name, a.product_cd, a.category, a.price
from FOOD_PRODUCT a, (SELECT max(price) as price from FOOD_PRODUCT) b
where a.price = b.price


