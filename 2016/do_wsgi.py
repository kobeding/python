#!/usr/bin/python3.4
#静态服务器:Apache/Nginx/Lighttpd/
#简单的Web应用,保存HTML文档,用现成的服务器软件,接受用户请求,从文件中读取HTML返回
#动态实现HTML,首先要实现底层代码(请求 响应 解析 http协议规范)
#底层代码有专门的服务器软件实现,python专注于生成HTML文档,编写Web业务
#WSGI：Web Server Gateway Interface：数据抽象的模块
#web server和html之间的一个处理程序,更方便的获取想要的数据
#内置WSGI服务器模块msgiref
#负责启动WSGI服务器,加载application()函数
from wsgiref.simple_server import make_server
from hello import application
#创建一个服务器，IP地址为空，端口是8000,处理函数是application
httpd = make_server('',8000,application)
print('Serving HTTP on port 8000...')
#开始监听HTTP请求:
httpd.serve_forever()
#无论多么复杂的web应用程序，入口都是一个WSGI处理函数
#HTTP请求的所有输入信息可以通过environ获得
#http响应的所有输出可以通过start_response()加上函数返回值作为Body
"""
def application(environ, start_response):
	method = environ['REQUEST_METHOD']
	path = environ['PATH_INFO']
	if method=='GET' and path=='/':
		return handle_home(environ, start_response)
	if method=='POST' and path='/signin':
		return handle_signin(environ, start_response)
...
比较麻烦,需要更高级的web框架，专注于用一个函数处理一个URL
至于URL到函数的映射，则交给web框架来做;
"""
