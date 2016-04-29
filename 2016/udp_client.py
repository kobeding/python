#!/usr/bin/python3.5
import socket
#创建一个socket：
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#SOCK_DGRAM指定端口类型是UDP，绑定端口和tcp一样，但不需要listen()
#不需要调用connect()，直接发送数据给服务器:
for data in [b'kobe',b'james',b'wade']:
	#发送数据:
	s.sendto(data,('127.0.0.1',9999))
	#接受数据:
	print(s.recv(1024).decode('utf-8'))

s.close()