from flask import Flask, request, jsonify

from app_helpers.database import Database
from app_helpers.repositories import Repositories
from app_helpers.sql_loader import SqlLoader
from services.user_service import UserService
from services.book_service import BookService

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

print("BASE_DIR =", BASE_DIR)
print("SQL_DIR =", BASE_DIR / "sql")


app = Flask(__name__)

loader = SqlLoader(BASE_DIR / "sql")

database = Database(
    main_db="/mnt/disk2/html/newbooks/databases/books.sqlite",
    sql_loader=loader,
    attachments={
        "users_db":"/mnt/disk2/html/newbooks/databases/users.sqlite"
    }
)

db = Repositories(database)
user_service = UserService(db)


settings = {
    "sourceBasePath": "http://chnemo.asuscomm.com/",
}

book_service = BookService(db, user_service)

@app.route("/")
def home():
    return "Hello Flask"


@app.route("/getBookList")
def books():

    return book_service.get_books(
        email=request.args.get("email")
    )


@app.route("/serarchBooks")
def search():

    return book_service.search(
        text=request.args.get("search", ""),
        email=request.args.get("email")
    )


@app.route("/getPlayList")
def get_play_list():

    id = request.args.get("id",int)
    email = request.args.get("email")

    return book_service.get_play_list(id, email)


@app.route("/getCurrentCycleBooks")
def current_cycle_books():

    email = request.args.get("email")

    return book_service.get_current_cycle_books(email)


@app.route("/getlastTenOpened")
def get_last_ten_opened():

    email = request.args.get("email")

    return book_service.get_last_ten_opened(email)


@app.route("/getLastTenNotOppenedBooks")
def get_last_ten_not_opened():

    email = request.args.get("email")

    return book_service.get_last_ten_not_opened(email)


@app.route("/getLastTenBooks")
def get_last_ten_books():

    email = request.args.get("email")

    return book_service.get_last_ten_books(email)


@app.route("/getLastTime")
def lastplay():

    email = request.args.get("email")
    book_id = request.args.get("bookId")

    return user_service.get_last_play(
        email=email,
        book_id=book_id
    )

@app.route("/setPlayTime")
def set_play_time():

    return jsonify(
        book_service.set_play_time(
            email=request.args.get("email"),
            book_id=request.args.get("bookId", type=int),
            file_num=request.args.get("fileNum", type=int),
            time=request.args.get("time", type=float)
        )
    )
