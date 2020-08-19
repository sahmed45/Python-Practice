# Program Name: Syed Ahmed Lab 6.py
# Course: IT 3883/W01
# Student Name: Syed Ahmed
# Assignment Number: Lab6
# Due Date: 03/30/2020
# Purpose: Tkinter

from tkinter import *


def click():   #entry input function
    text = te.get()
    return -1


def calc():    #gpa testing function
    x = click()
    if x >= 3.5:
        return "Dean's List"
    if x <= 2.0:
        return "Probation"
    if 2.0 <= x <= 3.5:
        return "Regular Standing"

    else:
        return "invalid GPA"


r = Tk()

r.title('GPA calc')
Label(r, text="Enter GPA").grid(row=0)
te = Entry(r)  #entry box
te.grid(row=0, column=1)
Button(r, text="Submit", command=click).grid(row=1, column=1)    #buttons
Label(r, text="Status:").grid(row=2, column=0)  #labels
Label(r, text=calc()).grid(row=2, column=1)

r.mainloop()
