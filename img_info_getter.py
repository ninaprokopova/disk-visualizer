import math

import matplotlib.pyplot as plt


class ImgInfoGetter:
    """Класс, который создаёт пирожковую диаграмму
    и сохряняет"""

    def get_and_save_pie_diagram(self, data: list[float],
                                 title: str,
                                 labels: list[str],
                                 explode: list[float],
                                 name: str) -> None:
        """Создаёт и сохраняет пирожковую диаграмму"""
        plt.figure()
        plt.pie(data, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        label_1 = self.get_label(label=labels[0], size=data[0])
        label_2 = self.get_label(label=labels[1], size=data[1])
        plt.legend(labels=[label_1, label_2], loc=3, fontsize=10)
        plt.axis('equal')
        plt.title(title, fontsize=15)
        plt.savefig(f'{name}.png')

    def get_label(self, label: str, size: float):
        """Возвращает подпись для легенды"""
        return label + ' ' + str(self.convert_bytes_to_gbytes(size)) + ' Гб'

    def convert_bytes_to_gbytes(self, bytes: float) -> float:
        """Конвертирует байты в Гбайты"""
        return float('{:.1f}'.format(bytes / 1073741824))
