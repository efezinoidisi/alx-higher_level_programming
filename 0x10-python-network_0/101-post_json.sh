#!/bin/bash
# This script sends a POST request to the url passed
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
