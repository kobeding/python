#!/usr/bin/env python3

import itertools
#itertools提供了很多非常有用的用于操作迭代对象的函数
#返回值不是list，而是iterator，只有通过for迭代生成
#count()创建一个无限迭代器
natuals = itertools.count(1)
#takewhile()根据条件判断来截取一个有限的序列
ns = itertools.takewhile(lambda x:x <= 10,natuals)
print(list(ns))
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in natuals:
	print(n,end=',')
	if n >= 100:
		break
#cycle()会传入一个序列无限的重复下去
cs = itertools.cycle('ABC')
t = 10
for c in cs:
	print(c,end=',')
	t = t - 1
	if t == 0:
		break
#repeat()限定重复的次数
cd = itertools.repeat('ABC',11)
p = 10
for d in cd:
	print(d,end=',')
	p = p - 1
	if p == 0:
		break
#chain()连接
for cc in itertools.chain('ABC','XYZ'):
	print(cc,end = ',')
#groupby()把迭代器中相邻的重复元素挑出来放在一起，忽略大小写：
for key,group in itertools.groupby('AaaBBbcCAAa',lambda c:c.upper()):
	print(key,list(group))




