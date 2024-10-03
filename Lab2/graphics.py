import numpy as np
import matplotlib.pyplot as plt

from Lab2.deriviate import f, df
from Lab2.methods import newton_method, simple_iteration_method


class FunctionGraphic:

    def __init__(self, a: int, b: int):
        self._x = np.linspace(a, b, 200)
        self._ax = plt.gca()
        self._y = f(self._x)

        self._ax.plot(self._x, self._y)
        self.create_grid()
        self.create_graphic()

    # Методы для создания графика
    def create_grid(self) -> None:
        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)
        self._ax.grid()
        return

    def create_graphic(self) -> str:
        self._ax.set_title('График функции y(x)')
        self._ax.set_xlabel('x')
        self._ax.set_ylabel('y')
        plt.savefig("pics/y(x).png")
        plt.show()
        return 'Создаем график функции'

    # Методы нахождения приближенного значения
    @staticmethod
    def interval_check(a: int, b: int) -> bool:
        """Проверяем есть ли на интервале [a, b] корень уравнения"""
        accuracy = 0.1
        if f(a) * f(b) < 0:
            return True

        if f(a) * f(b) > 0 and all(df(i, accuracy) > accuracy for i in range(a, b + 1)):
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
        self._x = [range(5)]
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2)

    def create_graphic(self, y1, y2) -> None:
        self.ax1.plot(self._x, y1)
        self.ax2.plot(self._x, y2)

        plt.show()
        return
