# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

# Пробовал сначала по шагам, все отдельно. Но получилось много проходов по матрице, сократил.


def fill_the_matrix():
    line = []
    new_sum = 0
    if len(matrix) > 3:
        return matrix
    for _ in range(0, 4):
        digit = int(input('Введите число(элемент матрицы): '))
        line.append(digit)
        new_sum += digit
    line.append(new_sum)
    matrix.append(line)
    fill_the_matrix()
    return matrix


# def line_modify(tmp_line):
#     line_sum = 0
#     for _ in tmp_line:
#         print(_, end=' ')
#         line_sum += _
#     print(line_sum)
#     return tmp_line.append(line_sum)
#
#
# def matrix_modify(tmp_matrix):
#     for _ in tmp_matrix:
#         line_modify(_)
#     return tmp_matrix


def print_matrix(tmp_matrix):
    for i in tmp_matrix:
        for j in i:
            print(j, end=' ')
        print()


matrix = []
print_matrix(fill_the_matrix())
# matrix_modify(fill_the_matrix())
# print_matrix(matrix_modify(fill_the_matrix()))
