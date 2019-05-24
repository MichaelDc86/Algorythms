# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
#  Сами минимальный и максимальный элементы в сумму не включать.

import random

# создаем массив--------------------------

array = []
for _ in range(0, 10):
    array.append(random.randint(-100, 100))

# array = [1, 2, 3, 4, 5, 6, 7]
# array = [0, 0]

min_val = array[0]
max_val = array[0]
min_val_position = 0
max_val_position = 0
sum_between = 0
for n, i in enumerate(array):
    # ищем минимальный--------------------
    if i <= min_val:
        min_val = i
        min_val_position = n
    # ищем максимальный-------------------
    elif i > max_val:
        max_val = i
        max_val_position = n

# ищем сумму между минимумом и максимумом

if max_val_position - min_val_position >= 0:
    step = 1
else:
    step = -1
for i in range((min_val_position+step), max_val_position, step):
    sum_between += array[i]

print(f'Array: {array}\n'
      f'Minimal_val: {min_val}; position: {min_val_position}\n'
      f'Maximum_val: {max_val}; position: {max_val_position}\n'
      f'Sum between Min and Max: {sum_between}')
