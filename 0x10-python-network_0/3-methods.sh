#!/bin/bash
# show methods
curl -I -L -s -X OPTIONS $1 | grep allow | tr -d 'allow: '
