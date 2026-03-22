#!/bin/bash
# Sends a GET request with header X-HolbertonSchool-User-Id set to 98 and displays the body
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
