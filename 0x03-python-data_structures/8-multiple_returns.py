#!/usr/bin/python3
def multiple_returns(sentence):
    len1 = len(sentence)
    if len1 == 0:
        return (0, None)
    else:
        return (len1, sentence[0])
