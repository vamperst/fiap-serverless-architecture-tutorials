import boto3
import json


def handler(event, context):
    print(json.dumps(event))
    