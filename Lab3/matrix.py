class Matrix:

    def __init__(self, matrix: list[list[float]]):
        self._matrix = matrix
        self._n: int = len(self._matrix)
        self._m: int = len(self._matrix[0])

    def __str__(self) -> str:
        return '\n'.join([' '.join(map(str, i)) for i in self._matrix])

    def submatrices(self, matrix: list[list[float]]) -> None:
        matrix_a: list[list[float]] = []
        matrix_b: list[float] = []

        for i in range(self._n):
            *matrix_a_i, matrix_b_i = matrix[i]

            matrix_a.append(matrix_a_i)
            matrix_b.append(matrix_b_i)

        self._matrix_a = matrix_a
        self._matrix_b = matrix_b

    @staticmethod
    def minor(matrix, row, col) -> list[list[float]]:
        return [i[:col] + i[col + 1:] for i in matrix[:row] + matrix[row + 1:]]

    def determinant(self, matrix: list[list[float]]) -> float:
        n = len(matrix)

        if n == 1:
            return matrix[0][0]

        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = 0
        for col in range(n):
            sign = (-1) ** col
            det += sign * matrix[0][col] * self.determinant(self.minor(matrix, 0, col))
        return det
