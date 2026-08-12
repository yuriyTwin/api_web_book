class BookService:

    def __init__(self, db, user_service):
        self.db = db
        self.user_service = user_service

    def get_books(self, email=None):
        return self.db.books.get_book_list(email=email).all()

    def search(self, text, email=None):
        return self.db.books.search_books(
            search=text,
            email=email
        ).all()


    def get_play_list(self, book_id, email):

        playlist = self.db.books.get_play_list(
            bookId=book_id
        ).all()

        books = []

        for book in playlist:
            books.append({
                        "mp3": f"abooks/{book['id']}/{book['fileNum']}.mp3",
                        "title": book["name"],
                        "poster": book["img"],
                        "oga": "",
                        "artist": ""
                        })

        last_play = self.user_service.get_last_play(
            email=email,
            book_id=book_id
        )

        return {
            "list": books,
            "lastPlay": last_play
        }


    def get_current_cycle_books(self, email):
        return self.db.books.get_current_cycle_books(
            email=email
        ).all()

    def get_last_ten_opened(self, email):
        return self.db.books.get_last_ten_opened(
            email=email
        ).all()


    def get_last_ten_not_opened(self, email):
        return self.db.books.get_last_ten_not_opened(
            email=email
        ).all()


    def get_last_ten_books(self, email):
        return self.db.books.get_last_ten_books(
            email=email
        ).all()


    def get_last_play(self, userId, bookId=None):

        if bookId is None:
            return self.db.books.get_last_play(
                userId=userId
            )

        return self.db.books.get_last_play_by_book(
                userId=userId,
                bookId=bookId
            )


    def set_play_time(self, email, book_id, file_num, time):

        user = self.db.users.get_user_by_email(email=email).one() #.all()[0]

        user_id = user["id"]

        self.db.users.update_last_book(
            userId=user_id,
            bookId=book_id
        ).exec()

        last_play = self.get_last_play(
            userId=user_id,
            bookId=book_id
            ).one() #.all()[0]


        if last_play["opened"] == 1:
            self.db.users.update_last_play(
                userId=user_id,
                bookId=book_id,
                fileNum=file_num,
                time=time
            ).exec()
        else:
            self.db.users.insert_last_play(
                userId=user_id,
                bookId=book_id,
                fileNum=file_num,
                time=time
            ).exec()

        return last_play
