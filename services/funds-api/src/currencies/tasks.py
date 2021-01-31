import csv
from typing import NoReturn

from apps.utils import constants as con
from . import services as ser


def populate_currencies(
        *,
        filename: str
) -> NoReturn:
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=con.CSV_DELIMITER)
        for row in reader:
            area = ser.create_currency(**row)
            # TODO: Add logging
            print(f" * area {area['currency_code']} created")
