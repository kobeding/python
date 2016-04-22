#!/usr/bin/python3.5

from multiprocessing import Process 
#跨平台版本的多进程模块，Prccess类代表一个进程对象

import os

#子进程要执行的代码
def run_proc(name):
	print('Run child process %s (%s) ...' % (name,os.getpid()))

if __name__ == '__main__':
	print('Parent process %s.'  % os.getpid())
	p = Process(target=run_proc,args=('test',))
#创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例
	p.start()#用start()方法启动
	p.join()#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
	print('Chill process end.')
"""
Parent process 13631.
Run child process test (13634) ...
Chill process end.
"""