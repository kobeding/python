import logging
#内置logging模块可以非常容易的记录错误信息
def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:#可能出错的程序代码段
		bar('0')
	except Exception as e:
		logging.exception(e)
#try机制可以跨越多层调用，在合适层次去捕获错误就可以了
main()
print('END') #产生错误，END还是可以输出
"""
通过配置，logging可以把错误记错到日志文件里，方便事后排查
ERROR:root:division by zero
Traceback (most recent call last):
  File "err-logging.py", line 11, in main
    bar('0')
  File "err-logging.py", line 7, in bar
    return foo(s) * 2
  File "err-logging.py", line 4, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero
END
"""