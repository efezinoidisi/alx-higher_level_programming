#!/bin/bash
# This script sends a POST request to the url passed
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
