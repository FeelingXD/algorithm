-- 코드를 입력하세요 
SELECT O.Animal_id, O.name 
from Animal_outs O
where O.animal_id not in (select animal_id from animal_ins)