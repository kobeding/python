#!/usr/bin/python3.5
#数据读写不一定是文件，也可以在内存中读写
from io import StringIO

f = StringIO()#创建StringIO，然后像文件一样写入
f.write('hello')
 #print(f.write('hello')) 输出：5
f.write(' ')
f.write('world')
print(f.getvalue())#getvalue()方法用于获得写入后的str

f = StringIO('hello!\nhi!\nthanks!\nbye!\n')
print(f.read())
"""
readlines()有点问题，输出是空格？？！
for line in f.readlines():
	print(line)
“”“