# -*- coding: utf-8 -*-

x = input('Enter a five digit number: ')
sum = 0
d = int(x[0])
d = d+1 if d<9 else 0
sum += d * 10**4

d = int(x[1])
d = d+1 if d<9 else 0
sum += d * 10**3

d = int(x[2])
d = d+1 if d<9 else 0
sum += d * 10**2

d = int(x[3])
d = d+1 if d<9 else 0
sum += d * 10

d = int(x[4])
d = d+1 if d<9 else 0
sum += d

print(sum)
