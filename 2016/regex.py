#!/usr/bin/python3.5
#用字符串定义一个字符串的规则，匹配
#\d    \w    \s  ....[0-9,a-z]   {3,8}  {n}     .(1) *(0-) +(1-) ?(0-1)   [a|A]
#re模块
import re
print('ABC\t\-001')
print(r'ABC\t\-001')
print(re.split(r'[\s\,\;]+','a,b;;   c   d'))
#ABC	\-001
#ABC\t\-001

print('Test: 010-12345')
#'-'是特殊字符，在正则表达式中，要用\转义
m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
#匹配成功，返回一个match对象，否则返回None
print(m.group(1),m.group(2))
#group分组，()表示就是要提取的分组
t = '19:05:30'
print('Test:',t)
#编译
re_time = re.compile(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:([0-5][0-9])\:([0-5][0-9])$')
m = re_time.match(t)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))