class FooError(ValueError):
	pass
#抛出错误，捕捉到一个错误就是捕获到该class的一个实例
#自己编写函数也可以抛出错误
def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value:%s' % s)
	return 10 / n

foo('0')
main()
print('END') #产生错误，END不能输出
"""
Traceback (most recent call last):
  File "err_raise.py", line 11, in <module>
    foo('0')
  File "err_raise.py", line 8, in foo
    raise FooError('invalid value:%s' % s)
__main__.FooError: invalid value:0
"""