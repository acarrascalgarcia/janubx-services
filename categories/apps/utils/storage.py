import logging
from typing import Union

import boto3
from botocore.exceptions import ClientError
from boto3.resources.base import ServiceResource


class Storage:

    def copy(self, *, source: str, destination: str) -> bool:
        raise NotImplementedError

    def download(self, *, source: str, destination: str) -> bool:
        raise NotImplementedError

    def move(self, *, source: str, destination: str) -> bool:
        raise NotImplementedError

    def remove(self, *, source: str) -> bool:
        raise NotImplementedError

    def upload(self, *, source: str, destination: str) -> bool:
        raise NotImplementedError

    def log(
            self,
            *,
            operation: str,
            input: str,
            output: str,
            level: str = None
    ) -> Union[None]:
        logger = logging.getLogger(__name__)
        default = 'info'

        level = level or default

        log_data = {
            'operation': operation,
            'input': input,
            'output': output,
            'source': type(self).__name__
        }

        _method = getattr(logger, level, default)
        _method(log_data)


class S3Config:

    def __init__(self, *, bucket_name: str):
        self._bucket_name = bucket_name

    def get_connection(self) -> ServiceResource:
        connection = boto3.resource('s3')
        return connection

    @property
    def bucket_name(self):
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, value):
        ...


class S3Connector(Storage):

    def __init__(self, *, config: S3Config):
        self.config = config

    def __enter__(self):
        self.connection = self.config.get_connection()
        return self.connection

    def __exit__(self, exception_type, exception_value, traceback):
        ...

    def copy(
            self,
            *,
            source: str,
            destination: str,
            destination_bucket_name: str = None
    ) -> bool:
        input = f'copy from {source} to {destination}'
        output = 'ok'

        with self as connector:
            bucket = connector.Bucket(self.config.bucket_name)

            if destination_bucket_name is not None:
                input = (
                    f'copy from {self.config.bucket_name}/{source} to'
                    f' {destination_bucket_name}/{destination}'
                )

                bucket = connector.Bucket(destination_bucket_name)

            source = {
                'Bucket': self.config.bucket_name,
                'Key': source
            }
            try:
                bucket.copy(source, destination)
            except Exception:
                self.log(
                    operation='copy',
                    input=input,
                    output=output,
                    level='exception'
                )
                return False

        self.log(operation='copy', input=input, output=output)
        return True

    def download(self, *, source: str, destination: str) -> bool:
        input = f'download from {source} to {destination}'
        output = 'ok'

        with self as connector:
            bucket = connector.Bucket(self.config.bucket_name)
            try:
                bucket.download_file(source, destination)
            except ClientError:
                output = "source file doesn't exist"
                self.log(
                    operation='get',
                    input=input,
                    output=output,
                    level='exception'
                )
                return False

        self.log(operation='get', input=input, output=output)
        return True

    def move(self, *, source: str, destination: str) -> bool:
        input = f'move from {source} to {destination}'
        output = 'ok'

        self.copy(source=source, destination=destination)
        self.remove(source=source)

        self.log(operation='rename', input=input, output=output)
        return True

    def remove(self, *, source: str) -> bool:
        input = f'remove {source}'
        output = 'ok'

        with self as connector:
            bucket = connector.Bucket(self.config.bucket_name)
            bucket.delete_objects(
                Delete={
                    'Objects': [
                        {
                            'Key': source
                        }
                    ]
                }
            )

        self.log(operation='remove', input=input, output=output)
        return True

    def upload(
            self,
            *,
            source: str,
            destination: str,
            **kwargs
    ) -> bool:
        input = f'upload from {source} to {destination}'
        output = 'ok'

        with self as connector:
            bucket = connector.Bucket(self.config.bucket_name)
            bucket.upload_file(source, destination, **kwargs)

        self.log(operation='put', input=input, output=output)
        return True
