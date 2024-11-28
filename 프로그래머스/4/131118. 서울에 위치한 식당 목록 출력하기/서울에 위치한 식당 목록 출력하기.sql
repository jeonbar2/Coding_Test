-- 코드를 입력하세요
SELECT a.REST_ID, a.REST_NAME, a.FOOD_TYPE, a.FAVORITES, a.ADDRESS, ROUND(avg(b.REVIEW_SCORE),2) SCORE
FROM REST_INFO a, rest_review b
where a.rest_id = b.rest_id
and a.address like '서울%'
group by a.rest_id, a.rest_name
order by score desc