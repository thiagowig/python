import requests


def execute():
    url = "https://www.googleapis.com/gmail/v1/users/me/messages/send"

    payload = "{    \n   \"raw\": \"Q29udGVudC1UeXBlOiB0ZXh0L3BsYWluOyBjaGFyc2V0PSJ1cy1hc2NpaSIKTUlNRS1WZXJzaW9uOiAxLjAKQ29udGVudC1UcmFuc2Zlci1FbmNvZGluZzogN2JpdAp0bzogZGV2LnRoaWFnb0BnbWFpbC5jb20KZnJvbTogZ21haWwtMDJAY3JlZGVudGlhbC10ZXN0LTI1MDYxMi5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbQpzdWJqZWN0OiBUZXN0aW5nIHNvbWV0aGluZyBXRUlSRAoKCjxodG1sPgoKPGJvZHk-CiAgICBIaSBKYW1lcyBIZXRmaWVsZCEKICAgIEhvdyBhcmUgeW91Pwo8L2JvZHk-Cgo8L2h0bWw-\"\n}"
    headers = {
        'authorization': "Bearer ya29.c.Kl6CB5y6AKGMVlzFhhR_0aei4gPN-M0XKy8KCMPiBO4VLiA8qra0uJL6_dMjphCnJ_8j38jk-WmEhYPLMIbVuqSuRXLmPU5_BkX4pbgM1FYh66DGKwSK8ab8ngOXuxy6",
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "fe0c5754-d1c3-3f5f-324c-eeb59526b008"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

    return response.text


execute()