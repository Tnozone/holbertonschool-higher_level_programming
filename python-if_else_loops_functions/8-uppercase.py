#!/usr/bin/python3
def uppercase(str):
    for i in str:
        caract = ord(i)
        if ord(c) >= 97 and ord(c) <= 122:
            caract = caract - 32
        print("{:c}".format(caract), end='')
    print()
