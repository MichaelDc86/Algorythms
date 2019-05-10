# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
#  Это два абсолютно разных значения.

import random

# создаем массив--------------------------

array = []
for _ in range(0, 10):
    array.append(random.randint(-99, 99))
# print(array)

# ищем макс отрицательное-----------------

max_negative = array[0]
position = 0
for n, j in enumerate(array):
    if j < 0 and abs(j) < abs(max_negative):
        max_negative = j
        position = n
print(f'Массив: {array}\nМаксимальное отрицательное число: {max_negative}\nоно занимает {position} позицию')
