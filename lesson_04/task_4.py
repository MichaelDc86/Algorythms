# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

# С использованием решета Эратосфена

import cProfile


def sieve(k):

    def fill_array_(n):
        array = [i for i in range(n+1)]
        array[1] = 0
        for i in range(2, n+1):
            if array[i] != 0:
                j = i + i
                while j < n + 1:
                    array[j] = 0
                    j += i

        return list(filter(lambda x: x != 0, array))  # list(set(array))

    k_stop = k
    while True:
        prime_array = fill_array_(k)
        if len(prime_array) >= k_stop:
            break
        k += 1

    return prime_array, prime_array[-1]


# a, b = sieve(100)
# print(f'{a}\n{len(a)}\n{b}')

# Результаты замеров---------------------------------------------


# ------------------------------------------------
# python3 -m timeit -n 1000 -s "import task_4" "task_4.sieve(10)"
# 1000 loops, best of 3: 87.8 usec per loop
# ------------------------------------------------
# python3 -m timeit -n 1000 -s "import task_4" "task_4.sieve(20)"
# 1000 loops, best of 3: 490 usec per loop
# ------------------------------------------------
# python3 -m timeit -n 1000 -s "import task_4" "task_4.sieve(40)"
# 1000 loops, best of 3: 2.96 msec per loop
# ------------------------------------------------
# python3 -m timeit -n 1000 -s "import task_4" "task_4.sieve(100)"
# 1000 loops, best of 3: 33.3 msec per loop

# cProfile.run('sieve(10)')
# 1    0.000    0.000    0.000    0.000 task_4.py:10(sieve)
# 20   0.000    0.000    0.000    0.000 task_4.py:12(fill_array_)
# 20   0.000    0.000    0.000    0.000 task_4.py:13(<listcomp>)
# 410  0.000    0.000    0.000    0.000 task_4.py:22(<lambda>)

# cProfile.run('sieve(20)')
# 1    0.000    0.000    0.001    0.001 task_4.py:10(sieve)
# 52   0.001    0.000    0.001    0.000 task_4.py:12(fill_array_)
# 52   0.000    0.000    0.000    0.000 task_4.py:13(<listcomp>)
# 2418 0.000    0.000    0.000    0.000 task_4.py:22(<lambda>)

# cProfile.run('sieve(40)')
# 1     0.000    0.000    0.004    0.004 task_4.py:10(sieve)
# 134   0.003    0.000    0.004    0.000 task_4.py:12(fill_array_)
# 134   0.000    0.000    0.000    0.000 task_4.py:13(<listcomp>)
# 14405 0.001    0.000    0.001    0.000 task_4.py:22(<lambda>)

# cProfile.run('sieve(100)')
# 1      0.000    0.000    0.047    0.047 task_4.py:10(sieve)
# 442    0.036    0.000    0.046    0.000 task_4.py:12(fill_array_)
# 442    0.003    0.000    0.003    0.000 task_4.py:13(<listcomp>)
# 142103 0.008    0.000    0.008    0.000 task_4.py:22(<lambda>)

# Вывод: На мой взгляд(результаты 3 замеров), алгоритм обладает нелинейной асимптотикой. До n**2 не дотягивает,
# похож на n*log(n). Сначала нолики удалял с помощью set, но оно неупорядоченное и терял нужный элемент,
# пршлось через filter делать.
