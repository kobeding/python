#!/usr/bin/env python3

import hashlib
#hashlib提供了常见的摘要算法，如MD5，SHA1等等
#摘要算法：哈希算法，散列算法，通过一个函数，把任意长度的数据转换为一个长度固定的数据串
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
#d26a53750bc40b38b65a520292f69306
#md5是最常见的摘要算法，速度很快，生成的结果是固定的128bit字节（32*4（16进制））

print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in'.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
#86e1eae2a08c152d39b55baed085c71a0cc9d10b
#160bit字节,40*4的16进制表示
