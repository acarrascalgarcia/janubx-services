from datetime import datetime

from pynamodb.attributes import (
    UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute
)
from pynamodb.models import Model


class PKMixin:
    pk = UnicodeAttribute(
        hash_key=True
    )


class BaseModel(Model, PKMixin):
    class Meta:
        abstract = True

    sk = UnicodeAttribute(
        range_key=True
    )

    is_active = BooleanAttribute(
        default=True
    )
    created_at = UTCDateTimeAttribute(
        default=datetime.now()
    )
    updated_at = UTCDateTimeAttribute()

    def save(self, conditional_operator=None, **expected_values):
        self.updated_at = datetime.now()
        super(BaseModel, self).save()

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))
