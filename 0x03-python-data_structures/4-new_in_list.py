#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    for i in my_list:
        new_list.append(i)
    if idx > (len(my_list) - 1) or idx < 0:
        return new_list
    else:
        new_list[idx] = element
        return new_list
