import numpy as np


def f(x) -> float:
    return -0.09 + 3.6 * x - 0.69 * x ** 2 - 4.16 * np.sin(x)


def df(x: float, accuracy: float) -> float:
    return (f(x + accuracy) - f(x - accuracy)) / (2 * accuracy)
