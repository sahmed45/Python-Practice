# Program Name: Syed Ahmed Extra Credit.py
# Course: IT 3883/W01
# Student Name: Syed Ahmed
# Assignment Number: Extra Credit
# Due Date: 04/26/2020
# Purpose: FooBar printing


i = 0

while i <= 100:
    if i % 15 == 0:
        print("foobar")
    elif i % 3 == 0:
        print("foo")
    elif i % 5 == 0:
        print("bar")

    else:
        print(i)
    i = i + 1
