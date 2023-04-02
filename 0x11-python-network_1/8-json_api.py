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
    payload = {'q': argv[1] if len(argv) > 1 else ""}
    url = 'http://0.0.0.0:5000/search_user'
    try:
        res = requests.post(url, data=payload)
        res.raise_for_status()
        data = res.json()
        if data:
            print(f'[{data.get("id")}] {data.get("name")}')
        else:
            print('No result')
    except ValueError as err:
        print('Not a valid JSON')


if __name__ == '__main__':
    post_url()
