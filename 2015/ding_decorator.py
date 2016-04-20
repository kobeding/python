import functools


def log(func):

    def wrapper(*args,**kw):
        print('call %s()' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log  #log放在now()定义处，相当与执行了语句now = log(now)
  	#log接收函数参数，返回函数
def now():
    print('2016-1-20')

print(now)
now()
now()  #只有调用函数才能打印出结果
