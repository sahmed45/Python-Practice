# Program Name: Syed Ahmed Lab 1.py
#Course: IT 3883/W01
#Student Name: Syed Ahmed
#Assignment Nummber: Lab1
#Due Date: 01/20/2020
#Purpose: Prints a welcome message and Sums 3 number inputs

print("'What's your name?") #name prompt
name = input()
print('Welcome, ', name) #welcome message print

print('Enter number 1') #number 1 prompt
n1 = input()
print('Enter number 2') #number 2 prompt
n2 = input()
print('Enter number 3') #number 3 prompt
n3 = input()
sum3 = int(n1) + int(n2) + int(n3)  #sum function
product = int(n1) * int(n2) * int(n3)  #product function
average = ((int(n1) + int(n2) + int(n3))/3) #average function

print(' The sum of the inputs is ',  sum3) #printing the sum
print(' The product of the inputs is ',  product) #printing the sum
print(' The average of the inputs is ',  average) #printing the sum