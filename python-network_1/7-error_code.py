#!/usr/bin/python3
"""Script that sends a request and displays error code if status >= 400"""
import requests
import sys

response = requests.get(sys.argv[1])
if response.status_code >= 400:
    print("Error code: {}".format(response.status_code))
else:
    print(response.text)
