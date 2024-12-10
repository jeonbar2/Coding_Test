select count(fish_type) as FISH_COUNT, month(TIME) as MONTH
from fish_info
group by MONTH
order by MONTH