# SELECT *,b.INGREDIENT_TYPE, sum(a.total_order) TOTAL_ORDER
# from first_half a,icecream_info b
# where a.flavor = b.flavor
# group by b.ingredient_type
# order by sum(a.total_order) desc;
select INGREDIENT_TYPE ,sum(a.total_order) TOTAL_ORDER
from first_half a
inner join icecream_info b
on a.flavor = b.flavor
group by ingredient_type
