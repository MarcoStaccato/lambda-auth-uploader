import json
import boto3
import uuid
from botocore.exceptions import ClientError
import logging



def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    try:
        logger.info(event)
        bucket_name = "your-bucket-name-goes-here"
        object_name = str(uuid.uuid1())
        fields = {}
        conditions = []
        # upload should occur within an hour
        expiration = 60 * 60

        body = json.loads(event['body'])

        response = s3_client.generate_presigned_post(bucket_name, object_name, fields, conditions, expiration)
        json_response = str(json.dumps(response))

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json_response
        }
    except ClientError as e:
        # Send some context about this error to Lambda Logs
        logger.info(e)
        raise e

