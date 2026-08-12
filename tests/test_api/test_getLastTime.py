import requests

from helpers.schema_validator import validate_json


def test_get_last_time():

    response = requests.get(
        "http://192.168.1.93/papi/getLastTime?email=ychokov@gmail.com"
    )

    assert response.status_code == 200

    validate_json(
        response.json(),
        "getLastTime"
    )
