/*O= out, I= In*/
select O.animal_id,O.name
from animal_ins I join animal_outs O
on I.animal_id =O.animal_id
where I.datetime> O.datetime 
ORDER BY I.DATETIME;

