#!/usr/bin/python3
"""
This module contains script that fetches a url and handles HTTP error
"""
import urllib.request
from sys import argv
from urllib.error import HTTPError


def handle_error():
    """
    fetch a url using the module urllib and handle error
    """
    request = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            data = response.read().decode('utf-8')
    except HTTPError as err:
        print(f'Error code: {err.code}')


if __name__ == '__main__':
    handle_error()
