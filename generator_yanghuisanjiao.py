#!/usr/bin/python3.4
# Filename: generator_yanghuisanjiao.py

def triangles():
    L = [1,]
    while(True):
        yield L
        i = len(L) - 1
        while(i):
            L[i] = L[i] + L[i-1]
            i -= 1
        L.append(1)

n = 0
for t in triangles():
    print(t)
    n = n+1
    if n == 10:
        break
