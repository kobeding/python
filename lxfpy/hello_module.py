#!/usr/bin/python3.5
' a test module' #文档说明
__author__ = 'Kobe Ding' #作者说明
import sys 
def test():  #模块的attribute
	args = sys.argv  #sys中的那个模块
	#argv用list存储了命令行的所有参数
	#argv至少有一个元素，第一个参数永远是该.py的名称
	if len(args) == 1:
		print('Hello,World.')
#python3.5 hello_module.py --> sys.argv = ['hello_module']
#python3.5 hello_module.py  kobe--> sys.argv = ['hello_module','kobe']
	elif len(args) ==2:
		print(args[0])
		print('Hello,%s.' % args[1])
	else:
		print('too many arguments.')

if __name__ == '__main__':  #运行这个模块，默认名为这个
#其他地方导入，判断失败
#可以让一个模块通过命令行运行时执行一些额外的代码，运行测试
	print("test code in __main__")
	test()