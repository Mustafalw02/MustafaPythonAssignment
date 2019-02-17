# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 13:33:47 2019

@author: Mustafa
"""
#Taking Details

studentName = input("Please Enter the Student's Name: ")
fatherName = input("Please Enter the Father's Name: ")
rollNo = input('Please Enter the Roll Number: ')
courseName =  input('Please Enter the Course Name: ')

#Taking Marks
sub = input('Please Enter Subject Names seprated by commas: ').split(',')
subCode = input('Please Enter Sibject Code seprated by commas: ').split(',')
sub1 = int(input("Marks in " + sub[0] + ":"))
sub2 = int(input("Marks in " + sub[1] + ":"))
sub3 = int(input("Marks in " + sub[2] + ":"))
sub4 = int(input("Marks in " + sub[3] + ":"))
sub5 = int(input("Marks in " + sub[4] + ":"))

#Calculating total and %
totalMarks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = totalMarks/5

#Printing Marksheet
print()
print('|' + '-'*78 + '|')
print('|' + '*'*35 + 'MARKSHEET' + '*'*34 + '|')
print('|' + '-'*78 + '|')
print('|{:^78}|'.format('ACROPOLIS INSTITUTE OF TECHNOLOGY AND RESEARCH, INDORE'))
print('|' + '-'*78 + '|')
#Printing Details
print('''|{:<17}{:<25}{:<17}{:<19}|
|{:<17}{:<25}{:<17}{:<19}|'''
.format("Student's Name: ",studentName,"Father's Name: ",fatherName,
        "Roll Number: ",rollNo,"Course Name:",courseName ))

#Printing Marks, Total and %
print('''|                                                                              |
| |--------------------------------------------------------------------------| |
| |{:^7}|{:^14}|{:^34}|{:^16}| |
| |--------------------------------------------------------------------------| |'''
.format('S.No', 'Subject Code', 'Subject Name', 'Marks Obtained'))
print('''| |{:^7}|{:^14}|{:<34}|{:^16}| |
| |{:^7}|{:^14}|{:<34}|{:^16}| |
| |{:^7}|{:^14}|{:<34}|{:^16}| |
| |{:^7}|{:^14}|{:<34}|{:^16}| |
| |{:^7}|{:^14}|{:<34}|{:^16}| |
| |--------------------------------------------------------------------------| |
| |                                             Total Marks: {:^16}| |
| |                                             Percentage:  {:^16}| |
| |                                             Result:      {:^16}| |
| |--------------------------------------------------------------------------| |'''
.format("1.",subCode[0],sub[0],sub1,
        "2.",subCode[1],sub[1],sub2,
        "3.",subCode[2],sub[2],sub3,
        "4.",subCode[3],sub[3],sub4,
        "5.",subCode[4],sub[4],sub5,
        totalMarks, percentage, "PASS"))
print('|' + ' '*78 + '|')
print('|' + '-'*78 + '|')
