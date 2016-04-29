#!/usr/bin/python3.5
import socket
#创建一个socket：
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
#SOCK_DGRAM指定端口类型是UDP，绑定端口和tcp一样，但不需要listen()
#直接接收来自任何客户端的数据:
s.bind(('127.0.0.1',9999))
print('Bind UDP on 9999...')
while True:
	#接收数据:
	data,addr = s.recvfrom(2014)
	#recvfrom()方法返回数据和客户端的地址与端口
	#服务器收到数据后 直接调用sendto()就可以把数据发送给客户端
	print('Received from %s:%s.' % addr)
	#s.sendto(b'Hello,%s' % data ,addr)
	reply = 'Hello,%s!' % data.decode('utf-8')
	s.sendto(reply.encode('utf-8'),addr)