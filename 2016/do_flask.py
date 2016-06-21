#!/usr/bin/python3.4
#处理3个URL（/   GET /signin  POST /signin）
from flask import Flask
from flask import request

app = Flask(__name__)
#用装饰器在内部自动的把URL和函数关联起来
@app.route('/',methods=['GET','POST'])
def name():
	return '<h1>Home</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
	return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''
@app.route('/signin', methods=['POST'])
def signin():
	# 需要从request对象读取表单内容：
	if request.form['username']=='admin' and request.form['password']=='password':
		return '<h3>Hello, admin!</h3>'
	return '<h3>Bad username or password.</h3>'
#配置URL，从HTTP请求拿到用户数据
#web框架提供自己的API来实现这些功能
#request.from['name']来获取表单内容
if __name__ == '__main__':
	app.run()

