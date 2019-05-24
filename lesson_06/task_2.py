# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5, если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random
import sys


def show_size(x, level=0):
    memo_val = 0
    print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    memo_val += sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                memo_val += show_size(key, level + 1)[0]
                memo_val += show_size(value, level + 1)[0]
        elif not isinstance(x, str):
            for item in x:
                memo_val += show_size(item, level + 1)[0]

    return sys.getsizeof(x), memo_val


def show_size_decor(func):

    def wrapper(*args):

        if len(args) == 0:
            vars_dict = func()
            print(vars_dict)
            print(func.__name__)
        else:
            print(func.__name__)
            vars_dict = func(*args)
        memo_vol = 0
        for key in vars_dict:
            key = vars_dict.get(key)
            memo_vol += show_size(key)[1]
        print(f'Функция {func.__name__} затратила {memo_vol} байт памяти на переменные')

    return wrapper


@show_size_decor
def main():
    first = [random.randint(-99, 99) for _ in range(0, random.randint(1, 30))]
    second = []

    for position, i in enumerate(first):
        if (i % 2) == 0:
            second.append(position)

    print(f'Первый массив случайных чисел: {first}')
    print(f'Второй массив, содержащий индексы четных элементов первого(нумерация с "0"): {second}')

    return vars()


main()

# 64 - разрядная ubuntu
# Python 3.6.7

# Результат

# Первый массив случайных чисел: [-86, 93, -64, 39, 41, -23, -71, 8, -32, -16, 7, -1, -30, 74, 94, -68, 84, -7, 34, 45, 8, -47, -50, 69, 47]
# Второй массив, содержащий индексы четных элементов первого(нумерация с "0"): [0, 2, 7, 8, 9, 12, 13, 14, 15, 16, 18, 20, 22]
# {'first': [-86, 93, -64, 39, 41, -23, -71, 8, -32, -16, 7, -1, -30, 74, 94, -68, 84, -7, 34, 45, 8, -47, -50, 69, 47], 'second': [0, 2, 7, 8, 9, 12, 13, 14, 15, 16, 18, 20, 22], 'position': 24, 'i': 47}
# main
#  type=<class 'list'>, size=264, obj=[-86, 93, -64, 39, 41, -23, -71, 8, -32, -16, 7, -1, -30, 74, 94, -68, 84, -7, 34, 45, 8, -47, -50, 69, 47]
# 	 type=<class 'int'>, size=28, obj=-86
# 	 type=<class 'int'>, size=28, obj=93
# 	 type=<class 'int'>, size=28, obj=-64
# 	 type=<class 'int'>, size=28, obj=39
# 	 type=<class 'int'>, size=28, obj=41
# 	 type=<class 'int'>, size=28, obj=-23
# 	 type=<class 'int'>, size=28, obj=-71
# 	 type=<class 'int'>, size=28, obj=8
# 	 type=<class 'int'>, size=28, obj=-32
# 	 type=<class 'int'>, size=28, obj=-16
# 	 type=<class 'int'>, size=28, obj=7
# 	 type=<class 'int'>, size=28, obj=-1
# 	 type=<class 'int'>, size=28, obj=-30
# 	 type=<class 'int'>, size=28, obj=74
# 	 type=<class 'int'>, size=28, obj=94
# 	 type=<class 'int'>, size=28, obj=-68
# 	 type=<class 'int'>, size=28, obj=84
# 	 type=<class 'int'>, size=28, obj=-7
# 	 type=<class 'int'>, size=28, obj=34
# 	 type=<class 'int'>, size=28, obj=45
# 	 type=<class 'int'>, size=28, obj=8
# 	 type=<class 'int'>, size=28, obj=-47
# 	 type=<class 'int'>, size=28, obj=-50
# 	 type=<class 'int'>, size=28, obj=69
# 	 type=<class 'int'>, size=28, obj=47
#  type=<class 'list'>, size=192, obj=[0, 2, 7, 8, 9, 12, 13, 14, 15, 16, 18, 20, 22]
# 	 type=<class 'int'>, size=24, obj=0
# 	 type=<class 'int'>, size=28, obj=2
# 	 type=<class 'int'>, size=28, obj=7
# 	 type=<class 'int'>, size=28, obj=8
# 	 type=<class 'int'>, size=28, obj=9
# 	 type=<class 'int'>, size=28, obj=12
# 	 type=<class 'int'>, size=28, obj=13
# 	 type=<class 'int'>, size=28, obj=14
# 	 type=<class 'int'>, size=28, obj=15
# 	 type=<class 'int'>, size=28, obj=16
# 	 type=<class 'int'>, size=28, obj=18
# 	 type=<class 'int'>, size=28, obj=20
# 	 type=<class 'int'>, size=28, obj=22
#  type=<class 'int'>, size=28, obj=24
#  type=<class 'int'>, size=28, obj=47
# Функция main затратила 1572 байт памяти на переменные
