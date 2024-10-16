class Matrix:
    def __init__(self, matrix: list[list[float]]):
        self.__matrix = matrix
        self.__n: int = len(self.__matrix)
        self.__m: int = len(self.__matrix[0])

    def __str__(self) -> str:
        return '\n'.join([' '.join(map(str, i)) for i in self.__matrix])

    @property
    def get_matrix(self) -> list[list[float]]:
        return self.__matrix

    @property
    def get_rows(self) -> int:
        return self.__n

    @property
    def get_cols(self) -> int:
        return self.__m

    def submatrices(self) -> tuple:
        matrix_a: list[list[float]] = []
        matrix_b: list[float] = []

        for i in range(self.__n):
            *matrix_a_i, matrix_b_i = self.__matrix[i]

            matrix_a.append(matrix_a_i)
            matrix_b.append(matrix_b_i)

        return matrix_a, matrix_b

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

    def rearrangement(self) -> None:
        for row in range(self.__n):
            max_col = row

            for col in range(self.__m - 1):
                if abs(self.__matrix[row][col]) > abs(self.__matrix[row][max_col]):
                    max_col = col

            if self.__matrix[row][max_col] > self.__matrix[max_col][max_col]:
                self.__matrix[row], self.__matrix[max_col] = self.__matrix[max_col], self.__matrix[row]
        return
