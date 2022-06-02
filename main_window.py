from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel


class MainWindow(QMainWindow):
    """Класс главного окна в приложении,
    отрисовывает картику info.png"""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = "Место на диске"
        self.setWindowTitle(self.title)
        label = QLabel(self)
        image_name = 'info.png'
        pixmap = QPixmap(image_name)
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())
