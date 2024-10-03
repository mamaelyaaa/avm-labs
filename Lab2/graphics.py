import numpy as np
import matplotlib.pyplot as plt

from typing import Optional

from deriviate import f, df
from methods import newton_method, simple_iteration_method


class FunctionGraphic:

    def __init__(self, a: int, b: int):
        self.__ax = plt.gca()
        self.__x = np.linspace(a, b)
        self.__y = f(self.__x)
        self.create_graphic()

    def create_graphic(self) -> None:
        self.__ax.plot(self.__x, self.__y)

        self.__ax.set_title('График функции y(x)')
        self.__ax.set_xlabel('x')
        self.__ax.set_ylabel('y')

        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)
        self.__ax.grid()

        plt.savefig("pics/y(x).png")
        plt.show()
        return

    @staticmethod
    def interval_check(a: int, b: int) -> bool:
        """Проверяем есть ли на интервале [a, b] корень уравнения"""
        accuracy = 0.1
        if f(a) * f(b) > 0 and all(df(i, accuracy) > accuracy for i in range(a, b + 1)) or f(a) * f(b) < 0:
            return True
        return False

    def find_nearest_x0(self, data: str) -> float:
        """Нахождим приближенное значение на заданном интервале с помощью метода половинного деления"""
        a, b = map(int, data.split())

        if not self.interval_check(a, b):
            raise Exception(
                'На данном промежутке корней нет, либо их больше чем 1\n'
                'Выберите другой промежуток или сократите имеющийся')

        accuracy = 0.5
        c = (a + b) / 2

        while (b - a) / 2 > accuracy:
            if f(a) * f(b) < 0:
                b = c
            else:
                a = c

            c = (a + b) / 2
        return c

    @staticmethod
    def count_iterations(x0: float, accuracies: list[float]) -> tuple:
        iteration_newton = {i: 0 for i in accuracies}
        iteration_simple = {i: 0 for i in accuracies}

        for epsilon in accuracies:
            answer1, iteration1 = newton_method(x0, epsilon)
            answer2, iteration2 = simple_iteration_method(x0, epsilon)

            iteration_newton[epsilon] = iteration1
            iteration_simple[epsilon] = iteration2

        newton_iter = list(iteration_newton.values())
        simple_iter = list(iteration_simple.values())

        return newton_iter, simple_iter


class IterationDependencyGraphic:

    def __init__(self):
        self.__ax = plt.gca()
        self.__x: list[int] = [i for i in range(-1, -6, -1)]
        self.__y1: Optional[list[int]] = None
        self.__y2: Optional[list[int]] = None

    def set_iterations(self, newton_iter: list[int], simple_iter: list[int]) -> None:
        self.__y1 = newton_iter
        self.__y2 = simple_iter
        return

    def create_graphic(self, i) -> None:
        self.__ax.plot(self.__x, self.__y1, label="Метод касательных")
        self.__ax.plot(self.__x, self.__y2, label='МПИ', linestyle='--')
        self.__ax.set_title(f'График зависимости количества итераций от точности для x{i}')
        self.__ax.set_xlabel('Log(e)')
        self.__ax.set_ylabel('Количество итераций')

        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)
        self.__ax.grid()

        plt.legend(loc='upper right')
        plt.savefig(f'pics/iteration_x{i}.png')
        plt.show()
        return
