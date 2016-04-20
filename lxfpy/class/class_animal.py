#!/usr/bin/python3.4
#Filename: class_animal.py

class Animal(object): #基类，父类或超类(base class，super class)
    def run(self):  #run方法
        print('Animal is running...')

class Dog(Animal):  #继承，子类subclass
    def run(self):   #重新定义run方法，覆盖或者直接添加新方法eat(self)
    #(也可以什么也不用做，直接继承，获得父类的全部功能)
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal): #理解多态的好处，再编写一个函数
#注意接受的不是Animal，但当我们传入Animal类型的实例时
    animal.run() #与Animal同样的run方法
    animal.run()#不保证是Animal类型，只需要保证对象有一个run()方法
    				#”鸭子类型“，不要求严格的继承体系

class Tortoise(Animal):
	def run(self): 
		print("Tortoise is runing slowly...")
#新增的子类,不必对run_twice()做任何修改，任何依赖Animal最为参数的函数
#或者方法都可以不加修改的正常运行，原因就在于多态
a = Animal()
b = Tortoise()
d = Dog()
c = Cat()

print('a is Animal?',isinstance(a,Animal))
print('a is Dog',isinstance(a,Dog))
print('a is Cat?',isinstance(a,Cat))

print('d is Animal?',isinstance(d,Animal))
print('d is Dog',isinstance(d,Dog))
print('d is Cat?',isinstance(d,Cat))

run_twice(a) #直接是Animal()实例，都有输出结果
run_twice(b)  #只要是Animal类型，照样可以输出
run_twice(c)  #传入Cat()--Animal类型实例
run_twice(d) #另外一个实例