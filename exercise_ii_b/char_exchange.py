# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 18:59:13 2019

@author: mustafa
"""
#Taking the Input
word = input('Enter the String: ')
#Printing the exchanged string
print('Exchanged string is ' + word[-1] + word[1:len(word)-1] + word[0])