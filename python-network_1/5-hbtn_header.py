#!/usr/bin/python3
"""Script that takes a URL and displays the value of X-Request-Id using requests"""
import requests
import sys

response = requests.get(sys.argv[1])
print(response.headers.get('X-Request-Id'))
