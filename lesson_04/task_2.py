# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# Вариант с использованием цикла для поиска минимальных элементов

import random
# import timeit
import cProfile


def find_minimals(values):
    min_val_array = []
    for t in range(2):
        pos = 0
        min_val = values[0]
        for i, j in enumerate(values):
            if j <= min_val:
                min_val = j
                pos = i
        min_val_array.append(values.pop(pos))
    return min_val_array


# создаем массив--------------------------
def fill_in_array():
    array_ = []
    for _ in range(10000):
        array_.append(random.randint(-99, 99))
    return array_
# ----------------------------------------


def main():
    array = fill_in_array()
    # print_array = array.copy()
    minimals = find_minimals(array)
    # print(f'Массив: {print_array}\nНаименьшие элементы массива: {minimals}')


main()
# rez = """main()"""
# print(timeit.timeit(rez, number=100, globals=globals()))

# Результаты замеров---------------------------------------------

# длина массива - 1000
# python3 -m timeit -n 1000 -s "import task_2" "task_2.main()"
# 1000 loops, best of 3: 850 usec per loop
# длина массива - 2000
# python3 -m timeit -n 1000 -s "import task_2" "task_2.main()"
# 1000 loops, best of 3: 1.72 msec per loop
# длина массива - 4000
# python3 -m timeit -n 1000 -s "import task_2" "task_2.main()"
# 1000 loops, best of 3: 3.45 msec per loop
# длина массива - 10000
# python3 -m timeit -n 1000 -s "import task_2" "task_2.main()"
# 1000 loops, best of 3: 8.58 msec per loop

# По результатам 3 первых замеров делаю вывод, что алгоритм обладает асимптотикой О(n). Hо данный алгоритм медленнее,
# чем в task_1.
# Основное время тартится на заполнение массива.

# cProfile.run('main()')

# длина массива - 1000
# 1    0.000    0.000    0.000    0.000 task_2.py:11(find_minimals)
# 1    0.004    0.004    0.017    0.017 task_2.py:25(fill_in_array)
# 1    0.000    0.000    0.017    0.017 task_2.py:34(main)
# длина массива - 2000
# 1    0.001    0.001    0.001    0.001 task_2.py:11(find_minimals)
# 1    0.004    0.004    0.020    0.020 task_2.py:25(fill_in_array)
# 1    0.000    0.000    0.020    0.020 task_2.py:34(main)
# длина массива - 4000
# 1    0.001    0.001    0.001    0.001 task_2.py:11(find_minimals)
# 1    0.005    0.005    0.023    0.023 task_2.py:25(fill_in_array)
# 1    0.000    0.000    0.023    0.023 task_2.py:34(main)
# длина массива - 10000
# 1    0.002    0.002    0.002    0.002 task_2.py:11(find_minimals)
# 1    0.013    0.013    0.060    0.060 task_2.py:25(fill_in_array)
# 1    0.000    0.000    0.062    0.062 task_2.py:34(main)
