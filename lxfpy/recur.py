#!/usr/bin/python3.5
#计算递归

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print('fact(1)=',fact(1))
print('fact(5)=',fact(5))
print('fact(9)=',fact(9))

def fact2(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num*product)
#尾递归，函数返回调用函数本身，return语句没有表达式，编译器或者解释器可以把尾递归做优化，使递归无论调用多少次，都只占用一个栈帧，不会出现栈溢出，把每一步的乘积传入到递归函数中。
print('fact(1)=',fact(1))
print('fact(5)=',fact(5))
print('fact(9)=',fact(9))

def move(n,a,b,c):
    if n == 1:
        print('move',a,'--->',c)
        return
    move(n-1,a,c,b)
    print('move',a,'--->',c)
    move(n-1,b,a,c)

move(3,'A','B','C')
print('--------------')
move(4,'A','B','C')

