select count(*) as FISH_COUNT, max(b.length)as MAX_LENGTH, b.FISH_TYPE
from fish_info b, 
    (select fish_type ,avg(IFNULL(length,10)) length 
        from fish_info
        group by fish_type
        having length>=33
        ) a
where b.fish_type = a.fish_type
group by b.fish_type
order by fish_type;