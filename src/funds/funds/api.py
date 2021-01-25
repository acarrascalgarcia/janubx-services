import logging
from marshmallow import ValidationError

from apps.utils import (
    api as api_utils,
    responses as res_utils
)

from . import parsers as par
from . import services as ser
from .schemas import FundInputSchema, FundOutputSchema


def create_fund(event, context):
    data = api_utils.get_data(event=event)

    try:
        attrs = FundInputSchema().load(data)
    except ValidationError as err:
        msg = f'create_fund :: ValidationError :: {err.messages}'
        logging.error(msg)
        return res_utils.bad_request()

    fund = ser.create_fund(**attrs)
    fund = FundOutputSchema().dump(fund)
    body = par.create_fund(fund=fund)

    return res_utils.created(body=body)
