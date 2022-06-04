#!/usr/bin/python3
def no_c(my_string):
    stringAsList = []
    stringAsList[:0] = my_string
    for i in stringAsList:
        if i in "Cc":
            stringAsList.pop(stringAsList.index(i))
    return "".join(stringAsList)
