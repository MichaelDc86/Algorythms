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
    def wrapper():
        vars_dict = func()

        memo_vol = 0
        for key in vars_dict:
            key = vars_dict.get(key)
            memo_vol += show_size(key)[1]
        print(f'Функция {func.__name__} затратила {memo_vol} байт памяти на переменные')

    return wrapper


def find_minimals(values, min_val_array):

    values = values.copy()
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
    for_memo_count, answer = find_minimals(array, min_val_array)
    print(f'Массив: {array}\nНаименьшие элементы массива: {answer}')
    print(locals())
    return locals()


main()


# --------------------------------------------------------Результаты-------------------------------------------------------
# 64 - разрядная ubuntu
# Python 3.6.7

# Результат

# Массив: [21, 13, 78, 18, -77, 65, -7, 30, 27, 63]
# Наименьшие элементы массива: [-77, -7]
# {'array': [21, 13, 78, 18, -77, 65, -7, 30, 27, 63], '_': 9, 'min_val_array': [-77, -7], 'for_memo_count': {'values': [21, 13, 78, 18, 65, -7, 30, 27, 63], 'min_val_array': [-77, -7], 'min_val': -77, 'position': 4, 'n': 9, 'i': 63}, 'answer': [-77, -7]}
#  type=<class 'list'>, size=192, obj=[21, 13, 78, 18, -77, 65, -7, 30, 27, 63]
# 	 type=<class 'int'>, size=28, obj=21
# 	 type=<class 'int'>, size=28, obj=13
# 	 type=<class 'int'>, size=28, obj=78
# 	 type=<class 'int'>, size=28, obj=18
# 	 type=<class 'int'>, size=28, obj=-77
# 	 type=<class 'int'>, size=28, obj=65
# 	 type=<class 'int'>, size=28, obj=-7
# 	 type=<class 'int'>, size=28, obj=30
# 	 type=<class 'int'>, size=28, obj=27
# 	 type=<class 'int'>, size=28, obj=63
#  type=<class 'int'>, size=28, obj=9
#  type=<class 'list'>, size=96, obj=[-77, -7]
# 	 type=<class 'int'>, size=28, obj=-77
# 	 type=<class 'int'>, size=28, obj=-7
#  type=<class 'dict'>, size=368, obj={'values': [21, 13, 78, 18, 65, -7, 30, 27, 63], 'min_val_array': [-77, -7], 'min_val': -77, 'position': 4, 'n': 9, 'i': 63}
# 	 type=<class 'str'>, size=55, obj=values
# 	 type=<class 'list'>, size=144, obj=[21, 13, 78, 18, 65, -7, 30, 27, 63]
# 		 type=<class 'int'>, size=28, obj=21
# 		 type=<class 'int'>, size=28, obj=13
# 		 type=<class 'int'>, size=28, obj=78
# 		 type=<class 'int'>, size=28, obj=18
# 		 type=<class 'int'>, size=28, obj=65
# 		 type=<class 'int'>, size=28, obj=-7
# 		 type=<class 'int'>, size=28, obj=30
# 		 type=<class 'int'>, size=28, obj=27
# 		 type=<class 'int'>, size=28, obj=63
# 	 type=<class 'str'>, size=62, obj=min_val_array
# 	 type=<class 'list'>, size=96, obj=[-77, -7]
# 		 type=<class 'int'>, size=28, obj=-77
# 		 type=<class 'int'>, size=28, obj=-7
# 	 type=<class 'str'>, size=56, obj=min_val
# 	 type=<class 'int'>, size=28, obj=-77
# 	 type=<class 'str'>, size=57, obj=position
# 	 type=<class 'int'>, size=28, obj=4
# 	 type=<class 'str'>, size=50, obj=n
# 	 type=<class 'int'>, size=28, obj=9
# 	 type=<class 'str'>, size=50, obj=i
# 	 type=<class 'int'>, size=28, obj=63
#  type=<class 'list'>, size=96, obj=[-77, -7]
# 	 type=<class 'int'>, size=28, obj=-77
# 	 type=<class 'int'>, size=28, obj=-7
# Функция main затратила 1854 байт памяти на переменные
