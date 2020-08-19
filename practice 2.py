for i in range(5):
    n = input("enter an integer ")
    if int(n) == 99:
        print("Ninety-nine")
    elif int(n) == 75:
        print("seventy-five")
    else:
        print("no match")

count = 0
while count < 5:
    n = input("enter an integer ")
    if int(n) == 99:
        print("Ninety-nine")
    elif int(n) == 75:
        print("seventy-five")
    else:
        print("no match")
    count += 1

y = 0
s = 120
while y < 30:
    s *= 1.01
    y += 1
print("In 30 years you will have ", s)