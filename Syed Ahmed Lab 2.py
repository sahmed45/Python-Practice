# Program Name: Syed Ahmed Lab 2.py
#Course: IT 3883/W01
#Student Name: Syed Ahmed
#Assignment Number: Lab2
#Due Date: 02/03/2020
#Purpose: Calculates a college's budget increased based on new students

nb = 0
count = 0

while count < 3:

    s = input("'How many new students are entering")
    print("'What is the old budget?")  # old budget prompt
    ob = input()
    count += 1
    if int(s) >= 1500:
        nb = int(ob) * 1.05
        print('The budget increase is 5% and the new budget is', nb)
        continue
    elif int(s) >= 1001: #1001-1500 conditional
        nb = int(ob) * 1.04
        print('The budget increase is 4% and the new budget is', nb)
        continue
    elif int(s) >= 601: #601-1000 conditional
        nb = int(ob) * 1.03
        print('The budget increase is 3% and the new budget is', nb)
        continue
    elif int(s) >= 301: #301-600 conditional
        nb = int(ob) * 1.02
        print('The budget increase is 2% and the new budget is', nb)
        continue
    elif int(s) >= 1: #1-300 conditional
        nb = int(ob) * 1.01
        print('The budget increase is 1% and the new budget is', nb)
        continue
    else: #0 conditional
        nb = int(ob)
        print('There is no budget increase and the new budget is', nb)
        continue

