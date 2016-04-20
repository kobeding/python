#!/usr/bin/python3.4
#Filename: class_student.py

class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))

    def get_grade(self):
        if self.__score >= 91:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)

print('bart.get_name() = ',bart.get_name())
bart.set_score(60)
print('bart.get_score() = ',bart.get_score())
print('lisa.get_score() = ',lisa.get_score())
bart.print_score()
lisa.print_score()

print('grade of Bart:',bart.get_grade())
print('grade of Lisa:',lisa.get_grade())
print('Do NOT use bart._Student__name:',bart._Student__name)
