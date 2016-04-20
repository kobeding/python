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
        @functools.wraps(func)   #wrapper() 前面需加上这个
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@logger('DEBUG')   #传入参数
def today():
    print('2016-1-20')

today()   #相当与执行 today = logger('DEBUG')(today)
#首先执行logger('DEBUG'),返回decorator函数，再调用返回的函数，参数是now函数
#最终返回的是wrapper函数。
print(today.__name__)
#输出是today(本来是wrapper)
#但内置functools.wraps
#wrapper.__name__ = func.__name__  ??
#