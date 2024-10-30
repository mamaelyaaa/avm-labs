from typing import Optional

import matplotlib.pyplot as plt
import numpy as np

# from Lab2.deriviate import f
# from Lab2.methods import newton_method, simple_iteration_method


class BaseGraphic:
    def __init__(self):
        self._ax = plt.gca()

    def set_title(self, title: str) -> None:
        self._ax.set_title(title)

    def set_labels(self, xlabel: str, ylabel: str) -> None:
        self._ax.set_xlabel(xlabel)
        self._ax.set_ylabel(ylabel)

    def add_grid_and_axes(self) -> None:
        """Добавляем сетку и оси"""
        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)
        self._ax.grid()

    @staticmethod
    def show_and_save(filename: str = None) -> None:
        """Отображает и сохраняет график, если указан файл"""
        if filename:
            plt.savefig(filename)
        plt.show()


class FunctionGraphic(BaseGraphic):

    def __init__(self, a: int, b: int):
        super().__init__()
        self.__x = np.linspace(a, b)
        self.__y = f(self.__x)
        self.create_graphic()

    def create_graphic(self) -> None:
        self._ax.plot(self.__x, self.__y)
        self.set_title('График функции y(x)')
        self.set_labels('x', 'y')
        self.add_grid_and_axes()
        self.show_and_save("pics/y(x).png")

    @staticmethod
    def interval_check(a: int, b: int) -> bool:
        """Проверка на наличие корня на интервале"""
        if f(a) * f(b) < 0:
            return True
        return False

    def find_nearest_x0(self, data: str) -> float:
        """Метод половинного деления для нахождения корня"""
        a, b = map(int, data.split())
        if not self.interval_check(a, b):
            raise Exception('На данном промежутке корней нет, либо их больше чем 1.')

        accuracy = 0.5
        c = (a + b) / 2

        while (b - a) / 2 > accuracy:
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
            c = (a + b) / 2
        return c

    @staticmethod
    def count_iterations(x0: float, accuracies: list[float]) -> tuple:
        """Подсчет итераций для различных методов."""
        iteration_newton = {i: 0 for i in accuracies}
        iteration_simple = {i: 0 for i in accuracies}

        for epsilon in accuracies:
            _, iteration1 = newton_method(x0, epsilon)
            _, iteration2 = simple_iteration_method(x0, epsilon)

            iteration_newton[epsilon] = iteration1
            iteration_simple[epsilon] = iteration2

        newton_iter = list(iteration_newton.values())
        simple_iter = list(iteration_simple.values())

        return newton_iter, simple_iter


class IterationDependencyGraphic(BaseGraphic):
    def __init__(self):
        super().__init__()
        self.__x: list[int] = [i for i in range(-1, -6, -1)]
        self.__y1: Optional[list[int]] = None
        self.__y2: Optional[list[int]] = None

    def set_iterations(self, newton_iter: list[int], simple_iter: list[int]) -> None:
        self.__y1 = newton_iter
        self.__y2 = simple_iter

    def create_graphic(self, i: int) -> None:
        if self.__y1 is None or self.__y2 is None:
            raise ValueError("Данные итераций не заданы")

        self._ax.plot(self.__x, self.__y1, label="Метод касательных")
        self._ax.plot(self.__x, self.__y2, label='МПИ', linestyle='--')

        self.set_title(f'График зависимости количества итераций от точности для x{i}')
        self.set_labels('Log(e)', 'Количество итераций')

        self.add_grid_and_axes()
        plt.legend(loc='upper right')
        self.show_and_save(f'pics/iteration_x{i}.png')
