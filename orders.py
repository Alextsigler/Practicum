import requests
import data
import configuration


def create_order(body: dict) -> dict:
    url = f'{configuration.URL_SERVICE}{configuration.ORDER_PATH}'
    response = requests.post(url, json=body, headers=data.headers)
    response.raise_for_status()
    return response.json()