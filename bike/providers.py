import requests
from bike.lib.constans import API_BIKE_SANTIAGO
from typing import Any, Dict, List, Optional, Tuple
from bike.models import Stations, Extra


def get_bike_data_stations():
    response = requests.get(API_BIKE_SANTIAGO)
    stations = response.json()['network']['stations']
    return stations


def create_bike_extra(data: Dict[str, Any]) -> Extra:
    extra = Extra.objects.filter(uid=data.get('uid')).first()
    if not extra:
        bike_extras = Extra(
            address=data.get('address',''),
            altitude=data.get('altitude'),
            ebikes=data.get('ebikes'),
            has_ebikes=data.get('has_ebikes'),
            last_updated=data.get('last_updated'),
            normal_bikes=data.get('normal_bikes'),
            payment=data.get('payment'),
            payment_terminal=data.get('payment-terminal'),
            post_code=data.get('post_code',''),
            renting=data.get('renting'),
            returning=data.get('returning'),
            slots=data.get('slots'),
            uid=data.get('uid'),
        )
        bike_extras.save()
        return bike_extras
    return None


def create_bike_stations(extra: Extra, data: Dict[str, Any]) -> Stations:
    station = Stations.objects.filter(id_api=data.get('id')).first()
    if not station:
        bike_stations = Stations(
            empty_slots=data.get('empty_slots'),
            extra=extra,
            free_bikes=data.get('free_bikes'),
            id_api=data.get('id'),
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
            name=data.get('name'),
            timestamp=data.get('timestamp'),
        )
        bike_stations.save()
        return bike_stations
    return None
