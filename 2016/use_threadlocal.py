#!/usr/bin/python3.5
#多线程，每个线程使用自己的局部变量比使用全局变量好，全局变量要加锁
#局部变量在函数调用的时候传递比较麻烦
"""
def process_thread(name):
	#std是局部变量，但每个函数都需要使用，故必须传入
	std = Student(name)
	do_task_1(std)
	do_task_2(std)
#用全局变量？不行，每个线程处理不同的Student对象，不能共享
def do_task_1(std):
	do subtask_11(std)
	do subtask_12(std)

def do_task_2(std):
	do subtask_21(std)
	do subtask_22(std)
#或用全局dict存放所有Student对象
#然后以thread自身作为key获得线程对应的Student对象
gobal_dict = {}

def std_thread(name):
	std = Student(name)
	#将std放在全局dict中
	gobal_dict[threading.current_thread()] = std
	do_task_1(std)
	do_task_2(std)

def do_task_1(std):
	#不传入std，而是根据当前线程查找
	std = gobal_dict[threading.current_thread()]
	...
def do_task_2(std):
	#任何函数都可以查找出当前线程的std变量
	std = gobal_dict[threading.current_thread()]
	...
"""
#ThreadLocal最常用在为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等
#这样一个线程所有调用到的处理函数都可以非常方便的访问这些资源
import threading
#创建全局Threadlocal对象:
local_school = threading.local()
#local_school是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响
#local_school是一个全局变量，但每个属性如local_school.student都是线程的局部变量
#可以任意读写而互补干扰，也不用管理锁问题ThreadLocal内部会处理
#理解local_school是一个dict，还可以绑定其他变量local_school.teacher等

def process_student():
	#获取当前线程关联的student
	std = local_school.student
	print('Hello,%s in (%s)' % (std,threading.current_thread().name))

def process_thread(name):
	#绑定ThreadLocal的student：
	local_school.student = name
	process_student()
#每个线程都只能读写自己线程的独立副本，互补干扰
t1 = threading.Thread(target=process_thread,args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
"""
Hello,Alice in (Thread-A)
Hello,Bob in (Thread-B)
"""