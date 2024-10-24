from matplotlib import pyplot as plt


class BaseGraphic:
    def __init__(self):
        self._fig, self._ax = plt.subplots(figsize=(7, 5))

    def set_title(self, title: str) -> None:
        self._ax.set_title(title)

    def set_labels(self, xlabel: str, ylabel: str) -> None:
        self._ax.set_xlabel(xlabel)
        self._ax.set_ylabel(ylabel)

    def add_grid_and_axes(self) -> None:
        """Добавляем сетку и оси"""
        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)
        self._ax.grid()

    @staticmethod
    def show_and_save(filename: str = None) -> None:
        """Отображает и сохраняет график, если указан файл"""
        if filename:
            plt.savefig(filename)
        plt.show()


class DependencyDiagram(BaseGraphic):

    def __init__(self, accuracies, iterations):
        super().__init__()
        self.accuracies: list[str] = accuracies
        self.iterations = iterations
        self.create_graphic()

    def create_graphic(self) -> None:
        self._ax.bar(self.accuracies, self.iterations)
        self.set_title('Количество итераций необходимых для достижения точности')
        self.set_labels(xlabel='Точность', ylabel='Количество итераций')
        self.add_grid_and_axes()
        self.show_and_save('pics/diagram.png')


class ChangingGraphic(BaseGraphic):

    def __init__(self, a: int, b: int):
        self._fig, self._ax = plt.subplots(figsize=(10, 5))
        self.__x: list[int] = [k for k in range(a, b + 1)]
        self.a = a
        self.b = b
        self.y_values = [[] for _ in range(7)]

    def set_func(self, intermediate_data: list[list], i: int):
        self.y_values[i] = [row[i] for row in intermediate_data[:self.b + 1]]

    def create_graphic(self) -> None:
        colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']  # Задаем разные цвета для графиков
        labels = [f'x{i + 1}' for i in range(7)]

        for i in range(7):
            if self.y_values[i]:
                self._ax.plot(self.__x, self.y_values[i], label=labels[i], color=colors[i], marker='o', markersize=3)

        self.set_title('График изменения всех элементов вектора решения системы от номера итерации при точности = 0.1')
        self.set_labels('k', 'x')
        self.add_grid_and_axes()
        self._ax.legend(loc='lower left')
        self.show_and_save("pics/y(x).png")
