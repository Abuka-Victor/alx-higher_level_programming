#!/bin/bash
# a script to check the size of the body of the response
curl -si 0.0.0.0:5000/catch_me -w "You got me!" | tail -n 1
