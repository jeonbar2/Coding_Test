select a.id,c.fish_name,a.length
from fish_info a ,(
    SELECT fish_type, MAX(length) as LENGTH
    FROM fish_info
    GROUP BY fish_type) b
    , fish_name_info c
where a.length = b.length
and a.fish_type = b.fish_type
and a.fish_type = c.fish_type
    
