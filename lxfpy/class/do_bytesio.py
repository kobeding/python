#!/usr/bin/python3.5
#数据读写不一定是文件，也可以在内存中读写
#操作二进制数据，需要BytesIO，实现在内存中读取二进制
from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())
#b'\xe4\xb8\xad\xe6\x96\x87hello world!'
f = BytesIO('你好!thanks!bye!'.encode('utf-8'))
#f = BytesIO(b'hi!thanks!bye!')
print(f.read())
#b'\xe4\xbd\xa0\xe5\xa5\xbd!thanks!bye!'

