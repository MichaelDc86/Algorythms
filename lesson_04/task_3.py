# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# Вариант с использованием встроенной функции min() для поиска минимальных элементов и генератора
# списков для создания массива

import random
# import timeit
import cProfile


def find_minimals(values):
    min_val_array = []
    for t in range(2):
        min_val_array.append(values.pop(values.index(min(values))))
    return min_val_array


# создаем массив--------------------------
def fill_in_array():
    array_ = [random.randint(-99, 99) for _ in range(10000)]
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
# python3 -m timeit -n 1000 -s "import task_3" "task_3.main()"
# 1000 loops, best of 3: 795 usec per loop
# длина массива - 2000
# python3 -m timeit -n 1000 -s "import task_3" "task_3.main()"
# 1000 loops, best of 3: 1.56 msec per loop
# длина массива - 4000
# python3 -m timeit -n 1000 -s "import task_3" "task_3.main()"
# 1000 loops, best of 3: 3.14 msec per loop
# длина массива - 10000
# python3 -m timeit -n 1000 -s "import task_3" "task_3.main()"
# 1000 loops, best of 3: 7.96 msec per loop

# По результатам 3 первых замеров делаю вывод, что алгоритм обладает асимптотикой О(n).
# При сравнении 3 алгоритмов делаю вывод, что они работают приблизительно с одинаковой скоростью.
# Основное время тартится на заполнение массива.

# cProfile.run('main()')

# длина массива - 1000
# 1    0.000    0.000    0.000    0.000 task_3.py:12(find_minimals)
# 1    0.000    0.000    0.001    0.001 task_3.py:20(fill_in_array)
# 1    0.000    0.000    0.001    0.001 task_3.py:21(<listcomp>)
# 1    0.000    0.000    0.002    0.002 task_3.py:26(main)
# длина массива - 2000
# 1    0.000    0.000    0.000    0.000 task_3.py:12(find_minimals)
# 1    0.000    0.000    0.003    0.003 task_3.py:20(fill_in_array)
# 1    0.000    0.000    0.003    0.003 task_3.py:21(<listcomp>)
# 1    0.000    0.000    0.003    0.003 task_3.py:26(main)
# длина массива - 4000
# 1    0.000    0.000    0.000    0.000 task_3.py:12(find_minimals)
# 1    0.000    0.000    0.006    0.006 task_3.py:20(fill_in_array)
# 1    0.001    0.001    0.006    0.006 task_3.py:21(<listcomp>)
# 1    0.000    0.000    0.006    0.006 task_3.py:26(main)
# длина массива - 10000
# 1    0.000    0.000    0.000    0.000 task_3.py:12(find_minimals)
# 1    0.000    0.000    0.013    0.013 task_3.py:20(fill_in_array)
# 1    0.002    0.002    0.013    0.013 task_3.py:21(<listcomp>)
# 1    0.000    0.000    0.014    0.014 task_3.py:26(main)
