select a.item_id, a.item_name, a.rarity 
from item_info a left outer join item_tree b
on a.item_id = b.parent_item_id
where parent_item_id is null
order by item_id desc

