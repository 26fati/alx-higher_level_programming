#!/usr/bin/python3
"""displays the value of
the X-Request-Id variable found in the header of the response
using requests library.
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
