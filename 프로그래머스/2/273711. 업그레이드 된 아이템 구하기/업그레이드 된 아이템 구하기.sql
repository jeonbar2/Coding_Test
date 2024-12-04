-- 코드를 작성해주세요
select c.item_id, item_name, rarity
from item_info c,
(select b.item_id
from item_info a left outer join item_tree b
on a.item_id = b.parent_item_id
where rarity = 'RARE'
and parent_item_id is not null)d
where c.item_id = d.item_id
order by item_id desc
