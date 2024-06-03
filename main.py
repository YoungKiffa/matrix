import random


# Создает матрицу заданного размера
def create_matrix(rows, cols):
    matrix = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]
    return matrix


# Устанавливает значение элемента матрицы
def set_element(matrix, row, col, value):
    matrix[row][col] = value


# Возвращает значение элемента матрицы
def get_element(matrix, row, col):
    return matrix[row][col]


# Возвращает новую матрицу
def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

# возвращает новую матрицу, которая является транспонированной версией переданной матрицы
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Проверяет, равны ли две матрицы matrix1 и matrix2
def is_equal(matrix1, matrix2):
    return all(row1 == row2 for row1, row2 in zip(matrix1, matrix2))


def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Матрица не квадратная")
    else:
        pass
