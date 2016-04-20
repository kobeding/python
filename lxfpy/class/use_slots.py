#!/usr/bin/python3.5

class  Student(object):
	#__slots__ = ('name','age','score') #tuple定义允许绑定的属性名称
	def __init__ (self,name,age):
		self.name = name
		self.age = age
	def set_score(self,score):
		self.score = score
class GraduateStudent(Student):
	pass

s = Student('kobe',20)  #创建类实例
s.name = 'Michael' 
s.age = 20 #绑定属性，有限制，所以不能输出
print("s.age=",s.age)
try:
	s.number = 99
except AttributeError as e:
	print('AttributeError:',e)
g = GraduateStudent('wade',30)
g.score = 80 #给实例绑定一个属性，其他同类实例不能调用
print("g.score=",g.score)

def set_age(self,age):
	self.age = age
from types import MethodType
g.set_age = MethodType(set_age,g)
#给一个实例绑定方法(另一个实例不能用)
g.set_age(25)
print("g.age=",g.age)

def set_score(self,score):
#类中之前限定了只有name更age，所以score加不进去
	self.score = score
Student.set_score = MethodType(set_score,Student)
#给Student绑定方法后，所有的实例均可调用
s.set_score(10)
print("s.score=",s.score)
g.set_score(20)
print("g.score=",g.score)
	
