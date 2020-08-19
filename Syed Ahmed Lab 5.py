# Program Name: Syed Ahmed Lab 5.py
# Course: IT 3883/W01
# Student Name: Syed Ahmed
# Assignment Number: Lab5
# Due Date: 03/16/2020
# Purpose: Dictionary operations

comp = {'Company Name': input("Enter company name"), 'City': input("Enter City" ), 'State': input("Enter State")}
# ^ Dictionary creation with inputs
print(comp)

comp.pop('City') #remove city index
print(comp)