import sys  
from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QPixmap

from QT import mainWindow

from src.Product import Product 


import random


class MainWindow(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):

    product_mass = 0
    product_name = ''
    product_sum = 0

    All_sum = 0

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


        self.table_products.insertColumn(0)
        self.table_products.insertColumn(0)
        self.table_products.setHorizontalHeaderLabels(['Товар'])
        self.table_products.horizontalHeader().hide()

        self.bt_add_product.clicked.connect(self.add_product_to_buy_lust)
        self.bt_buy.clicked.connect(self.buy)




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
        """
        Отобразить продукт на превью
        """
        data = Product.get_product_by_name(self.sender().objectName())
        pix = QPixmap()
        pix.loadFromData(data.image_data) 
        self.bt_best_product.setIcon(pix)
        self.bt_best_product.setIconSize(QtCore.QSize(200,200))

        self.product_mass = random.random().__round__(3)
        self.product_name = data.name_ru
        self.product_sum = round(self.product_mass*data.price,3)

        label = f"""Товар: {data.name_ru}\nМасса: {self.product_mass}\nЦена: {data.price}\nСумма: { self.product_sum}"""

        self.label_best_product.setText(label)
    



    numbers_iterator = iter(range(1,999))
    

    def add_product_to_buy_lust(self):
        """
        Добавление продукта с список покупок
        """
        label = str.ljust(str(next(self.numbers_iterator)),3,'.')
        label += str.ljust(str(self.product_name),25,'_')
        label += str(self.product_sum)
        self.list_products_buy.addItem(label)

        self.All_sum += self.product_sum


    def buy(self):
        """
        Кнопка купить
        """
        print(f'Куплено продуктов на {self.All_sum}')
        self.All_sum = 0
        self.list_products_buy.clear()
        self.numbers_iterator = iter(range(1,999))

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
