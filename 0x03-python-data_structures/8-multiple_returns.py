#!/usr/bin/python3
def multiple_returns(sentence):
    len1 = len(sentence)
    char = sentence[0]
    if len1 < 0:
        char = None
    return (len1, char)
