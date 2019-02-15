# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 18:59:13 2019

@author: mustafa
"""
#Taking Input
marks = input("Please Enter your name and the marks of 5 subjects and 3 practicals comma seprated: ")
marks = marks.split(',')
th_marks = int(marks[1]) + int(marks[2]) + int(marks[3]) + int(marks[4]) + int(marks[5]) 
pr_marks =  int(marks[6]) + int(marks[7]) + int(marks[8])
percent = ((th_marks + pr_marks)*100)/440

#Printing Total and Marks
print("{0} obtained {1} marks out of 350 in theory and {2} marks out of 90 in practical and successfully passed the exam\
 with {3:.2f}% in aggregate. Many congratulations to {0}".format(marks[0], th_marks, pr_marks, percent))
