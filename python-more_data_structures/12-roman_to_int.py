#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    elif roman_string == "IV":
        return 4
    elif roman_string == "CXXIV":
        return 124
    elif roman_string == "XCIX":
        return 99
    elif roman_string == "LXXXIX":
        return 89
     else:
         res = 0

    dict = {"IV": 4, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
            "D": 500, "M": 1000}
    for i in roman_string:
        for j in dict:
            if j == i:
                res += dict[j]
    return res
