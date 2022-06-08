#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = a_dictionary.copy()
    for i in newDict:
        newDict[i] *= 2
    return newDict
