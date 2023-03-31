#!/usr/bin/python3
"""
This module contains script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


def fetch_hbtn():
    """
    fetch a url using the module urllib
    """
    request = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(request) as response:
        data = response.read()
        output = f"Body response:\n\t- type: {type(data)}"
        output2 = f"\n\t- content: {data}\n\t- utf8 "
        output3 = f"content: {data.decode('utf-8')}"
        print(output + output2 + output3)


if __name__ == '__main__':
    fetch_hbtn()
