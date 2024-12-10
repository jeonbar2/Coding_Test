-- 코드를 입력하세요
SELECT ANIMAL_TYPE,count(*) COUNT
FROM ANIMAL_INS
GROUP BY animal_type
ORDER BY animal_type asc