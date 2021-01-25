from marshmallow import fields
from marshmallow import Schema, EXCLUDE


class CurrencyInputSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    currency_code = fields.Str(
        required=True
    )
    currency_name = fields.Str(
        required=True
    )


class CurrencyOutputSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    currency_code = fields.Str(
        required=True
    )
    currency_name = fields.Str(
        required=True
    )
