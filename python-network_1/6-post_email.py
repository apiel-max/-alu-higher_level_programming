#!/usr/bin/python3
"""Script that sends a POST request with email and displays response using requests"""
import requests
import sys

response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
print(response.text)
