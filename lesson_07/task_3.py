# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

import random
from collections import deque

n = int(input('Введите натуральное число: '))

SIZE = 2 * n + 1
# SIZE = 7

array = [random.randint(-100, 101) for i in range(SIZE)]
# array = [56, -52, 100, -38, -38]


def median(arr):

    left, right = [], [SIZE]
    arr = deque(arr)
    med = 0

    def median_count(arr_inside, m):
        d = []
        u = []

        for i in arr_inside:
            if i <= m:
                d.append(i)
            if i > m:
                u.append(i)
        return d, u

    while len(left) != len(right):
        med = arr.pop()
        left, right = median_count(arr, med)
        arr.appendleft(med)

    return med


print(f'Исходный массив: {array}')
print(f'Медиана: {median(array)}')
