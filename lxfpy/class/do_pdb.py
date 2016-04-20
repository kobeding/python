#!/usr/bin/python3.5 
import pdb

s = '0'
n = int(s)
pdb.set_trace()  #需要inport pdb，在可能出错的地方放一个这个，设置断点
#python3.5 do_pdb.py，直接运行程序，会在这里停止进入pdb调试环境
#p n  ---   c  ---等参数进行调试
print(10 / n)
"""
(Pdb) p n
0
(Pdb) p s
'0'
(Pdb) c
Traceback (most recent call last):
  File "do_pdb.py", line 7, in <module>
    print(10 / n)
ZeroDivisionError: division by zero
-------
 python3.5 -m pdb do_pdb.py 调出pdb调试交互
 (Pdb) l   ----列出程序
  1  	#!/usr/bin/python3.5
  2  ->	import pdb
  3  	
  4  	s = '0'
  5  	n = int(s)
  6  	pdb.set_trace()
  7  	print(10 / n)
[EOF]
(Pdb) n   ---单步运行
> /home/kobe/duv/python/lxfpy/class/do_pdb.py(4)<module>()
-> s = '0'
(Pdb) n
> /home/kobe/duv/python/lxfpy/class/do_pdb.py(5)<module>()
-> n = int(s)
(Pdb) n
> /home/kobe/duv/python/lxfpy/class/do_pdb.py(6)<module>()
-> pdb.set_trace()
(Pdb) n
> /home/kobe/duv/python/lxfpy/class/do_pdb.py(7)<module>()
-> print(10 / n)
(Pdb) p s   ---输出变量值
'0'
(Pdb) p n
0

"""