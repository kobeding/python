#!/usr/bin/python3.5
#表现的像list那样按照下标取值，需要实现__getitem()__方法
class Fib(object):
	def __getitem__ (self,n):
		if isinstance(n,int):
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a  #按照下标访问数列的任意一项
#__getitem__()传入的参数可能是一个list,也可能是一个slice,所以需要判断
#才能正确的执行不同的参数类型,从而得到想要的结果
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			#print(start)
			#print(stop)
			if start is None:
				start = 0
			a ,b = 1,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b,a+b
			return L
#还没有对[::2]step参数作出处理,也没负数作出处理
#定制多功能型,dict,ket,__delitem__()方法等
#动态语言的鸭子类型,不需要强制继承某个接口
f = Fib()             
print(f[0])
print(f[5])
print(f[10])
print(f[0:5])  #start=0,stop=5
print(f[:11])  #start=None,stop=11
"""
1
8
89
[1, 1, 2, 3, 5]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55,89]"""