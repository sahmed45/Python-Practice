
m = []
s = []
for i in range(12):
    m.append(input("enter month"))
    s.append(input("enter sales for that month"))
    s[i] = int(s[i])

for i in range(12):
    print('{0} {1}'.format(m[i], s[i]))

total = sum(s)
average = total / 12
print("total sales are ", total)
print("average sale is ", average)
high = max(s)
low = min(s)
print('highest monthly sale is {0} lowest monthly sale is {1}'.format(high, low))