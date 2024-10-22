# Исходная матрица
import numpy as np

matrix = np.array([
    [6.7, -0.1, 13.4, -4.5, 20.3, 20.1, -6.0],
    [12.2, -3.0, -0.8, -1.3, -8.6, -0.3, 1.6],
    [3.9, 4.2, 7.0, -3.2, -1.6, -0.7, 4.2],
    [-3.1, -7.3, 5.6, 6.1, 11.0, 2.3, -1.6],
    [6.3, 0.9, 7.0, 2.6, 4.4, 3.7, 10.0],
    [-3.9, 14.4, 10.5, 6.8, -4.7, -4.8, 2.3],
    [6.0, -3.3, 7.9, 10.6, -2.7, -7.6, -4.7]
])


class DiagonalDominance:
    def __init__(self, matrix):
        self.__matrix = np.array(matrix)
        self.__n, self.__m = self.__matrix.shape

    def make_diagonally_dominant(self):
        stable = False

        while not stable:
            stable = True

            # Перестановка строк
            for row in range(self.__n):
                # Ищем индекс максимального элемента по модулю в строке (исключая последний столбец)
                max_index = np.argmax(np.abs(self.__matrix[row][:-1]))

                # Проверяем, что максимальный элемент не на диагонали и больше диагонального элемента
                if max_index != row and abs(self.__matrix[row][max_index]) > abs(self.__matrix[max_index][max_index]):
                    # Переставляем строки
                    self.__matrix[[row, max_index]] = self.__matrix[[max_index, row]]
                    stable = False  # Матрица изменилась, проверку продолжаем
                    break

            # Перестановка столбцов
            for col in range(self.__m - 1):
                # Ищем индекс максимального элемента по модулю в столбце (исключая последний элемент)
                max_index = np.argmax(np.abs(self.__matrix[:, col]))

                # Проверяем, что максимальный элемент не на диагонали
                if max_index != col and abs(self.__matrix[max_index][col]) > abs(self.__matrix[col][col]):
                    # Меняем местами столбцы
                    self.__matrix[:, [col, max_index]] = self.__matrix[:, [max_index, col]]
                    stable = False  # Матрица изменилась, проверку продолжаем
                    break

        return self.__matrix

print(DiagonalDominance(matrix).make_diagonally_dominant())