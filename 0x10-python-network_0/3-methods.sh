#!/bin/bash
# Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sIX OPTIONS "$1" | grep "Allow" | cut -d ' ' -f 2- | head -2 | tail -1
