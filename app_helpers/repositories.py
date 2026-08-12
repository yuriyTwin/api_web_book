from .repository import SqlRepository


class Repositories:

    def __init__(self, db):

        self.books = SqlRepository(db, "books")
        self.users = SqlRepository(db, "users")
        self.reader = SqlRepository(db, "reader")
        self.author = SqlRepository(db, "author")
        self.genre = SqlRepository(db, "genre")
