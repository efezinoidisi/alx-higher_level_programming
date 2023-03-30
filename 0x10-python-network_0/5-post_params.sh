#!/bin/bash
# This script sends a POST request to the url passed
curl -s -X POST  -H "Content-Type: application/json" -d '{"email":"test@gmail.com", "subject":"I will always be here for PLD"}' "$1"
