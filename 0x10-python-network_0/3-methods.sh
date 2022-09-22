#!/bin/bash
# show methods
curl -si -X OPTIONS $1 | grep Allow | tr -d 'Allow: '
