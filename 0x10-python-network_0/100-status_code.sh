#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL, and displays the status code of the response.
curl -s -o -w '%{http_code}' "$1"
