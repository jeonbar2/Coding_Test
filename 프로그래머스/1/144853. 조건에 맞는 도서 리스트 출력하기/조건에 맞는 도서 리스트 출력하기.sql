-- 코드를 입력하세요
SELECT book_id,
    DATE_FORMAT(published_date, '%Y-%m-%d') published_date
FROM BOOK
WHERE category = '인문'
and YEAR(published_DATE) = 2021