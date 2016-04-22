#!/usr/bin/python3.5
#多进程中同一个变量，各自有一份拷贝存在每个进程中，互不影响
#多线程中所有变量都由所有线程共享，任何变量可以被任何线程修改
#共享数据最大的危险在于多个线程同时改变一个变量
import time,threading

balance = 0
lock = threading.Lock()#创建锁

def change_it(n):
	global balance#赋值语句
	balance = balance + n
	balance = balance - n
#在cpu执行时分布：计算，存储在临时变量中，赋值给balance
#修改balance需要多条语句，执行时，线程可能中断，从而导致多个线程把同一个对象改乱了
#因此要上锁，等待锁释放，锁只有一个，同一个时刻只有一个线程持有该锁
def run_thread(n):
	for i in range(100000):
		#change_it(n)
		
		#要先获取锁:
		lock.acquire()#多个线程同时执行时，只有一个线程能成功获取锁，然后继续执行代码，
						#其他线程需继续等待直到获得锁为止
		try:
			change_it(n)
		finally:
			#改完了要释放锁
			lock.release()
#try...finally确保锁一定会得到释放		
t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
"""
锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行
坏处当然也很多，首先是阻止了多线程并发执行
包含锁的某段代码实际上只能以单线程模式执行
效率就大大地下降了。其次，由于可以存在多个锁
不同的线程持有不同的锁，并试图获取对方持有的锁时
可能会造成死锁，导致多个线程全部挂起
既不能执行，也无法结束，只能靠操作系统强制终止。
"""
