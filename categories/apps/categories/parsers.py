from typing import Any, Dict

from apps.utils import constants as con


def create_category(category: Dict[str, Any]) -> Dict[str, Any]:
    links = {
        'self': con.BASE_URL
    }
    data = {
        'type': 'categories',
        'id': category['category_identifier'],
        'attributes': category
    }
    payload = {
        'links': links,
        'data': data
    }
    return payload
