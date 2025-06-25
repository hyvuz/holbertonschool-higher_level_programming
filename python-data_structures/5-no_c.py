#!/usr/bin/python3
def no_c(my_string):
    copy_string = ''
    for char in my_string:
        if char != chr(99) and char != chr(67):
            copy_string += char
    return copy_string
