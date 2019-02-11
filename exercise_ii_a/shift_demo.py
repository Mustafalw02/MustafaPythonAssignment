# -*- coding: utf-8 -*-

x = int(input('Enter a number: '))
p = int(input('Number of shifts: '))
print('Left shift: ', end = "")
print(x*2**p)
print('Right shift: ', end = "")
print(x//2**p)

