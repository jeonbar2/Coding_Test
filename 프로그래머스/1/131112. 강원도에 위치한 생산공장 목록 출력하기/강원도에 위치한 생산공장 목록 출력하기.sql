-- 코드를 입력하세요
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
from food_factory
where address like '강원%'
order by factory_id asc;
