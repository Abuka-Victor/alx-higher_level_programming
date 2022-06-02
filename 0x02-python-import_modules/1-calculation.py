#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    for i, j in [(add, "+"), (sub, "-"), (mul, "*"), (div, "/")]:
        print("{} {} {} = {}".format(a, j, b, i(a, b)))
