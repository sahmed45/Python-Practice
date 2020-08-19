# Program Name: Syed Ahmed Lab 4.py
# Course: IT 3883/W01
# Student Name: Syed Ahmed
# Assignment Number: Lab4
# Due Date: 03/2/2020
# Purpose: File I/O Operations to Calculate GPA

f = open('students.txt', "r")  #open the file
s = f.read()
g = s.split()
n = g[4::5]    #make an array of only the grade numbers
p = g[::5]      #make an array of only the names
print("Student Records \n")
print(s)
print("\n")
print("Student Standing \n")
for x in range(8):
    v = float(n[x])
                               #determine standing
    if v >= 3.5:
        print("Deans List", p[x])
    elif v < 2.0:
        print("Probation", p[x])
    elif 2.0 <= v < 3.5:
        print("Regular Standing", p[x])
