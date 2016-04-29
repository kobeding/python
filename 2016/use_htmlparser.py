#!/usr/bin/python3.5
#j解析HTML，HTMLParser可以很方便的解析HTML（文本，图像）
from html.parser import  HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
	def handle_starttag(self,tag,attrs):
		print('<%s>' % tag)

	def handle_endtag(self,tag):
		print('<%s>' % tag)

	def handle_startendtag(self,tag,attrs):
		print('<%s>' % tag)

	def handle_data(self,data):
		print(data)

	def handle_comment(self,data):
		print('<!--',data,'-->')

	def handle_entityref(self,name):
		print('&#%s;' % name)

	def handle_charref(self,name):
		print('&#%s;' % name)

parser = MyHTMLParser()
#feed()方法可以多次调用，HTML字符串可以分次放入
#特殊字符串有两种，一种是&nbsb，一种是&#1234，都可以通过Parser来解析
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
	<p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')