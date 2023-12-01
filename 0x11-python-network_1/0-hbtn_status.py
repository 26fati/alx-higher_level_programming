#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print('Body response:')
        print(f'\t- type: {type(html)}')
        print(f'\t- content: {html}')
        data = html.decode("UTF-8")
        print(f'\t- utf8 content: {data}')
