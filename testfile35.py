#! /bin/env python3
# -*-coding: utf-8 -*-
# name = input('please input your name:')
# print ('name is:',name)


l = [x*x for x in range(1, 11) if x % 2 == 0]
print(isinstance(l, list))
print(l)

print([m+n+p for m in "ABC" for n in "EF" for p in "GH"])

from functools import reduce
def str2int(s):
    def fn(x, y):
        return x*10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

x = str2int('15963')
print(isinstance(x, int))

x1 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}['12345'[3]]
print(x1)

print(sorted([1,9,-10,6,-4,7], key=abs, reverse=True))

f = str2int
print(f.__name__)

import functools
int2 = functools.partial(int, base=2)
print(int2('100000'))

if __name__ == '__main__':
    num = str2int('1203')
    print(num)

a = 2
print('hello' if a == 0 else 'World')

if 3 > a > 1:
    print('a:',a)
if 1 < a > 0:
    print(a)

names = ['Tom', 'Tina', 'Alis']
score = [50, 94, 65]
for i, j in zip(names, score):
    print(i, ':', j)
for index, name in enumerate(names):
    print(index, name)

L = [0, 1, 2, 3, 4, 5, 6, 8, 10, 15, 18]
even = [num for num in L if num % 2 == 0]
print(even)



import pandas as pd
import numpy as np

items = np.zeros(3)
print(items)

dates = pd.date_range('20130101', periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

print(df.loc[:,['A', 'B']])

print(df.apply(lambda x: x.max() - x.min(), axis=1))

from math import ceil, floor
print(ceil(2.5), floor(2.5))