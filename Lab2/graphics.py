from math import ceil
import numpy as np
import matplotlib.pyplot as plt

from deriviate import f


class Graphic:

    def __init__(self, a: float, b: float):
        self.x = np.linspace(a, b, 200)
        self.y = f(self.x)

    def create_func_graphic(self) -> None:
        ax = plt.gca()
        ax.plot(self.x, self.y)

        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)

        ax.set_title('График функции y(x)')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid()
        plt.savefig("pics/y(x).png")
        return

    def find_closest_x0(self, visible: int) -> list[int]:
        x = [ceil(i) for i in self.x]
        y = [f(i) for i in self.x]

        nums = sorted(zip(x, y), key=lambda coord: abs(coord[1]))
        hmap = {}
        for x, y in nums:
            hmap[x] = hmap.get(x, 0) + 1

        return list(hmap)[:visible]



# def zero_method(a, b, visible) -> list[float]:
#     ax = plt.gca()
#     x = np.linspace(a, b, 200)
#     ax.plot(x, f(x))
#
#     # Алгоритм нахождения приближенных значений
#     y = [f(i) for i in x]
#     x = [ceil(i) for i in x]
#     compare = list(zip(x, y))
#     nums = sorted(compare, key=lambda coord: abs(coord[1]))
#     hmap = {}
#     for x, y in nums:
#         hmap[x] = hmap.get(x, 0) + 1
#
#     # Рисуем оси OX и OY
#     plt.axhline(0, color="black", linewidth=0.5)
#     plt.axvline(0, color="black", linewidth=0.5)
#
#     ax.set_title('График функции y(x)')
#     ax.set_xlabel('x')
#     ax.set_ylabel('y')
#     ax.grid()
#     plt.savefig("pics/y(x).png")
#     # plt.show()
#
#     return list(hmap)[:visible]