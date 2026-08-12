select
    b.id as bookid,
    b.name,
    'originImg/' || b.id || '.png' as img,
    l.fileNum,
    l.time,
    1 as opened
from books b
join users_db.lastPlay l
    on b.id = l.bookId
join users_db.users u
    on l.bookId = u.lastbookId
where u.id = :userId
