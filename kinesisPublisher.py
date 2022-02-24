import json
import boto3
import uuid
import random
from datetime import datetime

client = boto3.client('kinesis')

def lambda_handler(event, context):
    # TODO implement
    for i in range(10):
        date_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        print(date_time)
        unique_id = str(uuid.uuid4())
        value = random.randint(0, 100)
        payload = {
            'id': unique_id,
            'datetime': date_time,
            'value': str(value)
        }
        print(payload)
        response = client.put_record(
            StreamName = 'my-data-stream',
            Data=json.dumps(payload),
            PartitionKey=unique_id
        )
        print(response)
        response2 = client.put_record(
            StreamName = 'my-data-stream-2',
            Data=json.dumps(payload),
            PartitionKey=unique_id
        )
        print(response2)