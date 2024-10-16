import numpy as np

from Lab3.matrix import Matrix


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
    matrix.rearrangement()
    matrix_a, matrix_b = matrix.submatrices()

    # Заполняем лямбду
    lam: list[float] = []
    for i in range(matrix.get_rows):
        sgn: int = 1 if matrix_a[i][i] >= 0 else -1
        lam.append(round(-sgn / (1 + abs(matrix_a[i][i])), abs(int(np.log10(accuracy)))))

    # Заполняем массив C
    matrix_c: list[list[float]] = matrix_a.copy()

    for i in range(matrix.get_rows):
        for j in range(matrix.get_cols - 1):
            if i == j:
                matrix_c[i][j] = round(1 + lam[i] * matrix_a[i][j], abs(int(np.log10(accuracy))))
            else:
                matrix_c[i][j] = round(lam[i] * matrix_a[i][j], abs(int(np.log10(accuracy))))

    # # Заполняем массив d
    matrix_d: list[float] = [round(-lam[i] * matrix_b[i], abs(int(np.log10(accuracy)))) for i in range(matrix.get_rows)]

    x1 = np.round(np.matmul(x0, matrix_c) + matrix_d, abs(int(np.log10(accuracy))))

    print(f'{x1 = }')
    # max(abs(np.matmul(matrix_a, x0) - matrix_b)) >= accuracy

    while max(abs(x1 - x0)) > accuracy:
        x0 = x1
        x1 = np.round(np.matmul(x0, matrix_c) + matrix_d, abs(int(np.log10(accuracy))))

    return x1