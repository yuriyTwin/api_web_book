from compare import compare


def test_playbook():
    compare(
        "getPlayList",
        {
            "id": 954,
            "email": "ychokov@gmail.com"
        }
    )
