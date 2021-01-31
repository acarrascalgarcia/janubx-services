from typing import Any, Dict, Optional

from .models import CategoryModel


def create_category(
        *,
        account_identifier: str,
        category_identifier: str,
        category_name: str,
        category_description: Optional[str] = None
) -> Dict[str, Any]:
    pk = f'{CategoryModel.PK_PREFIX}#{account_identifier}'
    sk = f'{CategoryModel.SK_PREFIX}#{category_identifier}'

    attrs = {
        'pk': pk,
        'sk': sk,
        'account_identifier': account_identifier,
        'category_identifier': category_identifier,
        'category_name': category_name.upper()
    }
    if category_description is not None:
        attrs['category_description'] = category_description.upper()
    category = CategoryModel(**attrs)
    category.save()

    result = dict(category)
    return result
