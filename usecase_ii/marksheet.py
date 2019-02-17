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
sub1 = int(input("Marks in Mathematics-III: "))
sub2 = int(input("Marks in Analysis Design of Algorithms: "))
sub3 = int(input("Marks in Software Engineering: "))
sub4 = int(input("Marks in Computer Org. & Architecture: "))
sub5 = int(input("Marks in Operating Systems: "))

#Calculating total and %
totalMarks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (totalMarks/450) * 100

#Printing Marksheet
print()
print('|' + '-'*78 + '|')
print('|' + '*'*35 + 'MARKSHEET' + '*'*34 + '|')
print('|' + '-'*78 + '|')

#Printing Details
print('''|{:<17}{:<61}|   
|{:<17}{:<61}|
|{:<17}{:<61}|
|{:<17}{:<61}|'''
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
.format("1.","BT401","Mathematics-III",sub1,
        "2.","CS402","Analysis Design Of Algorithm",sub2,
        "3.","CS403","Software Engineering",sub3,
        "4.","CS404","Computer Org. & Architecture",sub4,
        "5.","CS405","Operating Systems",sub5,
        totalMarks, percentage, "PASS"))
print('|' + ' '*78 + '|')
print('|' + '-'*78 + '|')
