def Election(x, y, z):
    count_true = int(x) + int(y) + int(z)
    if count_true > 1:
        return True
    else:
        return False

# Чтение входных данных
x, y, z = map(int, input().split())

# Вывод результата
print(int(Election(x, y, z)))
