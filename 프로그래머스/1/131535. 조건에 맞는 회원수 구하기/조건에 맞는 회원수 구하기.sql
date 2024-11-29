-- 코드를 입력하세요
SELECT count(*) as USERS
FROM USER_INFO
where age>=20 
AND age<=29
AND JOINED like '2021%'