#!/usr/bin/python3
"""
This module contains script that takes in a URL, sends a post request
to the URL and displays the body of the response
"""
import requests
from sys import argv


def post_url():
    """
    sends a post request to a  url using the package requests
    """
    payload = {'email': argv[2]}
    request = requests.post(argv[1], data=payload)
    print(request.text)


if __name__ == '__main__':
    post_url()
