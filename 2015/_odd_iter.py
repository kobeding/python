#!/usr/bin/python3.4
# test yiled return some odd number
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

x = int(input('Please input a number:'))
for i in _odd_iter():
    if i < x:
        print(i)
    else:
        break

