#!/usr/bin/python3.5
#操作文件，目录，内置os模块可以直接调用操作系统提供的接口函数
from datetime import datetime
import os
print(os.name) #操作系统类型--->posix
print(os.uname) #详细系统信息---><built-in function uname>
print(os.environ) #环境变量---->environ....
print(os.environ.get('PATH'))#获取某个环境变量
pwd = os.path.abspath('.')#查看当前目录的绝对路径
#/home/kobe/duv/python/lxfpy/class
#os.path.join(pwd,'testdir')
#将两个路径合并为一个,正确处理不同操作系统的路径分割符
#os.path.split(‘/home/kobe/duv/python/lxfpy/class/testdir’),拆分，后一部分总是最后级别的目录或者文件名
#os.path.splitext('xxxxx')--->得到文件扩展名('/xx/xx/xx','.txt')
#拆分合并函数不要求目录文件真的存在，只是对字符串进行操作
#os.rename('text.txt','text.py')
#os.remove('xxx')
#shutil模块提供copyfile()复制文件
os.mkdir('/home/kobe/duv/python/lxfpy/class/testdir')
os.rmdir('/home/kobe/duv/python/lxfpy/class/testdir')
print([x for x in os.listdir('.') if os.path.isdir(x)]) #找目录
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.txt'])#找特定的扩展名文件
#mkdir不能重复创建
#编写一个类似ls -l的输出程序
print('      Size   Last Modified      Name')
print('-----------------------------------------------------------')

for f in os.listdir(pwd):
	fsize = os.path.getsize(f)
	mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
	flag = '/' if os.path.isdir(f) else ' '
	print("%10d   %s   %s%s" % (fsize,mtime,f,flag))
