#!/usr/bin/python3
""" Module for task 0 """


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
