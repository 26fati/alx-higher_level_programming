#!/usr/bin/python3
if __name__ == "__main__":
    '''a program that prints all the names defined
    by the compiled module hidden_4'''
    import hidden_4

    nmaes = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
