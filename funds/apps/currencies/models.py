from pynamodb.attributes import UnicodeAttribute, BooleanAttribute

from apps.utils import constants as con
from apps.utils.models import BaseModel


class CurrencyModel(BaseModel):
    """
    - pk: {PK_PREFIX}
    - sk: {SK_PREFIX}#{CURRENCY_CODE}
    """

    class Meta:
        table_name = con.DYNAMODB_TABLE
        region = con.AWS_REGION

    PK_PREFIX = 'CUR'
    SK_PREFIX = 'CUR'

    currency_code = UnicodeAttribute()
    currency_name = UnicodeAttribute()
