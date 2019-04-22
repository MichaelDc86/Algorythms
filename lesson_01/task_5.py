# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

x1 = input('Введите букву: x1 = ')
x2 = input('Введите вторую букву: x2 = ')

x1_position = ord(x1) - 96
x2_position = ord(x2) - 96
letters_between = abs(x1_position - x2_position) - 1

print(f'Позиция первой буквы: {x1_position}\n'
      f'Позиция второй буквы:  {x2_position}\n'
      f'Количество букв между заданными:  {letters_between}')
