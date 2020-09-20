from typing import Optional

import boto3
from botocore.exceptions import ClientError
from botocore.response import StreamingBody
from boto3.resources.base import ServiceResource

from .constants import SETUP_BUCKET


def get_object_body_from_s3(
    *,
    key: str,
    bucket: Optional[str] = None,
) -> StreamingBody:

    bucket = bucket or cons.SETUP_BUCKET

    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, key)
    body = obj.get()['Body']

    return body
