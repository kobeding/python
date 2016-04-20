from enum import Enum,unique

@unique  #装饰器检查保证没有重复值
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

day1 = Weekday.Mon
print('day1 = ',day1)
print('Weekday.Tue =',Weekday.Tue)
print("Weekday['Tue'] =",Weekday['Tue'])
#print('Weekday.value =',Weekday.Mon.vaule)
print('Weekday.Mon == day1',day1 == Weekday.Mon)
print('Weekday.(1) == day1',day1 == Weekday(1))
"""
day1 =  Weekday.Mon
Weekday.Tue = Weekday.Tue
Weekday['Tue'] = Weekday.Tue
Weekday.Mon == day1 True
Weekday.(1) == day1 True
"""
for name,member in Weekday.__members__.items():
	print(name,'=>',member)
#Sun => Weekday.Sun...
Month = Enum('Month',('jan','feb','Mar','apr','may','jun','jul','aug','sep','oct','nov','dec'))
for name,member in Month.__members__.items():
	print(name,'=>',member)
#jan => Month.jan...