# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

     # 0123456789ABCDEF
     # 123456789ABCDEF10
     # 2,2,4,6,8,A,C,E,10,12,14,16,18,1A,1C,1E
     # 3,3,6,9,C,
     # 4
     # 5
     # 6
     # 7
     # 8
     # 9
     # A
     # B
     # C
     # D
     # E
     # F
from collections import deque


def sum_matrix():
    a = deque('0123456789ABCDEF', maxlen=16)
    b = list('0123456789ABCDEF')
    matrix = [b]

    for i in b:
        a.append('1'+i)
        matrix.append(list(a))
    matrix.pop()
    list(map(lambda x: print(x), matrix))
    return matrix


# sum_matrix()
print(sum_matrix()[2][10])
# x = list(input('Введите первое число: '))
# y = list(input('Введите второе число: '))


