#!/usr/bin/python3
def no_c(my_string):
    lst = [x for x in my_string if x not in 'Cc']
    new_string =''.join(lst)
    return new_string
