#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import requests
import sys

if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print(f'Error code: {e.response.status_code}')
