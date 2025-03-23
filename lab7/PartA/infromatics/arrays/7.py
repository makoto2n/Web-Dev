N = int(input())
array = list(map(int, input().split()))

left = 0
right = N - 1

while left < right:
    array[left], array[right] = array[right], array[left]
    left += 1
    right -= 1

print(*array)
