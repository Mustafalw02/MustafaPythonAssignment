# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 18:59:13 2019

@author: mustafa
"""
#Taking Input
word = input("Please enter the path of the file: ")
ext = input('Enter extension to which you need to change the file: ')
word = word.split('/')
word = word[-1].split('.')

#Printing Extension
print("Extension is:", word[0] + ext)
