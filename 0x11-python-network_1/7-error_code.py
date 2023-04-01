#!/usr/bin/python3
"""
This module contains script that takes in a URL, sends a get request
to the URL and displays the body of the response
"""
import requests
from sys import argv


def handle_error():
    """
    sends a post request to a  url using the package
    requests and handles http errors
    """
    try:
        res = requests.get(argv[1])
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.HTTPError as err:
        code = err.response.status_code
        if code >= 400:
            print(f'Error code: {code}')


if __name__ == '__main__':
    handle_error()
