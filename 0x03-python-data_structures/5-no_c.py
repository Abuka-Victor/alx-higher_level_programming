#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        stringAsList = [i for i in my_string if i not in "Cc"]
        return "".join(stringAsList)
    else:
        return my_string
