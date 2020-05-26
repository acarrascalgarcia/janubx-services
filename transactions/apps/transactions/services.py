from datetime import date
from decimal import Decimal
from typing import Any, Dict
from uuid import uuid4

from .models import TransactionModel


def create_transaction(
        *,
        account_identifier: str,
        category_identifier: str,
        transaction_action: int,
        transaction_detail: str,
        transaction_amount: Decimal,
        transaction_date: date,
        category_name: str
) -> Dict[str, Any]:
    formatted_date = transaction_date.strftime('%Y-%m-%d')
    pk = f'{TransactionModel.PK_PREFIX}#{account_identifier}'
    sk = f'{TransactionModel.SK_PREFIX}#{formatted_date}'
    lsi = f'{TransactionModel.LSI_PREFIX}#{category_identifier}'

    transaction_identifier = uuid4().hex

    attrs = {
        'pk': pk,
        'sk': sk,
        'lsi': lsi,
        'account_identifier': account_identifier,
        'category_identifier': category_identifier,
        'category_name': category_name.upper(),
        'transaction_identifier': transaction_identifier,
        'transaction_action': transaction_action,
        'transaction_detail': transaction_detail.upper(),
        'transaction_amount': transaction_amount,
        'transaction_date': formatted_date
    }
    transaction = TransactionModel(**attrs)
    transaction.save()

    result = dict(transaction)
    return result
