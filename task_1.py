# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input('Введите трехзначное число:  '))
a1 = a % 10
a2 = a % 100 // 10
a3 = a // 100
summ = a1 + a2 + a3
multiply = a1 * a2 * a3
print(f'Сумма: {summ}\nПроизведение: {multiply}')
