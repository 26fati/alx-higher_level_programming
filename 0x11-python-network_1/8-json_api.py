#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    try:
        value = {'q': sys.argv[1]}
    except IndexError:
        value = {'q': ''}
    r = requests.post('http://0.0.0.0:5000/search_user', data=value)
    try:
        response = r.json()
        if response == {}:
            print('No result')
        else:
            print(f'[{response["id"]}] {response["name"]}')
    except ValueError:
        print("Not a valid JSON")
