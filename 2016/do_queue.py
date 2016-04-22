#!/usr/bin/python3.5
#进程间通信通过Queue，Pipes等多种方法来交换数据
#multiprocessing（跨平台多进程）需要模拟出fork()的效果
#父进程所有python对象都必须通过pickle序列化再传到子进程
#在window下调试失败，是不是考虑pickle失败了
#进程接收的参数都是序列化后传过来的，如果参数无法序列化，就无法传送
#建议使用int  str 等基本类型做参数
from multiprocessing import Process,Queue
import os,time,random
#写数据进程的执行代码
def write(q):
	print('Process to write :%s'  % os.getpid())
	for value in ['A','B','C']:
		print('put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())
#读数据进程的执行代码
def read(q):
	print('Process to read: %s ' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)

if  __name__ == '__main__':
	#父进程创建Queue，并传给各个子进程：
	q = Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	#创建两个子进程，用于读写
	#启动子进程pw，写入：
	pw.start()
	#启动子进程pr，读取：
	pr.start()
	#等待pw结束：
	pw.join()
	#pr进程是死循环，无法等待其介绍，只能强行终止：
	pr.terminate()
"""
Process to write :17648
put A to queue...
Process to read: 17649 
Get A from queue.
put B to queue...
Get B from queue.
put C to queue...
Get C from queue.
"""