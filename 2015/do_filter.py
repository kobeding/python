#!/usr/bin/python3.4
# Filename: do_filter.py

def is_odd(n):
    return n % 2 == 1

L = range(100)
print(list(filter(is_odd,L)))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['A',' ','B',None,'C',''])))