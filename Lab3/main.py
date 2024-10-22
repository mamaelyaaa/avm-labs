from Lab3.matrix import Matrix
from Lab3.methods import method_kramer, method_simple_iteration

with open('x0.txt', 'r', encoding='utf-8') as x0_file:
    x0: list[float] = [float(i.strip()) for i in x0_file.readlines()]

with open('matrix.txt', 'r', encoding='utf-8') as input_file:
    matrix = Matrix([[float(i) for i in line.split()] for line in input_file.readlines()])

if __name__ == '__main__':
    print(method_kramer(matrix))
    print(method_simple_iteration(matrix, 0.0001, x0))