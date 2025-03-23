N = int(input())

while N > 1:
    if N % 2 != 0:
        print("NO")
        break
    N //= 2
else:
    print("YES")
