from typing import Any, Dict

from apps.utils import constants as con


def create_currency(currency: Dict[str, Any]) -> Dict[str, Any]:
    links = {
        'self': con.BASE_URL
    }
    data = {
        'type': 'currencies',
        'id': currency['currency_code'],
        'attributes': currency
    }
    payload = {
        'links': links,
        'data': data
    }
    return payload
