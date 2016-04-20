#!/usr/bin/python3.4
# 关于返回函数:
#看的不是很明白
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,3,4,5,6,7,8,9)
print(f)
print("----")
print(f())

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
#count函数运行完之后，fs=[f,f,f],此时i=3
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())

def count2():
    fs = []
    def f(n):
        def j():
            return n*n
        return j
    for i in range(1,4):
        fs.append(f(i))  #f(i)立即被执行，因此i的当前值被传入f()
    return fs
#fs = [f(1),f(2),f(3)]
f1,f2,f3 = count2()
print(f1())
print(f2())
print(f3())
