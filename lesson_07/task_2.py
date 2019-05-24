# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
rez_arr = []


def merge(arr):

    mid = len(arr) // 2

    f = arr[:mid]
    s = arr[mid:]

    def sort(first, last):
        if first > last:
            first, last = last, first
        return first, last

    if len(f) < 2 and len(s) < 2:
        tmp_arr = sort(f, s)

        if rez_arr:
            for i in range(len(tmp_arr)):
                if len(tmp_arr[i]) == 0:
                    continue
                j = 0
                while j < len(rez_arr) and tmp_arr[i][0] >= rez_arr[j]:
                    j += 1
                # rez_arr.insert(j, tmp_arr[i][0])  # очень хотелось сделать insert, так это просто, но скорость)))
                a = rez_arr[:j]
                a.append(tmp_arr[i][0])
                b = rez_arr[j:]
                rez_arr[:j] = a
                rez_arr[j+1:] = b

        if len(rez_arr) == 0:
            if tmp_arr[0]:
                rez_arr.append(tmp_arr[0][0])
                rez_arr.append(tmp_arr[1][0])
            else:
                rez_arr.append(tmp_arr[1][0])

        return

    merge(f)
    merge(s)

    return list(rez_arr)


array = [round(random.uniform(0, 50), 2) for i in range(SIZE)]
print(f'Исходный массив:        {array}')
print(f'Отсортированный массив: {merge(array)}')
print(f'Для сравнения:          {sorted(array)}')
