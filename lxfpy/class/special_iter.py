#!/usr/bin/python3.5
#一个类想被用于for...in循环，类似list和tuple，就必须实现一个__iter__()方法
#该方法返回一个迭代对象，不断调用__next__()方法直到Stop
class Fib(object):  #Fib类，可以用于for循环
	def __init__(self,n):  #不接收参数
		self.a , self.b = 0 , 1
		self.n = n
	def __iter__(self):
		return self  #实例本身就是迭代对象，故返回自己
	def __next__(self):
		self.a ,self.b = self.b ,self.a + self.b
		if self.a > self.n:  #100以内的Fib数
			raise StopIteration()
		return self.a
print(Fib(100))
#这一行输出这个:<__main__.Fib object at 0xb728506c>
for n in Fib(100):
	print(n,end=' ')