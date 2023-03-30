#!/bin/bash
# This script takes in a url, sends a request to that url

curl -w '%{size_download}\n' -o /dev/null -s "$1"
