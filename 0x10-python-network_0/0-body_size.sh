#!/bin/bash
# a script to check the size of the body of the response
curl "$1" -w "%{size_download}\n" | tail -n 1
