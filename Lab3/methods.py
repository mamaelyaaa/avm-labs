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


def method_simple_iteration(matrix: np.ndarray, x0: np.array, accuracy: float) -> tuple[np.array, int, list]:
    n, m = np.shape(matrix)

    matrix_a, vector_b = submatrices(matrix)

    matrix_a[[4, 5]] = matrix_a[[5, 4]]

    matrix_D = np.array([[15 if i == j else 1 for j in range(7)] for i in range(7)])
    matrix_b = np.linalg.inv(matrix_a) @ matrix_D
    matrix_d = matrix_b * vector_b

    matrix_a, vector_b = matrix_D, matrix_d

    # Диагонально преобладающая матрица
    stable = False
    while not stable:
        stable = True

        for row in range(n):
            max_index = np.argmax(np.abs(matrix[row, :-1]))

            if max_index != row and abs(matrix[row, max_index]) > abs(matrix[max_index, max_index]):
                matrix[[row, max_index], :] = matrix[[max_index, row], :]
                stable = False
                break


    # Заполняем лямбду
    vector_lambda = np.array([-1 * (np.sign(matrix_ii) / (1 + abs(matrix_ii))) for matrix_ii in matrix_a.diagonal()])
    print(vector_lambda)
    matrix_c = np.array([[1 + vector_lambda[i] * matrix_a[i, j] if i == j else vector_lambda[i] * matrix_a[i, j]
                          for j in range(m - 1)]
                          for i in range(n)])

    print(max(abs(np.linalg.eig(matrix_c)[0])))

    if max(abs(np.linalg.eig(matrix_c)[0])) > 1:
        raise Exception("Достаточное условие не сходится")

    vector_d = np.array([-1 * vector_lambda[i] * vector_b[i] for i in range(n)])

    x1 = (matrix_c @ x0) + vector_d
    iteration = 1
    intermediate_cache: list = [x1]

    while np.max(abs(x1 - x0)) > accuracy and np.max(abs(vector_b - (matrix_a @ x1))) >= accuracy:
        x0 = x1
        x1 = (matrix_c @ x0) + vector_d
        iteration += 1
        intermediate_cache.append(x1)

    return np.round(x1, int(abs(np.log10(accuracy)))), iteration, intermediate_cache
