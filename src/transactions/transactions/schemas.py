from marshmallow import fields
from marshmallow import Schema, EXCLUDE


class TransactionInputSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    account_identifier = fields.Str(
        required=True
    )
    category_identifier = fields.Str(
        required=True
    )
    category_name = fields.Str(
        required=True
    )
    transaction_action = fields.Integer(
        required=True
    )
    transaction_detail = fields.Str(
        required=True
    )
    transaction_amount = fields.Number(
        required=True
    )
    transaction_date = fields.Date(
        required=True,
        format='%Y-%m-%d'
    )


class TransactionOutputSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    account_identifier = fields.Str(
        required=True
    )
    category_identifier = fields.Str(
        required=True
    )
    category_name = fields.Str(
        required=True
    )
    transaction_identifier = fields.Str(
        required=True
    )
    transaction_action = fields.Integer(
        required=True
    )
    transaction_detail = fields.Str(
        required=True
    )
    transaction_amount = fields.Number(
        required=True
    )
    transaction_date = fields.Str(
        required=True
    )
