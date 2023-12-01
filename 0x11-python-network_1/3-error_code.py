#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import urllib.request
from urllib.error import HTTPError
import sys

req = urllib.request.Request(sys.argv[1])
try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("UTF-8"))
except HTTPError as e:
    print('Error code: ', e.code)
