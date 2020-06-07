from os import getenv

AWS_REGION = 'us-east-1'
BASE_URL = getenv('BASE_URL')
CSV_DELIMITER = ';'
DYNAMODB_HOST = 'https://dynamodb.eu-central-1.amazonaws.com'
DYNAMODB_TABLE = getenv('DYNAMODB_TABLE')
SETUP_BUCKET = getenv('SETUP_BUCKET')
