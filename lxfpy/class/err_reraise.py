
def foo(s):
	n = int(s)
	if n == 0:
		raise ValueError('invalid value:%s' % s)#这里有一个抛出错误

	return 10 / n

def bar():
	try:
		foo('0')
	except ValueError as e:#这里有一个捕获错误，打印输出
		print('ValueError!')
		raise#raise语句不带参数，将错误原样抛出
	except ZeroDivisionError:
		raise ValueError('intput error!')
		#把一种类型的错误转化为另一种类型，要是合理的转换逻辑
bar()
print('END') #产生错误，END不会输出
"""
捕获的目的只是记录一下，方便后续追踪，当前函数不知道怎么处理该错误
继续上抛，让顶层调用者去处理
ValueError!
Traceback (most recent call last):
  File "err_reraise.py", line 14, in <module>
    bar()
  File "err_reraise.py", line 10, in bar
    foo('0')
  File "err_reraise.py", line 5, in foo
    raise ValueError('invalid value:%s' % s)
ValueError: invalid value:0
"""