# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = [[random.randint(-10, 10) for j in range(0, 4)] for i in range(0, 4)]


def find_max_in_min_elements(tmp_matrix):

    max_element = 0  # tmp_matrix[0][0]
    for j in range(0, len(tmp_matrix[0])):
        min_element = tmp_matrix[0][j]

        for i in range(0, len(tmp_matrix)):

            if tmp_matrix[i][j] <= min_element:
                min_element = tmp_matrix[i][j]

        if j == 0 or min_element >= max_element:
            max_element = min_element

        # print(min_element, max_element)
    return max_element


print(matrix, find_max_in_min_elements(matrix))
