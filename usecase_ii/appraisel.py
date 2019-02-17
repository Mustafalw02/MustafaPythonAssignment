# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 15:05:36 2019

@author: Mustafa
"""

#Taking Details
date = input("Please Enter Today's Date: ")
hr = input('Please Enter the Name of HR: ')
comp_name = input('Please Enter the name of Company: ')
place = input("Please Enter the place where company is located: ")
firstName = input('Please Enter the first Name of Employee: ')
lastName = input('Please Enter the last Name of Employee: ')
monthlySalary = float(input('Please Enter the Monthly Salary of Employee: '))
emp_des = input("Designation of Employee: ")
whitespace = 73 - (len(firstName) + len(lastName))
#Calculating appraisel
newSalary = monthlySalary * 1.15

#Printing Appraisel Letter
print('''
|------------------------------------------------------------------------------|
|To,                                                                           |
|                                                                              |''')

print('|Mr. {} {}'.format(firstName, lastName) + " " * (whitespace) + "|")

print('''|{0:<78}|      
|{1:<78}|
|{2:<78}|
|                                                                              |
|Date:{4:<73}|
|                                                                              |
|From,                                                                         |
|                                                                              |
|{3:<78}|
|HR Manager                                                                    |
|{1:<78}|
|                                                                              |
|Sub: Performance Appraisal                                                    |
|                                                                              |
|It is a privilege for me to write this letter to you. Employees like you who  |
|work with sheer dedication are an asset to the organization. I am feeling     |
|very proud to mention that the company has decided to give you a raise in your| 
|salary by 15%. I have gone through your performance chard and was surprised   | 
|to see that you have always achieved your target well on time and sometimes   |
|even exceeded the same also.                                                  |
|                                                                              |
|Your increment will be effective from next month and I am forwarding this     |
|copy of appraisal letter to the payroll department also. If you have any      |
|doubts regarding your increment, please feel free to meet me in person.       |
|                                                                              |
|Yours truly,                                                                  |
|                                                                              |
|______________                                                                |
|                                                                              |
|{3:<78}|
|HR Manager                                                                    |
|------------------------------------------------------------------------------|
'''.format(emp_des, comp_name, place,hr, date ))
