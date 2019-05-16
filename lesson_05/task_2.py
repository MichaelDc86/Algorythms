# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]


from collections import deque

hex_list = list('0123456789ABCDEF')


def sum_matrix():
    a = deque(hex_list, maxlen=16)
    matrix = [hex_list]

    for i in hex_list:
        a.append('1'+i)
        matrix.append(list(a))
    matrix.pop()
    # list(map(lambda x: print(x), matrix))
    return matrix


def sum_vals(a, b):
    a = deque(a)
    a.reverse()
    b = deque(b)
    b.reverse()
    rez = []
    in_memo = 0

    def check_if_two(val, memo):
        if len(str(val)) == 2:
            memo += 1
            rez.append(list(str(val))[1])
        else:
            rez.append(val)
        return memo

    for i in range(min(len(a), len(b))):
        if in_memo != 0:
            tmp_summ_tmp = sum_matrix[numbers(a[i])][in_memo]
            in_memo = 0
            if len(str(tmp_summ_tmp)) == 2:
                in_memo += 1
                tmp_rez = sum_matrix[numbers(list(str(tmp_summ_tmp))[1])][numbers(b[i])]
                in_memo = check_if_two(tmp_rez, in_memo)
            else:
                tmp_rez = sum_matrix[numbers(tmp_summ_tmp)][numbers(b[i])]
                in_memo = check_if_two(tmp_rez, in_memo)
        else:
            tmp_summ = sum_matrix[numbers(a[i])][numbers(b[i])]
            in_memo = check_if_two(tmp_summ, in_memo)

    if len(a) != len(b):
        for j in range(min(len(a), len(b)), max(len(a), len(b))):
            try:
                if in_memo != 0:
                    tmp_rez = sum_matrix[in_memo][numbers(a[j])]
                    in_memo = 0
                    in_memo = check_if_two(tmp_rez, in_memo)
                else:
                    rez.append(a[j])
            except IndexError:
                if in_memo != 0:
                    tmp_rez = sum_matrix[in_memo][numbers(b[j])]
                    in_memo = 0
                    in_memo = check_if_two(tmp_rez, in_memo)
                else:
                    rez.append(b[j])
    if in_memo != 0:
        rez.append(str(in_memo))
    rez = deque(rez)
    rez.reverse()
    return list(rez)


sum_matrix = sum_matrix()


def numbers(val):
    for i, j in enumerate(hex_list):
        if j == val:
            return i


def val_modify(val):
    mult_num = 0
    mult_dict = {z: 16**z for z in range(7)}
    val = deque(val)
    val.reverse()
    for i, j in enumerate(val):
        mult_num += (numbers(j)) * mult_dict[i]
    return mult_num


def multiply(a, b):
    times_to_plus = val_modify(a)
    c = b
    for i in range(times_to_plus-1):
        c = sum_vals(c, b)
    return c


x = list(input('Введите первое число: ').upper())
print(x)
y = list(input('Введите второе число: ').upper())
print(y)

print('Сумма')
print(sum_vals(x, y))
print(''.join(sum_vals(x, y)))

print('Произведение')
print(multiply(x, y))
print(''.join(multiply(x, y)))


