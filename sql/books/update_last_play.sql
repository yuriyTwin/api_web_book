update users_db.lastPlay
set fileNum = :fileNum,
    time = :time,
    lastupdate=datetime('now','localtime')
where userId = :userId and bookId = :bookId
