from deriviate import f, df
from math import log10

"""
Посчитать количество итераций для достижения необходимых точностей, чтобы с их помощью составить график
"""


def newton_method(x0: float | int, accuracy: float) -> float:
    x1 = x0 - f(x0) / df(x0, accuracy)
    while abs(x1 - x0) > accuracy and abs(f(x0)) > accuracy:
        x0 = x1
        x1 = x0 - f(x0) / df(x0, accuracy)

    x_calc = round(x1, abs(int(log10(accuracy))) + 1)

    return x_calc


def simple_iteration_method(x0: float | int, v: float, gamma: float, accuracy: float) -> float:
    if v > 0.7 or v < 0.3:
        raise Exception('Неправильно указан коэффициент сходимости - [0.3; 0.7]')
    if gamma < 0:
        raise Exception('Неправильно указан параметр гаммы - (обычно = 1, но может быть любым больше или равен 0)')

    lam = - (df(x0, accuracy) * v) / (gamma + abs(df(x0, accuracy)))
    x1 = x0 + lam * f(x0)

    while abs(x1 - x0) > accuracy:
        x0 = x1
        x1 = x0 + lam * f(x0)

    x_calc = round(x1, abs(int(log10(accuracy))) + 1)

    return x_calc


# print(newton_method(1.4375, 0.00001))
# print(simple_iteration_method(6, 0.3, 0.01))
