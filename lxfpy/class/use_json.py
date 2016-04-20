#!/usr/bin/python3.5
#将PYTHON对象变为JSON,标准化格式,不同语言传递对象
import json
d = dict(name='bob',age=20,score=98)
data = json.dumps(d)
print('JSON Data is a str:',data)
#JSON Data is a str: {"score": 88, "age": 20, "name": "bob"}
#dumps返回一个str,内容就是标准的JSON,类似的,可以直接写入文件
with open('dump.txt','w') as f:
	k = json.dump(d,f)
print(k)  #输出是None
#然后反序列化
reborn = json.loads(data)
print(reborn)
#{'score': 88, 'age': 20, 'name': 'bob'}
with open('dump.txt','r') as f:
	p = json.load(f)
print(p) 
#{'score': 88, 'age': 20, 'name': 'bob'}
#dict -->  {}  定义class对象，Student类然后序列化
class Student(object):

	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score

	def __str__(self):
		return 'Student object (%s,%s,%s)' % (self.name,self.age,self.score)

s = Student('Bob',20,88)

std_data = json.dumps(s,default=lambda obj: obj.__dict__)
#json.dumps(.../....)提供很多参数，定制JSON的{}对象default是一个可选参数
#任意的class实例变为dict(default=lambda obj: obj.__dict__)
#通常class的实例都有个__dict__属性，就是一个dict，用来存储实例变量
#例外：__slot__的class  ??
print('Dump Student:',std_data)
#Dump Student: {"score": 88, "age": 20, "name": "Bob"}
rebuild = json.loads(std_data,object_hook=lambda d: Student(d['name'],d['age'],d['score']))
#loads方法首先转换出一个dict对象
#object_hook函数负责把dict转换为Student实例
print(rebuild)
#Student object (Bob,20,88)