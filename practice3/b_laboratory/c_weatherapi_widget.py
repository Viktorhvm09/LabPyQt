"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""

from ui.c_weatherapi_widget_form import Ui_Form
from PySide6 import QtWidgets
from a_threads import WeatherHandler

class Window(QtWidgets.QWidget):
    isRun = None
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__initSignals()


    def __initSignals(self):
        self.ui.WeatherPushButton.clicked.connect(self.__initThreads)

    def __initThreads(self):
        if self.isRun:
            self.thread.stop()
            self.ui.LatitudeLineEdit.setEnabled(True)
            self.ui.LongitudeLineEdit.setEnabled(True)
            self.ui.TimeDelayLineEdit.setEnabled(True)
            self.ui.WeatherPushButton.setText("Выполнить")
            self.isRun = False
        else:
            self.thread = WeatherHandler(float(self.ui.LatitudeLineEdit.text()), float(self.ui.LongitudeLineEdit.text()))
            self.thread.setDelay(float(self.ui.TimeDelayLineEdit.text()))
            self.thread.start()
            self.ui.LatitudeLineEdit.setEnabled(False)
            self.ui.LongitudeLineEdit.setEnabled(False)
            self.ui.TimeDelayLineEdit.setEnabled(False)
            self.thread.WeatherInfo.connect(lambda text: self.ui.WeatherPlainTextEdit.appendPlainText(str(text)))
            self.thread.started.connect(lambda: self.ui.WeatherPushButton.setText("Стоп"))
            self.isRun = True

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()