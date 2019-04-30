# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = [[random.randint(-10, 10) for j in range(0, 4)] for i in range(0, 4)]


def find_max_min_element(tmp_matrix):
    min_element = tmp_matrix[0][0]
    for i in tmp_matrix:
        if i[0] <= min_element:
            min_element = i[0]
    return min_element


print(matrix, find_max_min_element(matrix))
