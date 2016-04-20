#!/usr/bin/python3.5 
import unittest

from mydict import Dict

class TestDict(unittest.TestCase):#编写一个测试类,注意继承关系
	def setUp(self):
		print('setUp...')

	def tearDown(self):
		print('tearDown...')
#两个特殊的方法,每调用一次测试方法的前后分别被执行
#连接数据库，关闭数据库，不必在每个测试方法中重复相同代码	
	def test_init(self):#以test开头的方法才是测试方法，才能被执行
		d = Dict(a=1,b='test')
		self.assertEqual(d.a,1)#最常用的断言方法
		#self.assertEqual(abs(-1),1):断言函数返回结果与1相等
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))
#unittest,TestDict提供很多内置的条件判断，只需要调用这些方法就可以断言输出是否是我们所期望的
	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d['key'],'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d.key,'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']
	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
#另一种重要的断言，期待抛出指定类型的Error
			value = d.empty

if __name__ == '__main__':#这里可以把mydict_test.py当作正常的python脚本运行
	unittest.main()#python3.5 mydict_test.py 
#或者：python3.5 -m unittest mydict_test 直接运行单元测试
#推荐做法，一次批量运行很多单元测试，有工具可以自动运行这些单元测试