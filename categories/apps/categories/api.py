import logging
from marshmallow import ValidationError

from apps.utils import (
    api as api_utils,
    responses as res_utils
)

from . import parsers as par
from . import services as ser
from .schemas import CategoryInputSchema, CategoryOutputSchema


def create_category(event, context):
    data = api_utils.get_data(event=event)

    try:
        attrs = CategoryInputSchema().load(data)
    except ValidationError as err:
        msg = f'create_category :: ValidationError :: {err.messages}'
        logging.error(msg)
        return res_utils.bad_request()

    category = ser.create_category(**attrs)
    category = CategoryOutputSchema().dump(category)
    body = par.create_category(category=category)

    return res_utils.created(body=body)
