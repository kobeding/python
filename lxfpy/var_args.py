#!/usr/bin/python3.5

def hello(greeting,*args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s,%s!' % (greeting,',' .join(args)))

hello('hi')
hello('hi','kobe')
hello('hello','kobe','james','wade','rose')

names = ('kobe','james')
hello('hello',*names)
