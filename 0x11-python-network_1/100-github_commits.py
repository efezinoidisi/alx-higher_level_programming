#!/usr/bin/python3
"""
This module contains script that uses the github api to display 10 commits
from a github repository. The repo name and owner name are passed
as command line arguments
"""
import requests
from sys import argv


def get_commits():
    """
    sends a post request to a  url using the package requests
    """
    headers = {'Authorization': f'token {argv[2]}'}
    url = f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        for i in range(10):
            sha = f"{data[i].get('sha')}: "
            name = f"{data[i].get('commit').get('author').get('name')}"
            print(sha + name)
    except requests.exceptions.HTTPError as err:
        print('None')


if __name__ == '__main__':
    get_commits()
