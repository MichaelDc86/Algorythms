# import random
# n = input('Введите число(размер массива): ')
# a = [random.randint(0, 1000000000) for _ in range(int(n))]
# final_dict = {}
# final_list = []
# print(a)
#
# for i in a:
#     times = 0
#     for j in a:
#         if j == i:
#             times += 1
#     if times > 1:
#         final_dict[i] = times
# try:
#     max_times = max(final_dict.values())
# except ValueError:
#     print('Ни один элемент не повторяется')
#
# for x in final_dict.keys():
#     if final_dict[x] == max_times:
#         final_list.append(x)
# print(final_list)

n = input('Введите число(размер массива): ')
array = input('Введите числа - элементы массива: ')
final_dict = {}
final_list = []


def count(a):
    for i in a:
        times = 0
        for j in a:
            if j == i:
                times += 1
        if times > 1:
            final_dict[i] = times
    try:
        max_times = max(final_dict.values())
    except ValueError:
        print('Ни один элемент не повторяется')

    for x in final_dict.keys():
        if final_dict[x] == max_times:
            final_list.append(x)
    return int(max(final_list))


print(count(array))


rez = count(array)
print(rez)
