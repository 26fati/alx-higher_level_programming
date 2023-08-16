#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or (type(roman_string) is not str):
        return 0

    result = 0
    length = len(roman_string)
    if length == 1:
        return dic[roman_string]
    for i in range(0, length-1):
        s1 = dic[roman_string[i]]
        s2 = dic[roman_string[i + 1]]
        if s1 < s2:
            result = result - s1
        else:
            result = result + s1
    return result + s2
