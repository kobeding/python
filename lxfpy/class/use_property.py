class Student(object):
	@property#把一个getter方法变为属性
	def score(self):
	#def get_score(self):
	#def __init__ (self,score)
		#self.score = score
	#直接通过s.score = 60 修改。
	    return self._score
#之前的调用直接把属性暴露出来了，例如直接s.score = 60
#为了限制score的范围，通过set_score()方法来设置成绩,get_socre()得到成绩
#设置后,不能随便的设置score如：s.set_score(9000)
#但是,这种方法又显得有点复杂，没有直接用属性那么直接简单
#内置装饰器@property负责把一个方法变成属性调用
	@score.setter#负责把一个setter方法变成属性赋值
	def score(self,value):
	#def set_score(self,value):
#s.set_score(60)---OK  s.set_score(999)  ---不行

		if not isinstance(value,int):
			raise ValueError('score must be an interger!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		self._score = value

s = Student()
s.score = 60 #s.set_socre(60)
print('s.score=',s.score)  @s.get_score()
#s.score = 9999

		