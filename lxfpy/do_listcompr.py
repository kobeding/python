#!/usr/bin/python3.5

print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x%2==0])
print([m+n for m in 'ABC' for n in 'XYZ'])
#if过滤，两层for循环

d = {'x':'A','y':'B','z':'C'}
print([k +'='+ v for k,v in d.items()])
for k,v in d.items():
    print(k,v)
#for循环同时使用两个甚至多个变量，dict同时迭代key和value
L = ['Hello','WORLD']
print([s.lower() for s in L])
