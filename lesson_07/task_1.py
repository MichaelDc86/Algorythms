# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
#  заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10


def bubble(arr):
    first_bubble = 1
    decision = 0

    for j in range(len(arr)-1):
        if arr[j] < arr[j+1]:
            decision = 1
            first_bubble = j  # закомментировать для перехода к классическому пузырьку
            break

    if decision:
        while first_bubble <= len(arr):
            for i in range(len(arr)-1):
                if arr[i] < arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            # print(arr)
            first_bubble += 1
        return arr
    else:
        return 'Массив уже отсортирован', arr


array = [random.randint(-100, 99) for i in range(SIZE)]
# array = [60, 50, 45, 40, 37, 4, -37, -37, -46, -70]  # отсортированный массив для проверки
# array = [84, 83, 82, 44, 55, -6, 58, 17, 59, -71]  # для проверки ускорения("ума")

print(f'Исходный массив:        {array}')
print(f'Отсортированный массив: {bubble(array)}')
print(f'Для сравнения:          {sorted(array, reverse=True)}')
