#!/usr/bin/python
#!/usr/bin/python
# Filename: reference.py

print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist # mylist is just another name pointing to the same object!

del shoplist[0] # I purchased the first item, so I remove it from the list

print('shoplist is', shoplist)
print('mylist is', mylist)
# notice that both shoplist and mylist both print the same list without
# the 'apple' confirming that they point to the same object

print('Copy by making a full slice')
#mylist = shoplist[:] # make a copy by doing a full slice
del shoplist[0] # remove first item
#!/usr/bin/python
# Filename: reference.py

print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist # mylist is just another name pointing to the same object!

del shoplist[0] # I purchased the first item, so I remove it from the list

print('shoplist is', shoplist)
print('mylist is', mylist)
# notice that both shoplist and mylist both print the same list without
# the 'apple' confirming that they point to the same object

print('Copy by making a full slice')
mylist = shoplist[:] # make a copy by doing a full slice
del mylist[0] # remove first item

print('shoplist is', shoplist)
print('mylist is', mylist)
# notice that now the two lists are different

input()


print('shoplist is', shoplist)
print('mylist is', mylist)
# notice that now the two lists are different

input()

# Filename: seq.py

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# Slicing on a string
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])
input()

