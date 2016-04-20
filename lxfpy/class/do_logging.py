#!/usr/bin/python3.5 
#logging不会抛出错误，而且可以输出到文件，终极调试武器！！！
import logging
#logging允许你指定记录信息的级别，debug，info，warning，error
logging.basicConfig(level=logging.INFO)#c此时logging.debug不起作用
#logging还可以通过不同的配置，输出到不同的地方
s = '0'
n = int(s)
logging.info('n = %d ' % n)
print(10 / n)
"""
不加logging.basicConfig(level=logging.INFO)的输出：
Traceback (most recent call last):
  File "do_logging.py", line 9, in <module>
    print(10 / n)
ZeroDivisionError: division by zero
-----
INFO:root:n = 0 
Traceback (most recent call last):
  File "do_logging.py", line 9, in <module>
    print(10 / n)
ZeroDivisionError: division by zero
"""