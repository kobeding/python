#!/usr/bin/python3.5
#关于调试，简单粗暴，用print()把可能的问题变量都打印出来
#断言：assert代替print，断言失败，抛出AssertionError
def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!'
	return 10 / n

def main():
	foo('0')

main()
"""
python3.5 -0 do_assert.py 关闭assert,关闭后当作pass语句处理
Traceback (most recent call last):
  File "do_assert.py", line 12, in <module>
    main()
  File "do_assert.py", line 10, in main
    foo('0')
  File "do_assert.py", line 6, in foo
    assert n != 0, 'n is zero!'
AssertionError: n is zero!
"""