def cccmp(x,y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print(sorted([36,5,12,9,21],cccmp))

