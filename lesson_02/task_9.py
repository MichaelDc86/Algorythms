# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def sum_count(val):
    sum_digits = 0
    for i in val:
        sum_digits += int(i)
    return sum_digits


def input_val():
    val = input('Введите число: ')
    if val == '0':
        return '0', '0'
    else:
        val_val = val
        val_sum = sum_count(val)
        val_sum_next, val_val_next = input_val()
        val_sum_next = sum_count(val_val_next)
        if val_sum >= val_sum_next:
            return val_sum, val_val
        return val_sum_next, val_val_next


digits_sum, digit = input_val()
print(f'Число {digit} имеет максимальную сумму входящих в него цифр, равную {digits_sum}')
