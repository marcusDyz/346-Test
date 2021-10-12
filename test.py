#! /usr/bin/python3

import requests
import passwords

user = passwords.user
password = passwords.password

r = requests.get("https://httpbin.org", auth=(user,password))
print(user)
print(password)
