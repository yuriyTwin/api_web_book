from compare import compare


def test_books():
    compare(
        "getBookList",
        {
            "email": "ychokov@gmail.com"
        }
    )
