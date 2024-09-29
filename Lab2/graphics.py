import numpy as np
import matplotlib.pyplot as plt

from deriviate import f, df


class Graphic:

    def __init__(self, a: float, b: float):
        self.x = np.linspace(a, b, 200)
        self.y = f(self.x)

    def create_func_graphic(self) -> None:
        ax = plt.gca()
        ax.plot(self.x, self.y)

        # Рисуем декартову систему
        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)
        ax.grid()

        ax.set_title('График функции y(x)')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        plt.savefig("pics/y(x).png")
        plt.show()
        return

    @staticmethod
    def intervalCheck(a: int, b: int) -> bool:
        """Проверяем есть ли на интервале [a, b] корень уравнения"""
        accuracy = 0.1

        if f(a) * f(b) < 0 or all(df(i, accuracy) > accuracy for i in range(a, b + 1)):
            return True
        return False

    def find_closest_x0(self, data: str) -> float:
        """Нахождим приближенное значение на заданном интервале с помощью метода половинного деления"""
        a, b = map(int, data.split())

        if not self.intervalCheck(a, b):
            raise Exception('На данном промежутке корней нет, либо их больше чем 1')

        accuracy = 0.5
        c = (a + b) / 2

        while (b - a) / 2 > accuracy:
            if f(a) * f(b) < 0:
                b = c
            else:
                a = c

            c = (a + b) / 2

        return c
