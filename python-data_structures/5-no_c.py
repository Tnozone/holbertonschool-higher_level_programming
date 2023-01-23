#!/usr/bin/python3
def no_c(my_string):
    tab = [x for x in my_string[:] if x != "c" and x != "C"]
    str = ""
    for i in tab:
        str += i
    return str
