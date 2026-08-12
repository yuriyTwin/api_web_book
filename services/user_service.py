class UserService:

    def __init__(self, db):
        self.db = db

    def get_or_create_user(self, email):

        user = self.db.users.get_user_by_email(
            email=email
        ).one()

        if user is None:

            self.db.users.insert_user(
                email=email
            ).exec()

            user = self.db.users.get_user_by_email(
                email=email
            ).one()

        return user

    def get_last_play(self, email, book_id=None):

        print("EMAIL", email)
        user = self.get_or_create_user(email)

        if book_id is None:
            row = self.db.books.get_last_book(
                userId=user["id"]
            ).one()
        else:
            row = self.db.books.get_book_progress(
                userId=user["id"],
                bookId=book_id
            ).one()

        return row
