# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

# Без использования решета Эратосфена

import cProfile


def prime(k):
    prime_array = []
    i = 2
    while len(prime_array) < k:
        check = 0
        for j in range(2, i+1):
            if i % j == 0 and i != j:
                check = 1
                break

        if check == 0:
            prime_array.append(i)
        i += 1

    return prime_array, prime_array[-1]


# a, b = prime(100)
# print(f'{a}\n{len(a)}\n{b}')

# Результаты замеров---------------------------------------------


# ------------------------------------------------
# python3 -m timeit -n 1000 -s "import task_5" "task_5.prime(10)"
# 1000 loops, best of 3: 12.4 usec per loop
# ------------------------------------------------
# python3 -m timeit -n 1000 -s "import task_5" "task_5.prime(20)"
# 1000 loops, best of 3: 42 usec per loop
# ------------------------------------------------
# python3 -m timeit -n 1000 -s "import task_5" "task_5.prime(40)"
# 1000 loops, best of 3: 155 usec per loop
# ------------------------------------------------
# python3 -m timeit -n 1000 -s "import task_5" "task_5.prime(100)"
# 1000 loops, best of 3: 998 usec per loop

# cProfile.run('prime(10)')
# 1    0.000    0.000    0.000    0.000 task_5.py:10(prime)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 29   0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 10   0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('prime(20)')
# 1    0.000    0.000    0.000    0.000 task_5.py:10(prime)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 71   0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 20   0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('prime(40)')
# 1    0.001    0.001    0.001    0.001 task_5.py:10(prime)
# 1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
# 173  0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 40   0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('prime(100)')
# 1    0.002    0.002    0.002    0.002 task_5.py:10(prime)
# 1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
# 541  0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 100  0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# Вывод: По результатам 3 первых замеров делаю вывод, что алгоритм обладает асимптотикой О(n).
# Этот алгоритм быстрее алгоритма с использованием решета Эратосфена(в моем исполнении).
