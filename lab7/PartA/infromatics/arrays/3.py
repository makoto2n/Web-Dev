N = int(input())
array = list(map(int, input().split()))

count_positive = 0

for num in array:
    if num > 0:
        count_positive += 1

print(count_positive)
