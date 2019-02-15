# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 18:59:13 2019

@author: mustafa
"""
#Taking Input
marks = input("Please enter the marks of 5 subjects and 3 practicals: ")
marks = marks.split(',')
th_marks = int(marks[0]) + int(marks[1]) + int(marks[2]) + int(marks[3]) + int(marks[4]) 
pr_marks =  int(marks[5]) + int(marks[6]) + int(marks[7])
percent = (th_marks + pr_marks)/8

#Printing Total and Marks
print("Marks Obtained in Theory = " + str(th_marks))
print("Marks Obtained in Practical = " + str(pr_marks))
print("Percentage obtained = " + str(percent))