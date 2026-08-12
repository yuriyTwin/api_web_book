select
    b.id as bookid,
    b.name,
    'originImg/' || b.id || '.png' as img,
    lp.fileNum,
    lp.time,
    case
        when lp.time is not null then 1
        else 0
    end as opened
from books b
left join users_db.lastPlay lp
    on lp.bookId = b.id
   and lp.userId = :userId
where b.id = :bookId
