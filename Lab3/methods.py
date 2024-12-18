from math import ceil

import numpy as np


def submatrices(matrix: np.ndarray) -> tuple:
    matrix_a = matrix[:, :-1]
    vector_b = matrix[:, -1]
    return matrix_a, vector_b


def method_kramer(matrix: np.ndarray) -> np.ndarray:
    matrix_a, vector_b = submatrices(matrix)
    det = np.linalg.det(matrix_a)

    x: list[float] = []

    for col in range(len(matrix)):
        mod_matrix = matrix_a.copy()
        mod_matrix[:, col] = vector_b

        det_i = np.linalg.det(mod_matrix)

        x.append(float(round(det_i / det, 3)))

    return np.array(x)


def method_simple_iteration(matrix: np.array, x0: np.array, accuracy: float) -> tuple[np.array, int, list]:
    n, m = np.shape(matrix)

    matrix_a, vector_b = submatrices(matrix)

    # Преобразование в диагонально преобладающую
    matrix_D = np.array([[5 if i == j else 1 for j in range(6)] for i in range(6)])
    matrix_B = matrix_D @ np.linalg.inv(matrix_a)
    matrix_d = matrix_B @ vector_b

    matrix_a, vector_b = matrix_D, matrix_d

    # Заполняем лямбду
    vector_lambda = np.array([-1 * (np.sign(matrix_ii) / (1 + abs(matrix_ii))) for matrix_ii in matrix_a.diagonal()])

    matrix_c = np.array([[1 + vector_lambda[i] * matrix_a[i, j] if i == j else vector_lambda[i] * matrix_a[i, j]
                          for j in range(m - 1)]
                         for i in range(n)])

    if max(abs(np.linalg.eig(matrix_c)[0])) > 1:
        raise Exception("Достаточное условие не сходится")

    vector_d = np.array([-1 * vector_lambda[i] * vector_b[i] for i in range(n)])

    x1 = (matrix_c @ x0) + vector_d
    iteration = 1
    intermediate_cache: list = [x1]

    while np.max(abs(x1 - x0)) > accuracy and np.max(abs(vector_b - (matrix_a @ x1))) >= accuracy:
        prev_diff = np.max(abs(x1 - x0))

        if np.max(abs(x1 - x0)) < prev_diff:
            break

        x0 = x1
        x1 = (matrix_c @ x0) + vector_d
        iteration += 1
        intermediate_cache.append(x1)

    return np.round(x1, ceil(np.abs(np.log10(accuracy)))), iteration, intermediate_cache
