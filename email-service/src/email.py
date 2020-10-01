import logging
import os
import json
from http import HTTPStatus
import boto3

sqs = boto3.client('serverless')
queue_url = os.environ["EMAIL_QUEUE_URL"]

def handle(event, context):
    
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=event["body"]
    )

    logging.info(f"Message {response['MessageId']} sent to Queue.")

    return Response(HTTPStatus.ACCEPTED).json()
