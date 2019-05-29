# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
# func("papa")
# 6
# func("sova")
# 9

import hashlib

string_inp = input('Введите строку: ')


def sub_string_count(string):
    subs_array = []
    subs_num = 0
    h_str = hashlib.sha1(string.encode('utf-8')).hexdigest()
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            # print(string[i:j])
            h_subs = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            if h_subs not in subs_array and h_subs != h_str:
                subs_array.append(h_subs)
                subs_num += 1

    return subs_num


print(sub_string_count(string_inp))
