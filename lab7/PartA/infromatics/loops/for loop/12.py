a = input()
res = 0
index = len(a)-1
for i in a:
    if i=='1':
        res+=pow(2, index)
    index-=1
print(res)