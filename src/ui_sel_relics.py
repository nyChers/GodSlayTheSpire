# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_sel_relics.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ui_sel_relics(object):
    def setupUi(self, ui_sel_relics):
        ui_sel_relics.setObjectName("ui_sel_relics")
        ui_sel_relics.resize(711, 1000)
        self.sel_relics_list = QtWidgets.QTableWidget(ui_sel_relics)
        self.sel_relics_list.setGeometry(QtCore.QRect(10, 60, 690, 931))
        self.sel_relics_list.setAutoFillBackground(True)
        self.sel_relics_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.sel_relics_list.setAlternatingRowColors(True)
        self.sel_relics_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.sel_relics_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.sel_relics_list.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.sel_relics_list.setRowCount(0)
        self.sel_relics_list.setColumnCount(4)
        self.sel_relics_list.setObjectName("sel_relics_list")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.sel_relics_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.sel_relics_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.sel_relics_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.sel_relics_list.setHorizontalHeaderItem(3, item)
        self.text_search = QtWidgets.QLineEdit(ui_sel_relics)
        self.text_search.setGeometry(QtCore.QRect(10, 20, 151, 30))
        self.text_search.setObjectName("text_search")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(ui_sel_relics)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(460, 10, 235, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_add = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_add.setObjectName("btn_add")
        self.gridLayout_2.addWidget(self.btn_add, 0, 0, 1, 1)
        self.btn_back = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout_2.addWidget(self.btn_back, 0, 1, 1, 1)
        self.msg = QtWidgets.QLabel(ui_sel_relics)
        self.msg.setGeometry(QtCore.QRect(180, 20, 261, 30))
        self.msg.setText("")
        self.msg.setObjectName("msg")

        self.retranslateUi(ui_sel_relics)
        QtCore.QMetaObject.connectSlotsByName(ui_sel_relics)

    def retranslateUi(self, ui_sel_relics):
        _translate = QtCore.QCoreApplication.translate
        ui_sel_relics.setWindowTitle(_translate("ui_sel_relics", "选择遗物"))
        item = self.sel_relics_list.horizontalHeaderItem(0)
        item.setText(_translate("ui_sel_relics", "Relics ID"))
        item = self.sel_relics_list.horizontalHeaderItem(1)
        item.setText(_translate("ui_sel_relics", "Name"))
        item = self.sel_relics_list.horizontalHeaderItem(2)
        item.setText(_translate("ui_sel_relics", "FLAVOR"))
        item = self.sel_relics_list.horizontalHeaderItem(3)
        item.setText(_translate("ui_sel_relics", "DESCRIPTIONS"))
        self.btn_add.setText(_translate("ui_sel_relics", "添加"))
        self.btn_back.setText(_translate("ui_sel_relics", "返回"))

