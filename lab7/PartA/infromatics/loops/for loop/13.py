n = int(input())
cnt = 0
for i in range(0, n):
    a = int(input())
    cnt += 1 if a==0 else 0
print(cnt)