#!/usr/bin/python3.5
#定制类
class Student(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return 'Student object (name:%s)' % self.name
#定义好__str__返回一个好看的字符串
	__repr__ = __str__
#__repr__返回程序开发者看到的字符串，为调试服务
#__str__返回用户看到的字符串
s = Student('kobe')
s
print(s.name) #输出：kobe
print(s)
print(Student('kobe'))
#Student object (name:kobe)
#没有str与repr
#<__main__.Student object at 0xb7286fcc>
#<__main__.Student object at 0xb729018c>
