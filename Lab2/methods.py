from deriviate import f, df
from math import log10

"""
Посчитать количество итераций для достижения необходимых точностей, чтобы с их помощью составить график
"""
def newton_method(x0, accuracy: float) -> float:
    x1 = x0 - f(x0) / df(x0, accuracy)

    while abs(x1 - x0) > accuracy:
        x0 = x1
        x1 = x0 - f(x0) / df(x0, accuracy)

    return round(x1, abs(int(log10(accuracy))) + 1)


def simple_iteration_method(x0, v: float, accuracy: float) -> float:
    if v > 0.7 or v < 0.3:
        raise Exception('Неправильно указан коэффициент сходимости - [0.3; 0.7]')

    l = - (df(x0, accuracy) * v) / (1 + abs(df(x0, accuracy)))

    x1 = x0 + l * f(x0)

    while abs(x1 - x0) > accuracy:
        x0 = x1
        x1 = x0 + l * f(x0)

    return round(x1, abs(int(log10(accuracy))) + 1)

print(newton_method(6, 0.01))
print(simple_iteration_method(6, 0.3, 0.01))
