from urllib import request,parse
#urllib的request模块可以很方便的抓取URL内容，发送一个GET请求到制定页面，返回HTTP响应：
#get
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
	data = f.read()
	print('Status:',f.Status,f.reason)
	for k,v in f.getheaders():
		print('%s:%s' % (k,v))
	print('Data:',data.decode('utf-8'))
#advanced get:
req = request.Request('https://www.douban.com/')
req.add_header('User-Agent','Mozilla/6.0()')