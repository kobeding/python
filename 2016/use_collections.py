from collections import namedtuple
#collections提供很多有用的集合类
Point = namedtuple('Point2',['x','y'])
#Point <class '__main__.Point2'>
#namedtuple是一个函数，创建一个自定义的tuple对象，规定了tuple元素的个数
#用属性而不是索引来引用tuple元素，很方便的定义一种数据类型
p = Point(1,2)
print('Point:',p.x,p.y)
#Point: 1 2
print(isinstance(p,Point))
print(isinstance(p,tuple))
Cirle = namedtuple('Cirle',['x','y','z']) 
c = Cirle(2,2,2)
print(c.x,c.y,c.z)

#list[]索引访问元素很快，但是插入和删除元素就很慢,list是线性存储，数据量大的时候，插入和删除效率低
from collections import deque
#deque是为了实现高效插入和删除操作的双向列表，适合用于队列和栈
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
q.append('m')
q.pop()
q.popleft()
print(q)
#deque('a', 'b', 'c', 'x'])
from collections import defaultdict,OrderedDict
#defaultdict：希望key不存在时返回一个默认值
dd = defaultdict(lambda:'N/A')
#TypeError: first argument must be callable or None
dd['key1'] = 'abc'
print('dd[\'key1\']=',dd['key1'])
print('dd[\'key2\']=',dd['key2'])
#dd['key1']= abc
#dd['key2']= N/A
d = dict([('a',1),('b',2),('c',3)])
print(d)
#{'c': 3, 'b': 2, 'a': 1}
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)
#OrderedDict([('a', 1), ('b', 2), ('c', 3)])
#而且Od函数会按照key插入的顺序返回
#实现一个FIFO的dict，容量超出限制时，先删除最早添加的Key：
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

from collections import Counter
#Counter是一个简单的计数器，实际上是一个dict的子类
c = Counter('programming')
#for ch in 'programming':
#	c[ch] = c[ch] + 1 
print(c)
#Counter({'m': 2, 'g': 2, 'r': 2, 'n': 1, 'i': 1, 'p': 1, 'o': 1, 'a': 1})
