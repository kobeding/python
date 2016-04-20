#!/usr/local/bin/python3.5
#Fliename if.py

number = 23
guess = int(input('Enter an integer:'))

if guess == number:
	print('1.')
	print('2.')
elif guess < number:
	print('3.')
else:
	print('4.')
print('Done')
	
