#!/usr/bin/python3
def no_c(my_string):
    new = list(my_string)
    for x in new:
        if x == 'c' or x == 'C':
            x == ''
    return new
