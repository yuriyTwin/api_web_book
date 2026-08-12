update users_db.users 
set lastbookId = :bookId 
where id = :userId
