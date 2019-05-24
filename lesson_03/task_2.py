# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5, если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

first = [random.randint(-99, 99) for _ in range(0, random.randint(1, 30))]
second = []

for position, i in enumerate(first):
    if (i % 2) == 0:
        second.append(position)

print(f'Первый массив случайных чисел: {first}')
print(f'Второй массив, содержащий индексы четных элементов первого(нумерация с "0"): {second}')
