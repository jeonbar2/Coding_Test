SELECT a.item_id, b.item_name
FROM ITEM_TREE a, ITEM_INFO b
where a.parent_item_id is null
and a.item_id = b.item_id;

