-- 코드를 입력하세요
SELECT a.MEMBER_ID, a.MEMBER_NAME, a.GENDER, DATE_FORMAT(a.DATE_OF_BIRTH, '%Y-%m-%d') DATE_OF_BIRTH
from member_profile a
where a.TLNO is not null
and a.GENDER = 'W'
and DATE_FORMAT(a.DATE_OF_BIRTH, '%m') = 3 