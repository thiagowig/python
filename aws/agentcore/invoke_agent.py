import boto3
import json

client = boto3.client('bedrock-agentcore', region_name='us-east-1')
payload = json.dumps( {"prompt": "Explain machine learning in simple terms"})

response = client.invoke_agent_runtime(
    agentRuntimeArn='',
    runtimeSessionId='dfmeoagmreaklgmrkleafremoigrmtesogmtrskhmtkrlshmt',  # Must be 33+ chars
    payload=payload
)
response_body = response['response'].read()
response_data = json.loads(response_body)
print("Agent Response:", response_data)