#!/bin/bash
# This script takes in a url, sends a request to that url
curl -w '%{http_code}' -o /dev/null -s "$1"
