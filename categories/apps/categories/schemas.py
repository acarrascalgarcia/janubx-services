from marshmallow import fields
from marshmallow import Schema, EXCLUDE


class CategoryInputSchema(Schema):
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
    category_description = fields.Str()


class CategoryOutputSchema(Schema):
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
    category_description = fields.Str()
