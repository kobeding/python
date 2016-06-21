#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
#MVC(Model-View-Controller)模型-视图-控制器  嵌入一些变量和指令 根据传入的数据替换
from flask import Flask, request, render_template

app = Flask(__name__)
#处理URL的函数就是C:Controller，负责业务逻辑(检查用户名是否存在,取出用户信息等等)
#包含变量{{name}}的模块就是V，负责显示逻辑，通过简单的替换一些变量，最终输出用户看到的HTML
#Modle:是用来传给View的，View在替换变量的时候，可以从Model中取出相应的数据
@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
	return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	if username=='admin' and password=='password':
		return render_template('signin-ok.html', username=username)
	return render_template('form.html', message='Bad username or password', username=username)
#Flask通过render_template(渲染模块)函数来实现模块的渲染，和web框架类似，也有很多python模块
#Flask默认支持的模块是jinja2
if __name__ == '__main__':
	app.run()