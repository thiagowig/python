import os
import requests
import urllib

AUTH_HOST = os.environ["AUTH_HOST"]

users_file = open('users.txt', 'r')
users_lines = users_file.readlines()

for username in users_lines:
    username = username.replace('\n', '')
    username = urllib.parse.quote(username)
    print(f"\nUsername: {username}")

    for attempt in range(7):
        print(f"Attempt: {attempt + 1}")
        url = f"{AUTH_HOST}/oauth/token?grant_type=password&username={username}&password=invalid_password"

        requests.post(url)
