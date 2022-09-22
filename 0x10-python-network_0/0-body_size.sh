#!/bin/bash
# a script to check the size of the body of the response
if (($# == 1)); then
	curl -s $1 -w "%{size_download}\n" | tail -n 1
fi
