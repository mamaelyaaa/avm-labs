from Lab2.methods import newton_method
from graphics import Graphic

"""
Номер варианта: 73
Параметры функциональной зависимости: a0 = -0,09;  a1 = 3,60; a2 = -0,69;  a3 = -4,16.
Графический метод для п. 3 - метод нулей функции
Методы для пп. 4, 5 - Ньютона, простых итераций
"""


# Интервал локализации корней
A = -3
B = 7

E = iter(10 ** (-i) for i in range(1, 6))


if __name__ == '__main__':
    close_x = Graphic(A, B).find_closest_x0(input('Введите интервал для нахождения приближенного значения: '))
    print(newton_method(close_x, 0.01))
