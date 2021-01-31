import logging
from marshmallow import ValidationError

from apps.utils import (
    api as api_utils,
    responses as res_utils
)

from . import parsers as par
from . import services as ser
from .schemas import TransactionInputSchema, TransactionOutputSchema


def create_transaction(event, context):
    data = api_utils.get_data(event=event)

    try:
        attrs = TransactionInputSchema().load(data)
    except ValidationError as err:
        msg = f'create_transaction :: ValidationError :: {err.messages}'
        logging.error(msg)
        return res_utils.bad_request()

    transaction = ser.create_transaction(**attrs)
    transaction = TransactionOutputSchema().dump(transaction)
    body = par.create_transaction(transaction=transaction)

    return res_utils.created(body=body)
