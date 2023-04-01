#!/usr/bin/python3
"""
This module contains script that sends a POST request to a url passed as a
command line argument and displays the body of the response
"""
import urllib.request
from sys import argv
import urllib.parse


def post_url():
    """
    fetch a url using the module urllib
    """
    value = {'email': argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    request = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(request) as response:
        content = response.read().decode('utf-8')
        print(content)


if __name__ == '__main__':
    post_url()
