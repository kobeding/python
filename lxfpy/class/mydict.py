#!/usr/bin/python3.5 
class Dict(dict):#Dict类，行为和dict一致，但是可以通过属性来访问
#d = Dict(a=1,b='test');d['a'] >>> 1   ;d.a  >>>  1

	def __init__(self,**kw):
		super().__init__(**kw)#调用父类的方法
#super() -> same as super(__class__,<first argument>)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r" 'Dict' object has no attribute '%s' " % key)
	def __setattr__(self,key,value):
		self[key] = value