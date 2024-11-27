-- 코드를 입력하세요
SELECT ROUND(sum(a.daily_fee)/count(*) ,0) as AVERAGE_FEE
from CAR_RENTAL_COMPANY_CAR a
where a.car_type = 'SUV'