from collections import OrderedDict
class LastUpdateOrderedDict(OrderedDict):

	def __init__(self,capacity):
		super(LastUpdateOrderedDict,self).__init__()
		self._capacity = capacity

	def __setitem__(self,key,value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last = False)
			print('remove',last)
		if containsKey:
			del self[key]
			print('set:',(key,value))
		else:
			print('add',(key,value))
		OrderedDict.__setitem__(self,key,value)

d = LastUpdateOrderedDict(3)
m = dict([('a',1),('b',2),('c',3),('d',4)])
for key,value in m.items():
	d [key] = value
print(d)