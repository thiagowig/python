import requests
from google.oauth2 import service_account
from email.mime.text import MIMEText
import base64
from base64 import urlsafe_b64encode
import urllib3
import json


URL = "https://www.googleapis.com/gmail/v1/users/me/messages/send"

def execute(request):
    token = generate_token("service_account.json")
   
    #content = request.get_json()["content"]
    content = "My Message"

    #payload = generate_message(content)
    payload = "{    \n   \"raw\": \"Q29udGVudC1UeXBlOiB0ZXh0L3BsYWluOyBjaGFyc2V0PSJ1cy1hc2NpaSIKTUlNRS1WZXJzaW9uOiAxLjAKQ29udGVudC1UcmFuc2Zlci1FbmNvZGluZzogN2JpdAp0bzogZGV2LnRoaWFnb0BnbWFpbC5jb20KZnJvbTogZ21haWwtMDJAY3JlZGVudGlhbC10ZXN0LTI1MDYxMi5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbQpzdWJqZWN0OiBUZXN0aW5nIHNvbWV0aGluZyBXRUlSRAoKCjxodG1sPgoKPGJvZHk-CiAgICBIaSBKYW1lcyBIZXRmaWVsZCEKICAgIEhvdyBhcmUgeW91Pwo8L2JvZHk-Cgo8L2h0bWw-\"\n}"
    headers = {
        'authorization': f"Bearer {token}",
        'content-type': "application/json"
    }

    response = requests.request("POST", URL, data=payload, headers=headers)

    print(f"#### Response: {response.content}")

    return response.text

def generate_message(content):
    message = MIMEText(content)
    message['to'] = "dev.thiago@gmai.com"
    message['from'] = "gmail-02@credential-test-250612.iam.gserviceaccount.com"
    message['subject'] = "Mail test"
    encoded_message = urlsafe_b64encode(message.as_bytes())
    print(f"### ENcoded message: {encoded_message.decode()}")

    return json.dumps({'raw': encoded_message.decode()})


def generate_token(serviceAccount: str) -> str:
    """
    Generate the token from service account key file.
    """
    credentials = service_account.Credentials.from_service_account_file(serviceAccount, scopes=["https://www.googleapis.com/auth/gmail.send"], subject="gmail-02@credential-test-250612.iam.gserviceaccount.com")
    credentials.refresh(urllib3.PoolManager().request)

    print(f"#### Credential: {credentials.token}")

    return credentials.token


execute(None)    