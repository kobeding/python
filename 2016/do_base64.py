import base64
#用64个字符来表示任意二进制数据的方法
#常用在URL,Cookie，网页中传输少量的二进制数据
#3 8 ---> 4 6 六位：32 16 8 4 2 1 --->对应64个字符表示编码（或者自定义64字符顺序）
s = base64.b64encode('在python中使用BASE64编程'.encode('utf-8'))
print(s)
d = base64.b64encode(s).decode('utf-8')
print(d)

s = base64.urlsafe_b64encode('在python中使用BASE64编程'.encode('utf-8'))
#url中不能用+/(- _)作为参数
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)
"""
b'5ZyocHl0aG9u5Lit5L2/55SoQkFTRSA2NCDnvJbnqIs='
NVp5b2NIbDBhRzl1NUxpdDVMMi81NVNvUWtGVFJTQTJOQ0RudkpibnFJcz0=
b'5ZyocHl0aG9u5Lit5L2_55SoQkFTRQ=='
在python中使用BASE64编程
"""