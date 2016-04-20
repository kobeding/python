#!/usr/bin/python3.5

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x 

obj = MyObject()
print("hasattr(obj,'x')=",hasattr(obj,'x'))
print("hasattr(obj,'y')=",hasattr(obj,'y'))
setattr(obj,'y',19)
print("hasattr(obj,'y')=",hasattr(obj,'y'))
print("getattr(obj,'y')=",getattr(obj,'y'))
print("obj.y=",obj.y)
print("getattr(obj,'z')=",getattr(obj,'z',404))
f = getattr(obj,'power')  #获取属性power
print(f)
print(f())
"""output:
hasattr(obj,'x')= True
hasattr(obj,'y')= False
hasattr(obj,'y')= True
getattr(obj,'y')= 19
obj.y= 19
getattr(obj,'z')= 404
<bound method MyObject.power of <__main__.MyObject object at 0xb724e48c>>
81
"""
