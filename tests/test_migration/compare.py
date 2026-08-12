import json
import requests

PHP_URL = "http://chnemo.asuscomm.com/newbooks"
PY_URL = "http://192.168.1.93/papi"



def get_json(url, params):
    r = requests.get(url, params=params)

    print(f"\nGET {r.url}")
    print(f"Status: {r.status_code}")

    r.raise_for_status()

    return r.json()


def compare(endpoint, params=None):
    php = get_json(f"{PHP_URL}/{endpoint}", params)
    py = get_json(f"{PY_URL}/{endpoint}", params)

    if php != py:
        print("\n========== PHP ==========")
        print(json.dumps(php, indent=2, ensure_ascii=False))

        print("\n========== PYTHON ==========")
        print(json.dumps(py, indent=2, ensure_ascii=False))

    assert php == py, f"Mismatch in endpoint {endpoint}"
