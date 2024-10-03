from graphics import FunctionGraphic, IterationDependencyGraphic
from methods import newton_method, simple_iteration_method

"""
Номер варианта: 73
Параметры функциональной зависимости: a0 = -0,09;  a1 = 3,60; a2 = -0,69;  a3 = -4,16.
Графический метод для п. 3 - метод нулей функции
Методы для пп. 4, 5 - Ньютона, простых итераций
"""

# Интервал локализации корней
A: int = -3
B: int = 7

# Разные значения точности
E: list[float] = [0.1, 0.01, 0.001, 0.0001, 0.00001]

if __name__ == '__main__':
    # Создаем график функции
    graphic1 = FunctionGraphic(A, B)

    num_x0 = int(input('Сколько видно на графике решений уравнения?: '))

    with open('output.txt', 'a', encoding='utf-8') as out_file:
        out_file.truncate(0)

        for i in range(1, num_x0 + 1):
            # Пользователь получает приближенное значения для своего интервала
            x0: float = graphic1.find_nearest_x0(input('Введите интервал: '))
            print(f'Находим решение уравнения для приближения: {x0}', file=out_file)
            for accuracy in E:
                print(f'Точность: {accuracy}\n'
                      f'{newton_method(x0, accuracy)[0]}\n'
                      f'{simple_iteration_method(x0, accuracy)[0]}\n', file=out_file)
            print('------------------------------------------------------------------------', file=out_file)

            print('Файл "output.txt" обновлен')

            # Находим y1 и y2 для новых графиков
            newton_iter, simple_iter = graphic1.count_iterations(x0, E)

            # Создаем график зависимостей
            graphic2 = IterationDependencyGraphic()

            # Подгружаем количество итераций для рисовки графика
            graphic2.set_iterations(newton_iter, simple_iter)
            graphic2.create_graphic(i)
