# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#  заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10


def merge(arr):
    if len(arr) < 2:
        return arr

    left = merge(arr[:len(arr)//2])
    right = merge(arr[len(arr)//2:])

    rez_arr = []

    while len(left) != 0 or len(right) != 0:
        if len(left) == 0:
            rez_arr.append(right[0])
        if len(right) == 0:
            rez_arr.append(right[0])
        if left[0] > right[0]:
            rez_arr.append(right.pop(0))
            rez_arr.append(left.pop(0))
        else:
            rez_arr.append(left.pop(0))
            rez_arr.append(right.pop(0))

    return rez_arr


array = [round(random.uniform(0, 50), 2) for i in range(SIZE)]
print(f'Исходный массив:        {array}')
print(f'Отсортированный массив: {merge(array)}')
print(f'Для сравнения:          {sorted(array)}')
