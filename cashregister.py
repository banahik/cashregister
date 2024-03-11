import sys  
from PySide6 import QtWidgets, QtCore

from QT import mainWindow


class MainWindow(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
