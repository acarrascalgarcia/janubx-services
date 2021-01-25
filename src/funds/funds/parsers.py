from typing import Any, Dict

from apps.utils import constants as con


def create_fund(fund: Dict[str, Any]) -> Dict[str, Any]:
    links = {
        'self': con.BASE_URL
    }
    data = {
        'type': 'funds',
        'id': fund['fund_identifier'],
        'attributes': fund
    }
    payload = {
        'links': links,
        'data': data
    }
    return payload
