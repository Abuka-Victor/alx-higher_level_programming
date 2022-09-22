#!/bin/bash
# show methods
curl -si -X OPTIONS 0.0.0.0:5000/route_4 | grep Allow | cut -c 8-
