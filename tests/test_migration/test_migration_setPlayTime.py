import requests


OLD_API = "http://192.168.1.93/newbooks/setPlayTime"
NEW_API = "http://192.168.1.93/papi/setPlayTime"

LAST_TIME_API = "http://192.168.1.93/newbooks/getLastTime"


def test_migration_set_play_time():

    # получаем текущее состояние
    last_play = requests.get(
        LAST_TIME_API,
        params={
            "email": "ychokov@gmail.com"
        }
    ).json()


    params = {
        "email": "ychokov@gmail.com",
        "bookId": last_play["bookid"],
        "fileNum": last_play["filenum"],
        "time": last_play["time"]
    }


    old_response = requests.get(
        OLD_API,
        params=params
    )

    new_response = requests.get(
        NEW_API,
        params=params
    )


    assert old_response.status_code == 200
    assert new_response.status_code == 200


    old_json = old_response.json()
    new_json = new_response.json()


    assert new_json["bookid"] == old_json["bookid"]
    assert new_json["name"] == old_json["name"]
    assert new_json["img"] == old_json["img"]
    assert new_json["filenum"] == old_json["filenum"]
    assert new_json["opened"] == old_json["opened"]

    assert abs(
        new_json["time"] - old_json["time"]
    ) < 0.001
