#!/usr/bin/python3.4
# sorted 应用 
from operator import itemgetter

L = ['bob','about','Zoo','Credit']

print(sorted(L))
print(sorted(L,key = str.lower))

s = [('Bob',75),('Adam',92),('Bart',68),('Lisa',88)]

def by_name(t):
    return t[0]

s2 = sorted(s,key = by_name)
print(s2)

def by_score(t):
    return t[-1]

s3 = sorted(s,key = by_score,reverse = True)
print(s3)
#print(sorted(student,key = itermgetter(0)))
#print(sorted(student,key = lambda t: t[1])
#print(sorted(student,key = itemgetter(1),reverse = True))
