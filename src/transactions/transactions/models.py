from pynamodb.attributes import (
    UnicodeAttribute, BooleanAttribute,
    UTCDateTimeAttribute, NumberAttribute
)
from pynamodb.indexes import LocalSecondaryIndex, AllProjection

from apps.utils import constants as con
from apps.utils.models import BaseModel, PKMixin


class TransactionLSIIndex(LocalSecondaryIndex, PKMixin):
    """
    - pk: {PK_PREFIX}#{ACCOUNT_IDENTIFIER}
    - lsi: {LSI_PREFIX}#{CATEGORY_IDENTIFIER}
    """

    class Meta:
        projection = AllProjection()

    lsi = UnicodeAttribute(range_key=True)


class TransactionModel(BaseModel):
    """
    - pk: {PK_PREFIX}#{ACCOUNT_IDENTIFIER}
    - sk: {SK_PREFIX}#{TRANSACTION_DATE}#{TRANSACTION_IDENTIFIER}
    """

    class Meta:
        table_name = con.DYNAMODB_TABLE
        region = con.AWS_REGION

    PK_PREFIX = 'ACC'
    SK_PREFIX = 'TRA'
    LSI_PREFIX = 'CAT'

    account_identifier = UnicodeAttribute()
    category_identifier = UnicodeAttribute()
    transaction_identifier = UnicodeAttribute()
    transaction_action = NumberAttribute(default=0)
    transaction_detail = UnicodeAttribute()
    transaction_amount = NumberAttribute()
    transaction_date = UnicodeAttribute()
    category_name = UnicodeAttribute()
    lsi_index = TransactionLSIIndex()
    lsi = UnicodeAttribute()
