#!/usr/bin/python3.5
#多任务可以有多进程完成，也可以由一个进程内的多个线程完成
#线程是操作系统直接支持的执行单元，高级语言通常都内置多线程支持
#python是真正的posix thread，不是模拟出来的线程
import time,threading
#提供两个模块_thread--低级模块,threading--高级模块（对_thread进行了封装）
def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n = 0
	while  n <5 :
		n = n+1
		print('thread %s >>> %s' % (threading.current_thread().name,n))
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop,name='loopThread')
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
#任何进程默认启动一个线程，主线程，然后又可以启动新的线程
#threading.current_thread()--永远返回当前线程的实例
#不起名字，就是thread-1,thread-2,没有其他意义
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
"""
thread MainThread is running...
thread loopThread is running...
thread loopThread >>> 1
thread loopThread >>> 2
thread loopThread >>> 3
thread loopThread >>> 4
thread loopThread >>> 5
thread loopThread ended.
thread MainThread ended.
"""