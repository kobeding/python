#!/usr/bin/python3.4
#静态服务器:Apache/Nginx/Lighttpd/
#简单的Web应用,保存HTML文档,用现成的服务器软件,接受用户请求,从文件中读取HTML返回
#动态实现HTML,首先要实现底层代码(请求 响应 解析 http协议规范)
#底层代码有专门的服务器软件实现,python专注于生成HTML文档,编写Web业务
#WSGI：Web Server Gateway Interface
#只要求Web开发者实现一个函数，响应HTTP请求
#environ：一个包含所有HTTP请求信息dict对象;方便提取我们需要的数据,不需要对一大串字符做判断 截取
#start_response：一个发送HTTP响应的函数,调用这个函数,就发送了HTTP响应的Header
#Header只能发送一次,只能调用一次这个函数,其接受两个参数
#一个是HTTP响应码,一个是一组list表示的HTTP Header(两个str的tuple表示)
def application(environ,start_response):
	start_response('200 OK',[('Content_Type','text/html')])
	#固定的格式,接收我们需要返回的状态
	body = '<h1>Hello,%s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
	return [body.encode('utf-8')]
	#return [b'<h1>Hello,web!</h1>']
	#返回值作为HTTP响应的Body发送给浏览器
#如何从environ这个dict对象拿到HTTP请求信息，然后构造HTML;
#通过start_response()发送Header,最后返回Body。
#无论多么复杂的web应用程序，入口都是一个WSGI处理函数
#HTTP请求的所有输入信息可以通过environ获得
#http响应的所有输出可以通过start_response()加上函数返回值作为Body
# application()关注的是：request的内容是什么，需要response的内容是什么