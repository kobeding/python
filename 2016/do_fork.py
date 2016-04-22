#!/usr/bin/python3.5
#fork()系统调用，调用一次返回两次（复制一份子进程）
#一个父进程可以fork出很多子进程，所以父进程需要记住每个子进程的ID
#而子进程只需要调用getppid()就可以拿到父进程的ID
#有了fork，一个进程在接到新任务时就可以复制出一个子进程来处理新任务
#apache服务器就是由父进程监听端口，子进程处理新的http请求
import os#os封装常见的系统调用

print('Process (%s) start ...' % os.getpid())
pid = os.fork()  #子进程永远返回0,父进程返回子进程的ID
if pid == 0:
	print('I am child process (%s) and my parent is %s.' % (os.getpid(),os.getppid()))
else:        #不为0,此时返回的是子进程的ID（pid）
	print('I (%s) just created a child process (%s).' % (os.getpid(),pid))
"""
Process (12768) start ...
I (12768) just created a child process (12769).
I am child process (12769) and my parent is 12768.
"""