select count(*) as FISH_COUNT
from fish_info a, fish_name_info b
where a.fish_type = b.fish_type
and b.fish_name in ('BASS','SNAPPER')