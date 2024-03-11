import sys  
from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QPixmap

from QT import mainWindow

from src.Product import Product 


import random


class MainWindow(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):

    product_mass = 0

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


        self.table_products.insertColumn(0)
        self.table_products.insertColumn(0)
        self.table_products.setHorizontalHeaderLabels(['Товар'])
        self.table_products.horizontalHeader().hide()




        Product.load_data()
        self.add_products_in_table()


    def add_products_in_table(self):
        """
        Добавить продукт в таблицу
        """

        for one_product in Product.product_list:
            self.table_products.insertRow(0)
            self.table_products.setRowHeight(0,100)
            # self.table_products.insertColumn(0)

            pix = QPixmap()
            pix.loadFromData(one_product.image_data) 
            
            bt = QtWidgets.QPushButton(icon=pix,text='')
            bt.setIconSize(QtCore.QSize(100,100))
            bt.setObjectName(one_product.name)
            bt.clicked.connect(self.clicked_product)


            self.table_products.setCellWidget(0,0,bt)
            self.table_products.setItem(0, 1, QtWidgets.QTableWidgetItem(str(one_product.name_ru)))


    def clicked_product(self):
        data = Product.get_product_by_name(self.sender().objectName())
        print(data.name)
        pix = QPixmap()
        pix.loadFromData(data.image_data) 
        self.bt_best_product.setIcon(pix)
        self.bt_best_product.setIconSize(QtCore.QSize(200,200))

        self.product_mass = random.random().__round__(3)

        label = f"""Товар: {data.name_ru}\nМасса: {self.product_mass}\nЦена: {data.price}\nСумма: {round(self.product_mass*data.price,3)}"""

        self.label_best_product.setText(label)
    

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
