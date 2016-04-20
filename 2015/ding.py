#!/usr/bin/python3.4
#Filename: prime_numbers.py

#打印1000以内打素数：
def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

#构造3开始的奇数序列：
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

#定义一个筛选器：
def _not_divisiable(n):
    return lambda x: x % n > 0

#定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisiable(n),it)

if __name__ == '__main__':
    main()

