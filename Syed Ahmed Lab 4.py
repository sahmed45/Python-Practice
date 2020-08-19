# Program Name: Syed Ahmed Lab 4.py
# Course: IT 3883/W01
# Student Name: Syed Ahmed
# Assignment Number: Lab4
# Due Date: 03/2/2020
# Purpose: File I/O Operations to Calculate GPA

f = open('students.txt', "w")
count = 0
while count < 8:
    s = input("Enter Student name, student ID, number of hrs and GPA")
    f.write(s)
    f.write("\n")
    count += 1

