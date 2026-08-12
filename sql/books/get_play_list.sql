select 
	b.id, 
	f.fileNum, 
	b.img as origImg, 
	'originImg/' ||  b.id || '.png' as img, 
	f.name 
from files f 
join books b on b.id = f.bookid 
where f.bookid = :bookId 
order by f.numOrder
