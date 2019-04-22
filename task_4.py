# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число, случайное вещественное число, случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f',
# то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

choice = int(input('Выберите вариант диапазона:\n1 - целые числа\n2 - вещественные числа\n3 - строчные буквы\n'))
x1 = input('Введите левую границу диапазона(целое число, вещественное число или строчная буква):\nх1 = ')
x2 = input('Введите правую границу диапазона(целое число, вещественное число или строчная буква):\nх2 = ')

if choice == 1:
    rand_val = random.randint(int(x1), int(x2))
elif choice == 2:
    rand_val = random.uniform(float(x1), float(x2))
    rand_val = float('{:.2f}'.format(rand_val))
else:
    x1 = ord(x1)
    x2 = ord(x2)
    rand_val = chr(random.randint(x1, x2))

print(f'Случайная величина: {rand_val}')
