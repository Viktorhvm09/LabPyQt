from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Основное окно')
        self.resize(300, 200)

        button = QPushButton('Кнопка', self)
        button.setGeometry(10, 10, 100, 30)
        button.setStyleSheet('background-color: red; color: white;')


app = QtWidgets.QApplication()

window = MainWindow()
window.show()
window.resize(300, 200)

app.exec()