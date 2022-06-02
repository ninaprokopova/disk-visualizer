import shutil
import sys

from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
from img_connecter import ImgConnecter
from img_info_getter import ImgInfoGetter


def get_image_and_safe(disk_name: str, file_name: str) -> None:
    """Создаёт картинку с информацией о диске и сохраняет"""
    img_info_getter = ImgInfoGetter()
    usage = shutil.disk_usage(f'{disk_name}:')

    data = [usage.free, usage.used]
    labels = ["Свободно", "Занято"]
    explode = [0, 0.1]
    title = f'Место на диске {disk_name}'
    name = f'{file_name}'

    img_info_getter.get_and_save_pie_diagram(data=data,
                                             labels=labels,
                                             explode=explode,
                                             title=title,
                                             name=name)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    get_image_and_safe('D', '1')
    get_image_and_safe('C', '2')

    img_connector = ImgConnecter()
    img_connector.connect_imgs('1.png', '2.png')

    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
