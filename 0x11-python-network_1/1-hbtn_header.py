#!/usr/bin/python3
"""
This module contains script that fetches a url passed as a
command line argument and displays the X-Request-Id variable found
in the header of the response
"""
import urllib.request
from sys import argv


def fetch_url():
    """
    fetch a url using the module urllib
    """
    request = urllib.request.Request(argv[1])
    with urllib.request.urlopen(request) as response:
        data = response.headers
        print(data['X-Request-Id'])


if __name__ == '__main__':
    fetch_url()
