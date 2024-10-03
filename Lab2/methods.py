from Lab2.deriviate import f, df
from math import log10


def newton_method(x0: float, accuracy: float) -> tuple[str, int]:
    x1 = x0 - f(x0) / df(x0, accuracy)
    iteration = 1

    while abs(x1 - x0) > accuracy and abs(f(x0)) > accuracy:
        x0 = x1
        iteration += 1
        x1 = x0 - f(x0) / df(x0, accuracy)

    x_calc = round(x1, abs(int(log10(accuracy))))

    return f'Метод Ньютона:          {x_calc} +- {accuracy}', iteration


def simple_iteration_method(x0: float, accuracy: float, v: float = 0.7, gamma: float = 1) -> tuple[str, int]:
    if v > 0.7 or v < 0.3:
        raise Exception('Неправильно указан коэффициент сходимости - [0.3; 0.7]')
    if gamma < 0:
        raise Exception('Неправильно указан параметр гаммы - (обычно = 1, но может быть любым больше или равен 0)')

    sign: int = -1 if df(x0, accuracy) < 0 else 1
    lam = - (sign * v) / (gamma + abs(df(x0, accuracy)))

    x1 = x0 + lam * f(x0)
    iteration = 1

    while abs(x1 - x0) > accuracy:
        x0 = x1
        iteration += 1
        x1 = x0 + lam * f(x0)

    x_calc = round(x1, abs(int(log10(accuracy))))

    return f"Метод простых итераций: {x_calc} +- {accuracy}", iteration
