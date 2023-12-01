#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=value)
    print(r.text)
