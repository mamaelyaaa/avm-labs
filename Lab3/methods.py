import numpy as np

from Lab3.matrix import Matrix
from math import log10


def method_kramer(matrix: Matrix) -> list[float]:
    matrix_a, matrix_b = matrix.submatrices()
    det = matrix.determinant(matrix_a)
    x: list[float] = []

    for col in range(matrix.get_rows):
        mod_matrix = [matrix[:col] + [matrix_b[idx]] + matrix[col + 1:] for idx, matrix in enumerate(matrix_a)]
        det_i = Matrix(mod_matrix).determinant(mod_matrix)
        x.append(round(det_i / det, 3))
    return x


def method_simple_iteration(matrix: Matrix, accuracy: float, x0: list[float]) -> list[float]:
    matrix.make_diagonally_dominant()
    print(matrix)
    matrix_a, matrix_b = matrix.submatrices()

    # Заполняем лямбду
    lam: list[float] = []
    for i in range(matrix.get_rows):
        sgn: int = 1 if matrix_a[i][i] >= 0 else -1
        lam.append(-sgn / (1 + abs(matrix_a[i][i])))

    # Заполняем массив C
    matrix_c: list[list[float]] = matrix_a.copy()

    for i in range(matrix.get_rows):
        for j in range(matrix.get_cols - 1):
            if i == j:
                matrix_c[i][j] = 1 + lam[i] * matrix_a[i][j]
            else:
                matrix_c[i][j] = lam[i] * matrix_a[i][j]

    # # Заполняем массив d
    matrix_d: list[float] = [-lam[i] * matrix_b[i] for i in range(matrix.get_rows)]

    x1 = np.matmul(matrix_c, x0) + matrix_d
    eigenvalues, _ = np.linalg.eig(matrix_c)
    spectral_radius = max(abs(eigenvalues))

    while max(abs(x1 - x0)) > accuracy and max(abs(np.matmul(matrix_a, x0) - matrix_b)) >= accuracy:
        x0 = x1
        x1 = np.matmul(matrix_c, x0) + matrix_d

    return np.round(x1, abs(int(log10(accuracy))))