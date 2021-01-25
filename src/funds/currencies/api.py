import logging
from marshmallow import ValidationError

from apps.utils import (
    api as api_utils,
    responses as res_utils
)

from . import parsers as par
from . import services as ser
from .schemas import CurrencyInputSchema, CurrencyOutputSchema


def create_currency(event, context):
    data = api_utils.get_data(event=event)

    try:
        attrs = CurrencyInputSchema().load(data)
    except ValidationError as err:
        msg = f'create_currency :: ValidationError :: {err.messages}'
        logging.error(msg)
        return res_utils.bad_request()

    currency = ser.create_currency(**attrs)
    currency = CurrencyOutputSchema().dump(currency)
    body = par.create_currency(currency=currency)

    return res_utils.created(body=body)
