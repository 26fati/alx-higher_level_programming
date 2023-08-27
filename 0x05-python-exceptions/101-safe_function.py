#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as ex:
        sys.stderr.write("Exception: {}\n".format(ex))
        result = None
    return (result)
