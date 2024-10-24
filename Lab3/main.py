import numpy as np

from Lab3.graphic import DependencyDiagram, ChangingGraphic
from Lab3.methods import method_kramer, method_simple_iteration

E: list[float] = [0.1, 0.02, 0.005, 0.001]


if __name__ == '__main__':
    with open('x0.txt', 'r', encoding='utf-8') as x0_file:
        x0 = np.array([float(i.strip()) for i in x0_file.readlines()])

    with open('matrix.txt', 'r', encoding='utf-8') as input_file:
        matrix = np.array([[float(i) for i in line.split()] for line in input_file.readlines()])

    iterations: list[int] = []

    with open('output.txt', 'a', encoding='utf-8') as out_file:
        out_file.truncate(0)

        print(f'Метод Крамера: \n{method_kramer(matrix)}\n'
              f'------------------------------------------\n'
              f'Метод простых итераций:', file=out_file)
        for accuracy in E:
            print(f'Точность: {accuracy}', file=out_file)

            answer, iteration, _ = method_simple_iteration(matrix, x0, accuracy)
            print(f'{answer}', file=out_file)
            iterations.append(iteration)

    print('Файл "output.txt" обновлен')

    # Создаем диаграмму зависимостей
    graphic1 = DependencyDiagram([str(i) for i in E], iterations)

    # Находим промежуточные значения
    _, _, intermediate_vec = method_simple_iteration(matrix, x0, 0.1)
    graphic2 = ChangingGraphic(len(intermediate_vec))
    for i in range(7):
        graphic2.set_func(intermediate_vec, i)

    graphic2.create_graphic()
