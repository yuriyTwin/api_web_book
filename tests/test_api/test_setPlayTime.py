import requests
from helpers.schema_validator import validate_json


def test_set_play_time():

    email = "ychokov@gmail.com"
    API = "http://192.168.1.93/papi/getLastTime"

    # Получаем текущую книгу пользователя
    response = requests.get(
        API,
        params={
            "email": email
        }
    )

    assert response.status_code == 200

    last_play = response.json()

    # Вызываем setPlayTime с текущими данными
    response = requests.get(
        API,
        params={
            "email": email,
            "bookId": last_play["bookid"],
            "fileNum": last_play["filenum"],
            "time": last_play["time"]
        }
    )

    assert response.status_code == 200

    data = response.json()

    validate_json(
        data,
        "getLastTime"
    )

    assert data["bookid"] == last_play["bookid"]
    assert data["filenum"] == last_play["filenum"]
    assert data["opened"] == 1

    assert abs(data["time"] - last_play["time"]) < 0.001
