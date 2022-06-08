#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    newDict = a_dictionary.copy()
    for i in sorted(newDict):
        print(f"{i}: {newDict[i]}")
