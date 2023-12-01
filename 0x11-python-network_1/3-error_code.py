#!/usr/bin/python3
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys

req = Request(sys.argv[1])
try:
    with Request.urlopen(req) as response:
        print(response.read().decode("UTF-8"))
except HTTPError as e:
    print('Error code: ', e.code)