def min_four(a, b, c, d):
    return min(a, b, c, d)

# Чтение четырех чисел
a, b, c, d = map(int, input().split())

# Вывод результата
print(min_four(a, b, c, d))
