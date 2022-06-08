#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = my_list.copy()
    for i in newList:
        if i == search:
            newList[newList.index(search)] = replace
    return newList
