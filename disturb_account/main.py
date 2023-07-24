import os
import requests

AUTH_HOST = os.environ["AUTH_HOST"]

users_file = open('users.txt', 'r')
users_lines = users_file.readlines()

for username in users_lines:
    username = username.replace('\n', '')
    print("\nUsername: " + username)

    for attempt in range(7):
        print("Attempt: " + str(attempt + 1))
        url = AUTH_HOST + "/oauth/token?grant_type=password&username=" + username + "&password=invalid_password"

        requests.post(url)
