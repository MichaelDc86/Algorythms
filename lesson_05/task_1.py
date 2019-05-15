# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
#  Программа должна определить среднюю прибыль (за год для всех предприятий)
#  и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import Counter
from collections import defaultdict


def inpt():
    firms_quantity = input('Введите количество(целое число) предприятий: ')
    firms_dict = defaultdict(list)

    for i in range(int(firms_quantity)):
        firms_income = []
        firm_name = input(f'Введите название предприятия № {i+1}: ')
        for j in range(1, 5):
            income = input(f'Введите прибыль предприятия № {i+1} за {j} квартал: ')
            firms_income.append(int(income))
        firms_dict[firm_name] = firms_income
    return firms_dict


prep_dict = inpt()
summa = 0
for k in prep_dict:
    summa += sum(prep_dict[k])

middle_val = summa/len(prep_dict)
lower_names = []
higher_names = []
for k in prep_dict:
    mid_tmp_val = sum(prep_dict[k])/4
    if mid_tmp_val > middle_val:
        higher_names.append(k)
    else:
        lower_names.append(k)

print(f'{prep_dict}\n{middle_val}\n{lower_names}\n{higher_names}')

# print(prep_dict)
