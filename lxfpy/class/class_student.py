#!/usr/bin/python3.4
#Filename: class_student.py

class Student(object):  #定义类 类名（继承），本身只是一个类
    def __init__(self,name,score): #模板作用，必须属性绑定
        self.name = name
        self.score = score
#__init__第一个参数永远是self，表示创建实例本身(谁创建就是谁)
#把各种属性绑定到self，self指向创建实例(bart/lisa等)本身
#创建参数的方法跟普通函数没什么区别(self必须外)
    def print_score(self):
        print('%s:%s' % (self.name,self.score))
#数据封装，称为类的方法(取得分数)
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
#内部封装，可以给这个类添加新的方法，通过实例直接调用
bart = Student('Bart Simpson',59)#创建实例，有内存地址
lisa = Student('Lisa Simpson',87)#要与__init__匹配
bart.age = 8
print(bart.age)  #可以输出
#print(lisa.age)  #不能输出，虽然是同一个类的不同实例
print('bart.name = ',bart.name )
print('lisa.score = ',bart.score )
bart.print_score()  #直接调用类(实例.方法)的方法
lisa.print_score()#如何打印，在类内部定义，数据和逻辑被“封装“起来了
#调用很容易，却不用知道内部实现的细节

print('grade of Bart:',bart.get_grade())
print('grade of Lisa:',lisa.get_grade())
