#!/usr/bin/python3.4
# Filename: generator_fix.py

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n+1
x = int(input('please input a number:'))
fib(x)
