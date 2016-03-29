#!/usr/bin/python3.5
#函数参数练习

def power1(x):
    return x*x
print(power1(5))

def power2(x,n):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s
print(power2(5,3))
#位置参数，调用函数时，传入的值按照位置顺序依次赋值

def power3(x,n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s
print(power3(5))
#默认参数n=2,输入一个参数时，简化函数调用（默认在后）降低函数调用难度
def enroll(name,gender,age=6,city='beijing'):
    print('name:',name)
    print('age:',age)
    print('gender:',gender)
    print('city:',city)
print(enroll('kobe','F'))
print(enroll('james','F',30))
print(enroll('wade','F',city='miami'))

def add_end1(L=[]):
    L.append('END')
    return L
print(add_end1([1,2,3]))
print(add_end1(['x','y','z']))
print(add_end1())
print(add_end1())
print(add_end1())
print(add_end1([1,2]))
print(add_end1())
print(add_end1([1,2]))
#默认参数L是一个变量，指向对象[]，每次调用，改变了默认参数内容
#所以，默认参数必须指向不变对象

def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end2())
print(add_end2())

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc(1,2,3))
print(calc(1,2,3,4))
print(calc())
nums = [1,2,3]
print(calc(*nums))
#python允许在list或者tuple前加*,吧list与tuple元素变成参数传入函数

def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('kobe',37)
person('james',30,city='CAL')
person('wade',32,gender='M',job='basketball player')
#关键字参数，扩展函数功能，先组装一个dict，然后将dict转换关键字参数
extra = {'city':'miami','job':'basketball player'}
person('wade',32,**extra)
#kw获得的是extra的一个拷贝

#命名关键字参数，限制关键字参数
def person2(name,age,*,city,job):
    print(name,age,city,job)
person2('jack',24,city='beijing',job='engineer')
#命名关键字参数必须传入参数名，没有传入参数名将报错
def person2(name,age,*,city='beijing',job):
    print(name,age,city,job)
person2('jack',24,job='engineer')
#可以有缺省值，从而简化调用
#必选，默认，可变/命名关键字，关键字（顺序）
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
print(f1(1,2))
print(f1(1,2,c=3))
print(f1(1,2,3,'a','b'))
print(f1(1,2,3,'a','b',x=99,y=88))
print(f2(1,2,d=99,x=88,ext=None,))
#注意给*赋值的方式（'a','b'）和给**复制的方式（x=88）
args = (1,2,3,4)
kw = {'d':99,'x':'#'}
f1(*args,**kw)
args=(1,2,3)
kw = {'d':88,'y':'##'}
f2(*args,**kw)
#args按顺序赋值，通过一个tuple和dict，可以调用函数将参数传入
#对于任意函数，可以通过类似func(*args,**kw)的形式调用它，无论参数是如何定义的
