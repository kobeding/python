import threading
#创建全局Threadlocal对象:
#local_school是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响
#local_school是一个全局变量，但每个属性如local_school.student都是线程的局部变量
#可以任意读写而互补干扰，也不用管理锁问题ThreadLocal内部会处理
#理解local_school是一个dict，还可以绑定其他变量local_school.teacher等
global_dict = {}
#local_school = threading.local()
def process_student():
	#获取当前线程关联的student
	std = global_dict[threading.current_thread()]
	#std = local_school.student
	print('Hello,%s in (%s)' % (std,threading.current_thread().name))

def process_thread(s_name):
	#绑定ThreadLocal的student：
	std = s_name
	global_dict[threading.current_thread()] = std
	#local_school.student = name
	process_student()
#每个线程都只能读写自己线程的独立副本，互补干扰
t1 = threading.Thread(target=process_thread,args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()