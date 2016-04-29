#!/usr/bin/python3.5

import socket
#创建一个socket：
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#AF_INET指定使用IPv4协议(AF_INET6)
#SOCK_STREAM指定使用面向流的TCP协议
#建立连接：
s.connect(('www.sina.com.cn',80))
#服务器，标准端口号，connect接收一个tuple参数
#发送数据：
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#接收数据：
buffer = []
while True:
	#每次最多接受1k字节:
	d = s.recv(1024)
	#调用recv(max)方法接收数据，循环中反复接收，直至返回空数据接收完毕
	if d:
		buffer.append(d)
	else:
		break
data = b' '.join(buffer)
#关闭连接:
s.close()
#分离HTTP头(打印)和网页内容(保存到文件)
header ,html = data.split(b'\r\n\r\n',1)#指定分隔符，分隔的子字符串个数
print(header.decode('utf-8'))
#把接收的数据写入文件:
with open('sina.html','wb') as f:
	f.write(html)