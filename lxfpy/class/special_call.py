#!/usr/bin/python3.5
#直接在实例本身上调用,而不是instance.method()
class Student(object):
	def __init__ (self,name):
		self.name = 'kobe'
		#self.score = score
	def __call__ (self,score):  #定义call方法,直接对实例进行调用
	#也可以定义参数,模糊实例与函数，对象与函数
		print('name is :%s,score is :%d ' %  (self.name,score))

s = Student('kobe')
s(99)#self不需要传入参数
#一般情况是s.get_score()之类的方法调用
print(callable(Student('kobe')))  #True
#判断一个对象是否可以被调用,输出：
#name is :kobe,score is :99 
#True

