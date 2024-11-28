-- 코드를 입력하세요
SELECT a.DR_NAME, a.DR_ID, a.MCDP_CD, DATE_FORMAT(a.HIRE_YMD, '%Y-%m-%d') HIRE_YMD
FROM DOCTOR a
WHERE a.MCDP_CD in ('CS','GS')
order by a.HIRE_YMD DESC

