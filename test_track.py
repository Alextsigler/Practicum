# Циглер Александр, 8-я кагорта, инженер по тестированию плюс
import requests
import data
import configuration
from utils.orders import create_order


def test_track_response() -> None:
    order = create_order(body=data.order_body)
    track = order.get('track')
    assert track is not None, "Created order hasn't a track identifier."

    params = {'t': track}
    response = requests.get(f"{configuration.URL_SERVICE}{configuration.ORDER_TRACK_PATH}", params=params)
    assert response.status_code == 200, f"Invalid status code, track id={track}."