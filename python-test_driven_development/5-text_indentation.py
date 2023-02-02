#!/usr/bin/python3
""" module documentation """


def text_indentation(text):
    """ seperates lines function """

    if type(text) is not str:
        raise TypeError("text must be a string")

    tab = [".", "?", ":"]
    tex = []

    for i in text:
        if i == " " and tex and tex[-1] in tab:
            continue
        tex.append(i)
    for i in range(len(tex)):
        if tex[i] in tab:
            print(tex[i], end="\n\n")
        else:
            print(tex[i], end="")
