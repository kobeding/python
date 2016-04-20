#!/usr/bin/python3.5
#读写功能有操作系统提供，请求操作系统打开一个文件对象（文件描述符）
#读写接口
from datetime import datetime

with open('text.txt','w') as f:#open()传入文件名和标识符
	f.write('today is :')
	f.write(datetime.now().strftime('%Y-%m-%d'))
#read()方法可以一次性读取文件的全部内容，读到内存，用str对象表示
with open('text.txt','r') as f:
	s = f.read()
	print('open for read ... ',s)
#open('xxxx','r/w/rb/wb',encoding='gbk',errors='ignore')
with open('text.txt','rb') as f:
	s = f.read()
	print('open as binary for read ... ',s)
#需调用f.close()方法关闭文件,保证全部写入，with自带，或者：
"""
read(size)反复调用，readline()调用配置文件很方便
for line in f.readline():
	print(line.strip())
---------
try:
	f = open('text.txt','r')
	print(f.read())
finally:
	if f:
		f.close()
"""