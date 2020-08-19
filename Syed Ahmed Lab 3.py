# Program Name: Syed Ahmed Lab 3.py
# Course: IT 3883/W01
# Student Name: Syed Ahmed
# Assignment Number: Lab3
# Due Date: 02/17/2020
# Purpose: Calculates and prints a students grade average and letter grade

global name1
global name2
global name3
name1 = input("Enter student one name")

t1 = int(input("Enter grade test 1"))
t2 = int(input("Enter grade test 2"))
t3 = int(input("Enter grade test 3"))               #Name and grade inputs
t4 = int(input("Enter grade test 4"))

name2 = input("Enter student two name")

t5 = int(input("Enter grade test 1"))
t6 = int(input("Enter grade test 2"))
t7 = int(input("Enter grade test 3"))               #Name and grade inputs
t8 = int(input("Enter grade test 4"))

name3 = input("Enter student three name")

t9 = int(input("Enter grade test 1"))
t10 = int(input("Enter grade test 2"))
t11 = int(input("Enter grade test 3"))               #Name and grade inputs
t12 = int(input("Enter grade test 4"))


def avg(x, y, z, q):
    sum1 = x + y + z + q          #average function
    avg1 = sum1 / 4
    return avg1


def grade(x):               #Letter grade function
    if x > 90:
        return "A"
    if 80 <= x <= 89:
        return "B"
    if 70 <= x <= 79:
        return "C"
    if 60 <= x <= 69:
        return "D"
    else:
        return "F"


avgg1 = avg(t1, t2, t3, t4)  #calling average function
avgg2 = avg(t5, t6, t7, t8)  #calling average function
avgg3 = avg(t9, t10, t11, t12)  #calling average function


print("Name: {}, Average: {}, Letter Grade: {}".format(name1, avgg1, grade(avgg1)))  #final print line
print("Name: {}, Average: {}, Letter Grade: {}".format(name2, avgg2, grade(avgg2)))  #final print line
print("Name: {}, Average: {}, Letter Grade: {}".format(name3, avgg3, grade(avgg3)))  #final print line