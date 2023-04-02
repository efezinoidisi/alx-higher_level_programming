#!/usr/bin/python3
"""
This module contains script that uses the github api to display user id
"""
import requests
from sys import argv


def post_url():
    """
    sends a post request to a  url using the package requests
    """
    headers = {'Authorization': f'token {argv[2]}'}
    url = f'https://api.github.com/users/{argv[1]}'
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        data = res.json()
        print(data.get('id'))
    except requests.exceptions.HTTPError as err:
        print('None')


if __name__ == '__main__':
    post_url()
