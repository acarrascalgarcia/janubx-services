from typing import Any, Dict, Optional

from .models import CurrencyModel


def create_currency(
        *,
        currency_code: str,
        currency_name: str
) -> Dict[str, Any]:
    pk = f'{CurrencyModel.PK_PREFIX}'
    sk = f'{CurrencyModel.SK_PREFIX}#{currency_code}'

    attrs = {
        'pk': pk,
        'sk': sk,
        'currency_code': currency_code.upper(),
        'currency_name': currency_name.upper()
    }
    currency = CurrencyModel(**attrs)
    currency.save()

    result = dict(currency)
    return result
