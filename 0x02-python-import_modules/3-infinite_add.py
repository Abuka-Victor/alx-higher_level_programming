#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv.pop(0)
    result = 0
    for i in argv:
        result += int(i)
    print(result)
