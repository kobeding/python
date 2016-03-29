#!/usr/bin/python3.4
#Filename: decorator.py

#关于装饰器:
import logging
logging.basicConfig(level = logging.INFO)

def add(a,b):
    return a + b
def checkParams(fn):
    def wrapper(a,b):
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
#检查参数是否为整形或浮点型
            return fn(a,b)
#是则通过fn返回计算结果
        logging.warning("variable 'a' and 'b' cannot be added")
        return
    return wrapper
#fn引用add，被封存在闭包的执行环境中返回
if __name__ == "__main__":
#将add函数对象传入，fn指向add
#等号左侧的add，指向checkParams的返回值wrapper
    add = checkParams(add)
    add(3,'hello')
    print(add(1,5))
