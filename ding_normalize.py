#!/usr/bin/python3.4 

from functools import reduce
L = ['adam','LISA','barT']
def normalize(L):
    return L[0].upper()+L[1:].lower()

s = map(normalize,L)
print(list(s))
