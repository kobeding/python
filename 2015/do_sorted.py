#!/usr/bin/python3.4
# sorted 应用 
from operator import itemgetter

L = ['bob','about','Zoo','Credit']

print(sorted(L))
print(sorted(L,key = str.lower))

s = [('Bob',75),('Adam',92),('Bart',68),('Lisa',88)]
def by_name(t):
	print(t[0])  #取前面的名
	return t[0]

s2 = sorted(s,key = by_name)
print(s2)

def by_score(t):
	print(t[-1]) #取后面的分数
	return t[-1]
	
s3 = sorted(s,key = by_score,reverse = True)
print(s3)
#print(sorted(s,key = itermgetter(0)))
#print(sorted(s,key = lambda t: t[1]))
#print(sorted(s,key = itemgetter(1),reverse = True))