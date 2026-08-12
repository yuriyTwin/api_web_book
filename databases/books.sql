CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE ganre(id integer primary key autoincrement, name char(150));
CREATE TABLE publish(id integer primary key autoincrement, name char(150));
CREATE TABLE reader(id integer primary key autoincrement, name char(150));
CREATE TABLE author(id integer primary key autoincrement, name char(150));
CREATE TABLE books(id integer primary key autoincrement, name char(255), description text, authorId int not null, ganreId int  not null, year int not null, readerId int not null, source text, playlist text, publishId int not null, time char(50), img text, cycleId int, orderId int, status int not null, torrent varchar(255));
CREATE TABLE cycleBook(id integer primary key autoincrement, authorId int not null, name char(150));
CREATE TABLE files(id integer primary key autoincrement, name char(150), source text not null, status int not null, bookid int not null, fileNum int not null, numOrder int null);