import json
import base64

def lambda_handler(event, context):
    # TODO implement
    print(event)
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])
        print(payload)
