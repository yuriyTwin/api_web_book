import requests

from helpers.schema_validator import validate_json


def test_serarch_books():

    response = requests.get(
        "http://192.168.1.93/papi/serarchBooks?search=%D1%81%D1%82%D1%80%D0%B0%D1%88%D0%BD%D1%8B%D0%B9%20%D0%B7%D0%B2%D0%B5%D1%80%D1%8C&email=ychokov@gmail.com"
    )

    assert response.status_code == 200

    validate_json(
        response.json(),
        "array_books"
    )
