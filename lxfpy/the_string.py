#!/usr/bin/python3.5

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

'''
输出：
/*Python-中文
b'Python-\xe4\xb8\xad\xe6\x96\x87'
Python-中文*/
'''
