select 
	b.id, 
	b.authorId, 
	b.orderId, 
	a.name as author, 
	b.cycleId, 
	c.name as cycle, 
	b.name, 
	b.img as origImg, 
	'originImg/' ||  b.id || '.png' as img, 
	b.readerId, 
	r.name as reader, 
	b.ganreId, 
	g.name as ganre, 
	b.time as duration, 
	0 as opened 
from users_db.lastplay l
join users_db.users u on u.id = l.userId 
join books b on l.bookid = b.id 
join author a on a.id = b.authorId 
left join cycleBook c on c.id = b.cycleId
join reader r on r.id = b.readerId 
join ganre g on g.id = b.ganreId 
where l.lastupdate is not null and u.email = :email 
order by l.lastupdate desc 
limit 10
