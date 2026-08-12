select
    b1.id,
    b1.authorId,
    b1.orderId,
    a.name as author,
    b1.cycleId,
    c.name as cycle,
    b1.name,
    b1.img as origImg,
    'originImg/' || b1.id || '.png' as img,
    b1.readerId,
    r.name as reader,
    b1.ganreId,
    g.name as ganre,
    b1.time as duration,
    case when b1.id = b.id then 1 else 0 end as opened
from books b
join books b1 on b1.cycleId = b.cycleId
join author a on a.id = b1.authorId
left join cycleBook c on c.id = b1.cycleId
join reader r on r.id = b1.readerId
join ganre g on g.id = b1.ganreId
join users_db.users u on u.lastbookId = b.id
where u.email = :email
order by b1.orderId
