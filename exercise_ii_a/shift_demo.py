# -*- coding: utf-8 -*-

#Taking Input
x = int(input('Enter a number: '))
p = int(input('Number of shifts: '))

#Manual Left Shift
print('*'*10 + 'Manual Left Shift' + '*'*10)
print('Left shift:',x<<p)
#Formula Left Shift
print('*'*10 + 'Formula Left Shift' + '*'*10)
print('Left shift: ', end = "")
print(x*2**p)

#Manual Right Shift
print('*'*10 + 'Manual Right Shift' + '*'*10)
print('Right shift:',x>>p)
#Formula Right Shift
print('*'*10 + 'Formula Right Shift' + '*'*10)
print('Right shift: ', end = "")
print(x//2**p)

