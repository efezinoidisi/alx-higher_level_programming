#!/bin/bash
# This script sends a delete request to the url
curl -s -i -X OPTIONS "$1" | grep 'Allow' | sed -e 's/Allow: //'
