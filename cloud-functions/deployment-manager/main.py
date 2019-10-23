import base64
import json

def execute(event, context):
    message = decode_message(event)

    print(message)


def decode_message(event):
    return json.loads(base64.b64decode(event['data']).decode('utf-8'))