# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# Вариант с использованием рекурсии для поиска минимальных элементов

import random
# import timeit
import cProfile


def find_minimals(values):

    min_val = values[0]
    position = 0
    if len(min_val_array) == 2:
        return None
    for n, i in enumerate(values):
        if i <= min_val:
            min_val = i
            position = n
    min_val_array.append(values.pop(position))
    find_minimals(values)
    return min_val_array


# создаем массив--------------------------
def fill_in_array():
    array_ = []
    for _ in range(1000):
        array_.append(random.randint(-99, 99))
    return array_
# ----------------------------------------


min_val_array = []


def main():
    array = fill_in_array()
    # print_array = array.copy()
    minimals = find_minimals(array)
    # print(f'Массив: {print_array}\nНаименьшие элементы массива: {minimals}')


# main()
# rez = """main()"""
# print(timeit.timeit(rez, number=100, globals=globals()))

# Результаты замеров---------------------------------------------

# длина массива - 1000
# python3 -m timeit -n 1000 -s "import task_1" "task_1.main()"
# 1000 loops, best of 3: 771 usec per loop

# --------------------------------------

# длина массива - 2000
# python3 -m timeit -n 1000 -s "import task_1" "task_1.main()"
# 1000 loops, best of 3: 1.54 msec per loop

# ---------------------------------------
# длина массива - 4000
# python3 -m timeit -n 1000 -s "import task_1" "task_1.main()"
# 1000 loops, best of 3: 3.07 msec per loop

# длина массива - 10000
# python3 -m timeit -n 1000 -s "import task_1" "task_1.main()"
# 1000 loops, best of 3: 7.81 msec per loop

# По результатам 3 первых замеров делаю вывод, что алгоритм обладает асимптотикой О(n)
# Основное время тартится на заполнение массива.

# cProfile.run('main()')

# длина массива - 1000
# 3/1    0.000    0.000    0.000    0.000 task_1.py:11(find_minimals)
# 1      0.003    0.003    0.011    0.011 task_1.py:27(fill_in_array)
# 1      0.000    0.000    0.012    0.012 task_1.py:39(main)
# длина массива - 2000
# 3/1    0.000    0.000    0.000    0.000 task_1.py:11(find_minimals)
# 1      0.005    0.005    0.021    0.021 task_1.py:27(fill_in_array)
# 1      0.000    0.000    0.022    0.022 task_1.py:39(main)
# длина массива - 4000
# 3/1    0.001    0.000    0.001    0.001 task_1.py:11(find_minimals)
# 1      0.006    0.006    0.027    0.027 task_1.py:27(fill_in_array)
# 1      0.000    0.000    0.027    0.027 task_1.py:39(main)
# длина массива - 10000
# 3/1    0.002    0.001    0.002    0.002 task_1.py:11(find_minimals)
# 1      0.014    0.014    0.066    0.066 task_1.py:27(fill_in_array)
# 1      0.000    0.000    0.068    0.068 task_1.py:39(main)
