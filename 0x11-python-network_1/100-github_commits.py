#!/usr/bin/python3
"""This module contains the get_commits function"""
import requests
from sys import argv


def get_commits():
    """Lists 10 commits from a github repository using the github"""
    _, repo, owner = argv
    url = f'https://api.github.com/repos/{owner}/{repo}/commits?per_page=10'
    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        for item in data:
            sha = f"{item.get('sha')}: "
            name = f"{item.get('commit').get('author').get('name')}"
            print(sha + name)
    except requests.exceptions.HTTPError as err:
        pass


if __name__ == '__main__':
    get_commits()
