#!/usr/bin/python3.5

def print_score(**kw):
    print('----------------')
    for name,score in kw.items():
        print('%10s  %d' % (name,score))
    print()

print_score(kobe=99,james=88,wade=77)

data = {
    'kobe B':99,
    'james L':88,
    'wade D':77
}
print_score(**data)

def print_info(name,*,gender,city='beijing',age):
    print('Personal Info')
    print('--------------')
    print('  Name:%s' % name)
    print('Gender:%s' % gender)
    print('  City:%s' % city)
    print('   Age:%s' % age)
    print()
print_info('bob',gender='M',age=20)
print_info('lisa',gender='F',city='LA',age=19)
