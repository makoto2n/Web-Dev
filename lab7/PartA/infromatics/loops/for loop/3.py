from math import sqrt

a = int(input())
b = int(input())

for i in range(a, b+1):
    if int(sqrt(i))**2 == i:
        print(i)
