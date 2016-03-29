#!/usr/bin/python3.4 

from functools import reduce
L = [1,2,3,4,5]
def prod(x,y):
    return x*y
s = reduce(prod,L)
print(s)
