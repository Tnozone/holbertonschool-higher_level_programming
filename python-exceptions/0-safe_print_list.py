#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb = 0
    try:
        for i in range(x):
            print("{:}".format(my_list[i]), end="")
            nb += 1
        print()
    except:
        print()
        return nb
    return nb
