# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 634)
        font = QFont()
        font.setFamilies([u"Arial"])
        MainWindow.setFont(font)
        self.actionsitem_panel = QAction(MainWindow)
        self.actionsitem_panel.setObjectName(u"actionsitem_panel")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setPointSize(15)
        self.centralwidget.setFont(font1)
        self._2 = QHBoxLayout(self.centralwidget)
        self._2.setObjectName(u"_2")
        self._2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bt_best_product = QPushButton(self.centralwidget)
        self.bt_best_product.setObjectName(u"bt_best_product")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_best_product.sizePolicy().hasHeightForWidth())
        self.bt_best_product.setSizePolicy(sizePolicy)
        self.bt_best_product.setMinimumSize(QSize(200, 200))
        self.bt_best_product.setMaximumSize(QSize(200, 200))

        self.horizontalLayout.addWidget(self.bt_best_product)

        self.label_best_product = QLabel(self.centralwidget)
        self.label_best_product.setObjectName(u"label_best_product")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(15)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.label_best_product.setFont(font2)
        self.label_best_product.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.label_best_product)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(15)
        font3.setBold(False)
        self.label.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label)

        self.finde_products = QLineEdit(self.centralwidget)
        self.finde_products.setObjectName(u"finde_products")
        self.finde_products.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_3.addWidget(self.finde_products)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.table_products = QTableWidget(self.centralwidget)
        self.table_products.setObjectName(u"table_products")
        self.table_products.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_2.addWidget(self.table_products)


        self._2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.list_products_buy = QListWidget(self.centralwidget)
        self.list_products_buy.setObjectName(u"list_products_buy")
        self.list_products_buy.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout.addWidget(self.list_products_buy)

        self.bt_buy = QPushButton(self.centralwidget)
        self.bt_buy.setObjectName(u"bt_buy")
        self.bt_buy.setMinimumSize(QSize(0, 50))
        self.bt_buy.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout.addWidget(self.bt_buy)


        self._2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 794, 36))
        self.menusattings = QMenu(self.menubar)
        self.menusattings.setObjectName(u"menusattings")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menusattings.menuAction())
        self.menusattings.addAction(self.actionsitem_panel)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionsitem_panel.setText(QCoreApplication.translate("MainWindow", u"system panel", None))
        self.bt_best_product.setText("")
        self.label_best_product.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.bt_buy.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c", None))
        self.menusattings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

