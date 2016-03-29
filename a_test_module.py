#!/usr/bin/python3.4
# Filename: a_test_module.py

'a test module'
__author__ = 'DINGcW'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World!')
    elif len(args) == 2:
        print('Hello,%s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()
