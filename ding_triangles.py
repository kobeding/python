#!/usr/bin/python3.4
# Filename: ding_triangles.py
#def triangles():
L = [1,]
x = 0
while x < 10:
	i = len(L) - 1
    while(i):
		L[i] = L[i] + L[i-1]
		i -= 1 
	L.append(1)
	print(L)
	x += 1

#y = triangles()
#print(y)
