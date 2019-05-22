# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

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
    # print(func.__code__.)

    def wrapper(*args, **kwargs):

        if len(args) == 0:
            vars_dict = func()
        else:
            # print(args)
            # print(*args)
            print(func.__name__)
            values, min_val_array = args[0], args[1]
            if len(values) != 10:
                vars_dict = func(values, min_val_array)
        print(vars_dict)
        print(type(vars_dict))
        # memo_vol = 0
        # for key in vars_dict:
        #     key = vars_dict.get(key)
        #     memo_vol += show_size(key)[1]
        # print(f'Функция {func.__name__} затратила {memo_vol} байт памяти на переменные')

    return wrapper


@show_size_decor
def find_minimals(values, min_val_array):

    min_val = values[0]
    position = 0
    if len(min_val_array) == 2:
        return values.append(min_val)
    for n, i in enumerate(values):
        if i <= min_val:
            min_val = i
            position = n
    min_val_array.append(values.pop(position))
    find_minimals(values, min_val_array)
    return locals(), min_val_array


@show_size_decor
def main():
    array = []
    for _ in range(0, 10):
        array.append(random.randint(-99, 99))
    min_val_array = []
    print(f'Массив: {array}\nНаименьшие элементы массива: {find_minimals(array, min_val_array)[1]}')
    return locals()


main()
# print(main.__code__.)
# print(main.__getattr__('_'))
# print(main().keys())
# print(main().get('_'))
# print(main.__dir__())
# print(main.__get__())


# d = [i for i in range(10)]
# show_size(d)
# print(show_size(d)[1])
# find_minimals.
# v = 'Hallo!'
# show_size(v)
# f = {q: j for q in range(4) for j in range(3)}
# show_size(f)


# 64 - разрядная windows7
# Python 3.6.5
