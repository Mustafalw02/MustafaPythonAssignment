# -*- coding: utf-8 -*-

x = int(input('Enter a five digit number: '))
sum = 0
sum += x%10
x //= 10
sum += x%10
x //= 10
sum += x%10
x //= 10
sum += x%10
x //= 10
sum += x%10
x //= 10

print(sum)
