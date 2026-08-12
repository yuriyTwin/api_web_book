insert into users_db.lastPlay(bookid, fileNum, time, userId, lastupdate)
values(:bookId, :fileNum, :time, :userId, datetime('now','localtime'))
