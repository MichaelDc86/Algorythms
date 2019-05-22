# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#  заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10


def merge(arr):
    tmp = []
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    # tmp.extend(arr[:mid])
    # tmp.extend(arr[mid:])
    left = arr[:mid]
    right = arr[mid:]
    tmp.append(left)
    tmp.append(right)

    for i in tmp:
        print(merge(i))
    # if len(left) > 1:
    #     merge(left)
    #     print(left)
    # if len(right) > 1:
    #     merge(right)
    #     print(right)


    # print(left)
    # print(right)



array = [round(random.uniform(0, 50), 2) for i in range(SIZE)]
print(f'Исходный массив:        {array}')
print(f'Отсортированный массив: {merge(array)}')
print(f'Для сравнения:          {sorted(array)}')
