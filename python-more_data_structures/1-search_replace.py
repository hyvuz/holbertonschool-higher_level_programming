#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for elm in my_list:
        if elm == search:
            new_list.append(replace)
        else:
            new_list.append(elm)
    return new_list
