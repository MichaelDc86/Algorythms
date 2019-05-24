# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
#  Это два абсолютно разных значения.

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
    min_in_randrange = -99
    array = []
    for _ in range(0, 10):
        array.append(random.randint(-99, 99))

    max_negative = min_in_randrange
    position = 0
    for n, j in enumerate(array):
        if j < 0 and abs(j) < abs(max_negative):
            max_negative = j
            position = n
    print(f'Массив: {array}\nМаксимальное отрицательное число: {max_negative}\nоно занимает {position} позицию')

    return vars()


main()

# 64 - разрядная ubuntu
# Python 3.6.7

# Результат

# Массив: [67, -77, 67, 79, -79, -25, -57, 65, 84, 69]
# Максимальное отрицательное число: -25
# оно занимает 5 позицию
# {'min_in_randrange': -99, 'array': [67, -77, 67, 79, -79, -25, -57, 65, 84, 69], '_': 9, 'max_negative': -25, 'position': 5, 'n': 9, 'j': 69}
# main
#  type=<class 'int'>, size=28, obj=-99
#  type=<class 'list'>, size=192, obj=[67, -77, 67, 79, -79, -25, -57, 65, 84, 69]
# 	 type=<class 'int'>, size=28, obj=67
# 	 type=<class 'int'>, size=28, obj=-77
# 	 type=<class 'int'>, size=28, obj=67
# 	 type=<class 'int'>, size=28, obj=79
# 	 type=<class 'int'>, size=28, obj=-79
# 	 type=<class 'int'>, size=28, obj=-25
# 	 type=<class 'int'>, size=28, obj=-57
# 	 type=<class 'int'>, size=28, obj=65
# 	 type=<class 'int'>, size=28, obj=84
# 	 type=<class 'int'>, size=28, obj=69
#  type=<class 'int'>, size=28, obj=9
#  type=<class 'int'>, size=28, obj=-25
#  type=<class 'int'>, size=28, obj=5
#  type=<class 'int'>, size=28, obj=9
#  type=<class 'int'>, size=28, obj=69
# Функция main затратила 640 байт памяти на переменные
