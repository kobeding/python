#!/usr/local/bin/python3.5
# Filename:func_doc.py

def printMax(x,y):
    '''Docstrings xxxxxx

    Test xxxxxx.'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x,'is max')
    else:
        print(y,'is max')
printMax(3,5)
print(printMax.__doc__)
help(printMax)
