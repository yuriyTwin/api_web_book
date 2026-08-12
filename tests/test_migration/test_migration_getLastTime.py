from compare import compare


def test_lastplay():
    compare(
        "getLastTime",
        {
            "email": "ychokov@gmail.com"
        }
    )
