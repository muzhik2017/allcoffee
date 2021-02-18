# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(971, 629)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.coffee_table = QtWidgets.QTableWidget(self.centralwidget)
        self.coffee_table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.coffee_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.coffee_table.setObjectName("coffee_table")
        self.coffee_table.setColumnCount(7)
        self.coffee_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.coffee_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.coffee_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.coffee_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.coffee_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.coffee_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.coffee_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.coffee_table.setHorizontalHeaderItem(6, item)
        self.coffee_table.horizontalHeader().setCascadingSectionResizes(False)
        self.coffee_table.horizontalHeader().setSortIndicatorShown(False)
        self.coffee_table.horizontalHeader().setStretchLastSection(False)
        self.coffee_table.verticalHeader().setVisible(False)
        self.coffee_table.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.coffee_table)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.add_edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_edit_btn.setObjectName("add_edit_btn")
        self.horizontalLayout.addWidget(self.add_edit_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 971, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.clear_db_action = QtWidgets.QAction(MainWindow)
        self.clear_db_action.setObjectName("clear_db_action")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Кофе"))
        item = self.coffee_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.coffee_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название сорта"))
        item = self.coffee_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Степень обжарки"))
        item = self.coffee_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Молотый/в зёрнах"))
        item = self.coffee_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Описание вкуса"))
        item = self.coffee_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Цена"))
        item = self.coffee_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Объём упаковки"))
        self.add_edit_btn.setText(_translate("MainWindow", "Добавить/Редактировать"))
        self.clear_db_action.setText(_translate("MainWindow", "Очистить"))
