# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addEditForm(object):
    def setupUi(self, addEditForm):
        addEditForm.setObjectName("addEditForm")
        addEditForm.resize(400, 287)
        self.verticalLayout = QtWidgets.QVBoxLayout(addEditForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(addEditForm)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(addEditForm)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(addEditForm)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.sort_edit = QtWidgets.QLineEdit(addEditForm)
        self.sort_edit.setObjectName("sort_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sort_edit)
        self.degree_edit = QtWidgets.QLineEdit(addEditForm)
        self.degree_edit.setObjectName("degree_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.degree_edit)
        self.label_3 = QtWidgets.QLabel(addEditForm)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(addEditForm)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(addEditForm)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.flavor_edit = QtWidgets.QLineEdit(addEditForm)
        self.flavor_edit.setObjectName("flavor_edit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.flavor_edit)
        self.label_6 = QtWidgets.QLabel(addEditForm)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.price_box = QtWidgets.QDoubleSpinBox(addEditForm)
        self.price_box.setMinimum(0.0)
        self.price_box.setMaximum(1e+308)
        self.price_box.setObjectName("price_box")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.price_box)
        self.label_7 = QtWidgets.QLabel(addEditForm)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.volume_box = QtWidgets.QDoubleSpinBox(addEditForm)
        self.volume_box.setMinimum(0.0)
        self.volume_box.setMaximum(1e+138)
        self.volume_box.setSingleStep(0.5)
        self.volume_box.setObjectName("volume_box")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.volume_box)
        self.ground_or_grains_box = QtWidgets.QSpinBox(addEditForm)
        self.ground_or_grains_box.setMaximum(1)
        self.ground_or_grains_box.setObjectName("ground_or_grains_box")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ground_or_grains_box)
        self.id_box = QtWidgets.QSpinBox(addEditForm)
        self.id_box.setMaximum(99999999)
        self.id_box.setObjectName("id_box")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.id_box)
        self.verticalLayout.addLayout(self.formLayout)
        self.submit_btn = QtWidgets.QPushButton(addEditForm)
        self.submit_btn.setObjectName("submit_btn")
        self.verticalLayout.addWidget(self.submit_btn)

        self.retranslateUi(addEditForm)
        QtCore.QMetaObject.connectSlotsByName(addEditForm)

    def retranslateUi(self, addEditForm):
        _translate = QtCore.QCoreApplication.translate
        addEditForm.setWindowTitle(_translate("addEditForm", "Кофе - Добавить/Редактировать элемент"))
        self.label.setText(_translate("addEditForm", "ID(0 при добавлении)"))
        self.label_2.setText(_translate("addEditForm", "Название сорта"))
        self.label_3.setText(_translate("addEditForm", "Степень обжарки"))
        self.label_4.setText(_translate("addEditForm", "Молотый - 0/в зёрнах - 1"))
        self.label_5.setText(_translate("addEditForm", "Описание вкуса"))
        self.label_6.setText(_translate("addEditForm", "Цена"))
        self.label_7.setText(_translate("addEditForm", "Объём упаковки"))
        self.submit_btn.setText(_translate("addEditForm", "Подтвердить"))
