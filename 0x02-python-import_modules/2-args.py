#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv.pop(0)
    if argv:
        if len(argv) == 1:
            print("1 argument:")
            print("1: {}".format(argv[0]))
        else:
            print("{} arguments:".format(len(argv)))
            for i in range(len(argv)):
                print("{}: {}".format(i + 1, argv[i]))
    else:
        print("0 arguments.")
