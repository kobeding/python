#!/usr/bin/python3.5

from multiprocessing import Pool
#利用multiprocessing的pool可以很方便的同时处理几百或者上千的并行操作，脚本的复杂度也大大降低
import os,time,random

def long_time_task(name):
	print('Run task %s (%s)...' % (name,os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name,end - start))
if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)#设定为4,所以task4要等待某个task执行完毕后才执行 默认是CPU核数
	for i in range(5):
		p.apply_async(long_time_task,args=(i,))
	print('waiting for all subprocesss done...')
	p.close()
	p.join()
#等待所有的子进程执行完毕，调用join()之前必须调用close()，close()之后就不能继续添加新的Process
#防止主进程在worker进程结束前结束
	print('All subprocesss done.')
"""
Parent process 14688.
waiting for all subprocesss done...
Run task 0 (14690)...
Run task 1 (14689)...
Run task 3 (14691)...
Run task 2 (14692)...
Task 2 runs 0.45 seconds.
Run task 4 (14692)...
Task 4 runs 0.44 seconds.
Task 3 runs 1.27 seconds.
Task 1 runs 1.34 seconds.
Task 0 runs 1.36 seconds.
All subprocesss done.
"""