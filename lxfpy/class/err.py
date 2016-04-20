def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	bar('0')

main()
print('END')  #产生错误，END不会输出
"""
调用堆栈，错误一直往上抛，直到被python解释器捕获打印输出
Traceback (most recent call last):
  File "err.py", line 10, in <module>
    main()
  File "err.py", line 8, in main
    bar('0')
  File "err.py", line 5, in bar
    return foo(s) * 2
  File "err.py", line 2, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero
"""