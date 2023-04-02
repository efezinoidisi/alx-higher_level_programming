#!/usr/bin/python3
"""
This module contains script that uses the github api to display 10 commits
from a github repository. The repo name and owner name are passed
as command line arguments
"""
import requests
import sys


def get_commits():
    """
    sends a post request to a  url using the package requests
    """
    owner = sys.argv[2]
    repo = sys.argv[1]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
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
