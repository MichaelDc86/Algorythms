# Вывести наэкран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127 - м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке..


def print_symbol(symbol_code):
    if (symbol_code - 2) % 10 == 0:
        print()
    print(f'{symbol_code}-{chr(symbol_code)}  ', end='')


# -----Цикл---------
#
#
# start = 32
# end = 127
#
# for i in range(start, (end+1)):
#     print_symbol(i)

# -----Рекурсия---------


start = 32
end = 127


def main_print(n):
    if n == end:
        print_symbol(n)
        return None
    print_symbol(n)
    main_print(n+1)


main_print(start)
