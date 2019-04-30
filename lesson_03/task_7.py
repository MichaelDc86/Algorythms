# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random


def find_minimals(values):

    min_val = values[0]
    position = 0
    if len(min_val_array) == 2:
        return values.append(min_val)
    for n, i in enumerate(values):
        if i <= min_val:
            min_val = i
            position = n
    min_val_array.append(values.pop(position))
    find_minimals(values)
    return min_val_array


# создаем массив--------------------------
array = []
for _ in range(0, 10):
    array.append(random.randint(-100, 100))
# array = [1, 2, 3, 1]
# ----------------------------------------
min_val_array = []
print(f'Массив: {array}\nНаименьшие элементы массива: {find_minimals(array)}')
