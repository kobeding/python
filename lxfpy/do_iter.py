#!/usr/bin/python3.5
#关于迭代

from collections import Iterable,Iterator

def g():
    yield 1
    yield 2
    yield 3

print(isinstance([1,2,3],Iterable))
print(isinstance('abc',Iterable))
print(isinstance(123,Iterable))
print(isinstance(g(),Iterable))
print('-----------------------')
print(isinstance([1,2,3],Iterator))
print(isinstance(iter([1,2,3]),Iterator))
print(isinstance('abc',Iterator))
print(isinstance(123,Iterator))
print(isinstance(g(),Iterator))
#iter list:
print('for x in [1,2,3,4,5]:')
for x in [1,2,3,4,5]:
    print(x)

print('next():')
it = iter([1,2,3,4,5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a':1,'b':2,'c':3}
#iter each key:
print('iter key:',d)
for k in d.keys():
    print('key=',k)
#iter each value:
print('iter value:',d)
for v in d.values():
    print('key=',v)
#iter key & value:
print('iter item:',d)
for k,v in d.items():
    print('item:',k,v)
print("iter enumerate(['A','B','C'])")
for i,value in enumerate(['A','B','C']):
    print(i,value)
#iter complex list:
print('iter [(1,1),(2,4),(3,9)]:')
for x,y in  [(1,1),(2,4),(3,9)]:
    print(x,y)


