#!/usr/bin/python3.4
#Filename: decorator.py

#关于装饰器:
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2016-1-20')

now()

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2016-1-20')

today()
print(today.__name__)
