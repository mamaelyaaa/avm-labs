from Lab3.matrix import Matrix

with open('matrix.txt', 'r', encoding='utf-8') as input_file:
    A = [[float(i) for i in line.split()] for line in input_file.readlines()]


def method_kramer(matrix_a: list[list[float]], matrix_b: list[float]) -> list[float]:
    det = Matrix(matrix_a).determinant(matrix_a)
    x: list[float] = []

    for col in range(len(matrix_a)):
        mod_matrix: list[list[float]] = [matrix[:col] + [matrix_b[idx]] + matrix[col + 1:] for idx, matrix in
                                         enumerate(matrix_a)]

        det_i = Matrix(mod_matrix).determinant(mod_matrix)
        x.append(round(det_i / det, 3))

    return x


def method_simple_iteration(matrix_a: list[list[float]], matrix_b: list[float]) -> list[float]:
    def mod_matrix(matrix: list[list[float]]) -> list[list[float]]:
        n = len(matrix)
        m = len(matrix[0])

        for row in range(n):
            max_col = row

            for col in range(m - 1):
                if abs(matrix[row][col]) > abs(matrix[row][max_col]):
                    max_col = col

            if matrix[row][max_col] > matrix[max_col][max_col]:
                matrix[row], matrix[max_col] = matrix[max_col], matrix[row]

        return matrix

    new_matrix = mod_matrix(matrix_a)

    # Заполняем лямбду
    lam: list[float] = []
    for i in range(len(new_matrix)):
        sgn: int = 1 if new_matrix[i][i] >= 0 else -1
        lam.append(round((-sgn * 0.7) / (1 + abs(new_matrix[i][i])), 3))

    # Заполняем массив C
    matrix_c: list[list[float]] = new_matrix.copy()

    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            if i == j:
                matrix_c[i][j] = round(1 + lam[i] * new_matrix[i][j], 3)
            else:
                matrix_c[i][j] = round(lam[i] * new_matrix[i][j], 3)

    # Заполняем массив d
    matrix_d: list[float] = [round(-lam[i] * matrix_b[i], 3) for i in range(len(new_matrix))]

    for i in range(len(new_matrix)):
        matrix_d.append(round(-lam[i] * matrix_b[i], 3))

    print(matrix_c)
    print(matrix_d)

    x: list[float] = []
    # for i in range(len(new_matrix)):
    #     x_i =


print(method_simple_iteration(matrix_A, matrix_B))
