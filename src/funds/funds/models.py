from pynamodb.attributes import UnicodeAttribute, BooleanAttribute

from apps.utils import constants as con
from apps.utils.models import BaseModel


class FundModel(BaseModel):
    """
    - pk: {PK_PREFIX}#{ACCOUNT_IDENTIFIER}
    - sk: {SK_PREFIX}#{FUND_ABBR}
    """

    class Meta:
        table_name = con.DYNAMODB_TABLE
        region = con.AWS_REGION

    PK_PREFIX = 'ACC'
    SK_PREFIX = 'FUN'

    account_identifier = UnicodeAttribute()
    fund_identifier = UnicodeAttribute()
    fund_name = UnicodeAttribute()
    fund_description = UnicodeAttribute(null=True)
    currency_code = UnicodeAttribute()
