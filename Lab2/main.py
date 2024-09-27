from graphics import Graphic

# Интервал локализации корня
A = -3
B = 7

E = iter(10 ** (-i) for i in range(1, 6))

"""
Посчитать количество итераций для достижения необходимых точностей, чтобы с их помощью составить график
"""

if __name__ == '__main__':
    close_x = Graphic(A, B).find_closest_x0(int(input('Сколько видно приближенных значений на графике?: ')))
    print(close_x)
    # for x0 in close_x:


