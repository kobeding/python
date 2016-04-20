#!/usr/bin/python3.5
#变量从内存中变成可存储或传输的过程成为序列化(un/pickle)
#序列化后将其写入磁盘，或者网络传输到别的机器（反序列-->到内存）
#序列化对象
import pickle  #序列化模块
d = dict(name='Bob',age=20,score=88)
date = pickle.dumps(d)
print(date)
#pickle.dumps()，把任意对象序列化成为一个bytes，然后可以将其写入文件
with open('dump.txt','wb') as f:
	#f.write(b'test')
	k = pickle.dump(d,f) #-->直接把对象序列化后写入,奇怪的二进制文件内容
	#file-like Object
print(k)  #输出是None
print(date)
reborn = pickle.loads(date)
#从磁盘读到内存，先把内容读到一个bytes
#然后用pickle.loads()方法反序列出对象
print(reborn)
with open('dump.txt','rb') as f:
	d = pickle.load(f)#直接从file-like Object 中反序列化对象

print(d)
#输出与原来变量完全不相干的变量，只是内容相同而已
"""
b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00Bobq\x02X\x05\x00\x00\x00scoreq\x03KXX\x03\x00\x00\x00ageq\x04K\x14u.'
b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00Bobq\x02X\x03\x00\x00\x00ageq\x03K\x14X\x05\x00\x00\x00scoreq\x04KXu.'
{'name': 'Bob', 'age': 20, 'score': 88}
{'name': 'Bob', 'age': 20, 'score': 88}
"""