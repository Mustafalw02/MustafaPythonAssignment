# -*- coding: utf-8 -*-
#Taking Input
x = input('Enter a five digit number: ')
sum = 0

#Calculating Reverse
d = int(x[0])
sum += d

d = int(x[1])
sum += d * 10

d = int(x[2])
sum += d * 10**2

d = int(x[3])
sum += d * 10**3

d = int(x[4])
sum += d * 10**4

print(sum)
