#!/usr/bin/python3.5
#__getattr()__:动态的返回一个属性
class Student(object):
	def __init__ (self):
		self.name = 'kobe'

	def __getattr__ (self,attr): #调用不存在，会试图调用这个来尝试获取属性
		if attr == 'score':
			return 99
		if attr == 'age':
			return lambda:25  #返回函数也是完全可以的
		raise AttributeError(" Student() object has no attribute '%s'  "%  attr )
#把一个类的所有属性的调用方法都动态化处理了，不需要任何特殊手段
#可以针对完全动态的情况做调用
s = Student()
print(s.name)
print(s.score)
print(s.age())  #调用方式要改变，是函数的调用方式
print(s.grade)
#raise AttributeError(" Student() object has no attribute '%s'  % attr ")
#AttributeError:  Student() object has no attribute '%s'  % attr