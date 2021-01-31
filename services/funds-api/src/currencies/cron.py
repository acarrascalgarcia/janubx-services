# import logging

from apps.utils import constants as con
from apps.utils.storage import S3Config, S3Connector

from . import tasks as tas


# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)


def populate_currencies(event, context):
    config = S3Config(bucket_name=con.SETUP_BUCKET)
    connector = S3Connector(config=config)

    source = 'base/currencies.csv'
    destination = '/tmp/currencies.csv'
    ok = connector.download(source=source, destination=destination)

    if ok:
        tas.populate_currencies(filename=destination)
