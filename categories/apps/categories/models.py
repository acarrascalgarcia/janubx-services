from pynamodb.attributes import UnicodeAttribute, BooleanAttribute

from apps.utils import constants as con
from apps.utils.models import BaseModel


class CategoryModel(BaseModel):
    """
    - pk: {PK_PREFIX}#{ACCOUNT_IDENTIFIER}
    - sk: {SK_PREFIX}#{CATEGORY_ABBR}
    """

    class Meta:
        table_name = con.DYNAMODB_TABLE
        region = con.AWS_REGION

    PK_PREFIX = 'ACC'
    SK_PREFIX = 'CAT'

    account_identifier = UnicodeAttribute()
    category_identifier = UnicodeAttribute()
    category_name = UnicodeAttribute()
    category_description = UnicodeAttribute(null=True)
