from collections import deque

hex_list = list('0123456789ABCDEF')


def fill():
    a = []
    for i in range(1000):
        for j in hex_list:
            a.append(j)
    return a


def numbers(val):
    for i, j in enumerate(hex_list):
        if j == val:
            return i


def val_modify(val):
    mult_num = 0
    mult_dict = {x: 16**x for x in range(7)}
    # mult_dict = {0: 1, 1: 16, 2: 256}
    val = deque(val.upper())
    val.reverse()
    for i, j in enumerate(val):
        mult_num += (numbers(j)) * mult_dict[i]
    return mult_num


# print(fill())
# print(val_modify(['A', 'B', 'C']))
print(val_modify('abcdf'))
