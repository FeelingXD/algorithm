-- 경기도에 위치한 식품창고 목록
SELECT warehouse_id , warehouse_name, address ,IFnull(freezer_yn,'N') as freezer_yn
from food_warehouse 
where warehouse_name like '창고_경기%'
order by warehouse_id 
