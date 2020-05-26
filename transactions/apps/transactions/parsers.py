from typing import Any, Dict

from apps.utils import constants as con


def create_transaction(transaction: Dict[str, Any]) -> Dict[str, Any]:
    links = {
        'self': con.BASE_URL
    }
    data = {
        'type': 'transactions',
        'id': transaction['transaction_identifier'],
        'attributes': transaction
    }
    payload = {
        'links': links,
        'data': data
    }
    return payload
