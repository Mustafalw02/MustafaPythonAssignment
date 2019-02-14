# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 18:59:13 2019

@author: mustafa
"""
#Taking Input
word = input("Please enter the path of the file: ")
word = word.split('.')

#Printing Extension
print("Extension is:", word[-1])
