#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    if roman_string and type(roman_string) == str:
        myDict = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
        for i in range(len(roman_string)):
            if i != (len(roman_string) - 1) and \
                    myDict[roman_string[i]] < myDict[roman_string[i + 1]]:
                result += int(myDict[roman_string[i + 1]] -
                              (myDict[roman_string[i + 1]] / 10))
                result -= myDict[roman_string[i + 1]]
            else:
                result += myDict[roman_string[i]]
    return result
