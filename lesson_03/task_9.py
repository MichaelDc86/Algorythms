# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = [[random.randint(-10, 10) for j in range(0, 4)] for i in range(0, 4)]


def find_max_min_element(tmp_matrix):
    min_element = tmp_matrix[0][0]
    max_element = tmp_matrix[0][0]
    for j in range(0, (len(tmp_matrix[0])+1)):
        for i in range(0, (len(tmp_matrix)+1)):
            if tmp_matrix[i][j] <= min_element:
                min_element = tmp_matrix[i][j]
        if min_element >= max_element:
            max_element = min_element
    return max_element


print(matrix, find_max_min_element(matrix))
