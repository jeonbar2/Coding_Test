-- 코드를 작성해주세요
select year(DIFFERENTIATION_DATE) as YEAR,  abs(a.size_of_colony - sz) as YEAR_DEV,ID
from ECOLI_DATA a,(
select max(size_of_colony) as sz, year(DIFFERENTIATION_DATE) as j from ECOLI_DATA
group by j) b
where year(a.DIFFERENTIATION_DATE) = j
order by YEAR , YEAR_DEV



