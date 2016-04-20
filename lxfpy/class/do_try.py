#!/usr/bin/python3.5
#传统情况，通过返回约定的错误代码，检查错误
#跟返回的正确值混杂在一起，繁琐
#内置try...except...处理机制...
try:#认为某些代码可能会出错，放到这里面，出错，后续代码不会执行
	print('try...')
	r = 10 / 0
	print('result:',r)
except ZeroDivisionError as e: #出错后跳到这里，错误处理代码
	print('except:',e)
except ValueError as e:#捕获不同类型错误，嵌套使用，注意错误类间的继承关系
else:
	print('no error!')#没有错误时，执行else语句
finally:#都会被执行
	print('finally')
print('END')
"""
python的错误其实也是class，所有错误类型都继承自BaseException
try...
except: division by zero
finally
END
"""