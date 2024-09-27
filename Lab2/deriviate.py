import numpy as np


def f(x) -> float:
    return -0.09 + 3.6 * x - 0.69 * x ** 2 - 4.16 * np.sin(x)


def df(x: float, accuracy: float) -> float:
    return (f(x + accuracy) - f(x - accuracy)) / (2 * accuracy)


def df2(x: float, accuracy: float) -> float:
    return (f(x - 2 * accuracy) + f(x + 2 * accuracy) - 2 * f(x)) / (4 * accuracy ** 2)


"""
Номер варианта: 73
Параметры функциональной зависимости: a0 = -0,09;  a1 = 3,60; a2 = -0,69;  a3 = -4,16.
Графический метод для п. 3 - метод нулей функции
Методы для пп. 4, 5 - Ньютона, простых итераций
"""
