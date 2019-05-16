# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
#  Программа должна определить среднюю прибыль (за год для всех предприятий)
#  и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict


def inpt():
    firms_quantity_raw = input('Введите количество(целое число) предприятий: ')
    try:
        firms_quantity = int(firms_quantity_raw)
    except ValueError:
        print('Неверный формат числа предприятий!')
        inpt()
    firms_dict = defaultdict(list)

    for i in range(firms_quantity):
        firm_name = input(f'Введите название предприятия № {i+1}: ')
        for j in range(1, 5):
            income = input(f'Введите прибыль предприятия № {i+1} за {j} квартал: ')
            try:
                firms_dict[firm_name].append(float(income))
            except ValueError:
                print('Неверный формат прибыли!')
                inpt()
    return firms_dict


def count(prep_dict):
    if len(prep_dict) != 0:
        middle_val_dict = defaultdict(float)
        for k in prep_dict:
            middle_val_tmp = sum(prep_dict[k])/len(prep_dict[k])
            middle_val_dict[k] = middle_val_tmp

        middle_val = sum(list(middle_val_dict.values()))/len(middle_val_dict)
        lower_names = []
        higher_names = []
        for k in prep_dict:
            mid_tmp_val = sum(prep_dict[k])/4
            if mid_tmp_val > middle_val:
                higher_names.append(k)
            else:
                lower_names.append(k)

        print(f'Словарь всех фирм: {prep_dict}\n'
              f'Средняя прибыль за год(4 квартала) всех предприятий: {middle_val}\n'
              f'Названия предприятий, чья прибыль ниже средней: {lower_names}\n'
              f'Названия предприятий, чья прибыль выше средней: {higher_names}')


count(inpt())
