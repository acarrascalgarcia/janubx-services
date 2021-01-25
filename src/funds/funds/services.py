from typing import Any, Dict, Optional

from .models import FundModel


def create_fund(
        *,
        account_identifier: str,
        fund_identifier: str,
        fund_name: str,
        currency_code: str,
        fund_description: Optional[str] = None
) -> Dict[str, Any]:
    pk = f'{FundModel.PK_PREFIX}#{account_identifier}'
    sk = f'{FundModel.SK_PREFIX}#{fund_identifier}'

    attrs = {
        'pk': pk,
        'sk': sk,
        'account_identifier': account_identifier,
        'fund_identifier': fund_identifier,
        'fund_name': fund_name.upper(),
        'currency_code': currency_code.upper()
    }
    if fund_description is not None:
        attrs['fund_description'] = fund_description.upper()
    fund = FundModel(**attrs)
    fund.save()

    result = dict(fund)
    return result
