from marshmallow import fields
from marshmallow import Schema, EXCLUDE


class FundInputSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    account_identifier = fields.Str(
        required=True
    )
    fund_identifier = fields.Str(
        required=True
    )
    fund_name = fields.Str(
        required=True
    )
    fund_description = fields.Str()
    currency_code = fields.Str(
        required=True
    )


class FundOutputSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    account_identifier = fields.Str(
        required=True
    )
    fund_identifier = fields.Str(
        required=True
    )
    fund_name = fields.Str(
        required=True
    )
    fund_description = fields.Str()
    currency_code = fields.Str(
        required=True
    )
