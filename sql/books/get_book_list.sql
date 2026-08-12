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
	case when lp.bookid is null then 0 else 1 end as opened 
from books b 
join author a on a.id = b.authorId 
left join cycleBook c on c.id = b.cycleId 
join reader r on r.id = b.readerId 
join ganre g on g.id = b.ganreId 
left join(select bookid from users_db.lastPlay l 
		  join users_db.Users u on u.id = l.userId
		  where u.email = :email)lp on lp.bookid = b.id 
