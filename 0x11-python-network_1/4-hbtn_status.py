#!/usr/bin/python3
"""
This module contains script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


def fetch_hbtn():
    """
    fetch a url using the package requests
    """
    request = requests.get('https://alx-intranet.hbtn.io/status')
    request = request.text
    output = f"Body response:\n\t- type: {type(request)}"
    output2 = f"\n\t- content: {request}"
    print(output + output2)


if __name__ == '__main__':
    fetch_hbtn()
