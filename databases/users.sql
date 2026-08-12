CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE users(id integer primary key autoincrement,login varchar(50), password varchar(50), email varchar(50), lastbookId int, hash varchar(255));
CREATE TABLE lastPlay(id integer primary key autoincrement, userId int not null, bookid int not null, filenum int not null, time decimal(5,18), lastupdate datetime);
