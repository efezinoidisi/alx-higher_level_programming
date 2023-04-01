#!/usr/bin/python3
"""
This module contains script that takes in a URL, sends a request
to the URL and displays the value of the  variable X-Request-Id
in the response header
"""
import requests
from sys import argv


def fetch_url():
    """
    fetch a url using the package requests
    """
    request = requests.get(argv[1])
    print(request.headers['X-Request-Id'])


if __name__ == '__main__':
    fetch_url()
