#!/bin/bash
# This script sends a GET request to the url with a header variable
curl -H "X-School-User-Id: 98" "$1"
