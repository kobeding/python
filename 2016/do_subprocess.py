#!/usr/bin/python3.5
#很多时候，子进程并不是自身，而是外部进程，需要控制子进程的输入输出
#在python代码中运行命令 $ nslookup www.python.org
import subprocess
#subprocess模块可以非常方便的启动一个子进程，然后控制其输入输出
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)
print('$ nslookup')
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
#子进程需要输入，通过 communicate 方法，相当与直接在命令行nslookup后，输入：
#set q=mx
#python.org
#exit
print(output.decode('utf-8'))
print('Exit code :',p.returncode)
"""
$ nslookup www.python.org
Server:		127.0.1.1
Address:	127.0.1.1#53

Non-authoritative answer:
www.python.org	canonical name = python.map.fastly.net.
Name:	python.map.fastly.net
Address: 23.235.47.223

Exit code: 0
$ nslookup
Server:		127.0.1.1
Address:	127.0.1.1#53

Non-authoritative answer:
python.org	mail exchanger = 50 mail.python.org.

Authoritative answers can be found from:
python.org	nameserver = ns3.p11.dynect.net.
python.org	nameserver = ns4.p11.dynect.net.
python.org	nameserver = ns1.p11.dynect.net.
python.org	nameserver = ns2.p11.dynect.net.
mail.python.org	internet address = 188.166.95.178
ns1.p11.dynect.net	internet address = 208.78.70.11
ns2.p11.dynect.net	internet address = 204.13.250.11
ns3.p11.dynect.net	internet address = 208.78.71.11
ns4.p11.dynect.net	internet address = 204.13.251.11


Exit code : 0
"""