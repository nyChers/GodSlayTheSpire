# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_MyWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(496, 230)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Chers/Desktop/cute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 249, 199))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.writefile = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.writefile.setObjectName("writefile")
        self.gridLayout.addWidget(self.writefile, 1, 1, 1, 1)
        self.current_health = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.current_health.setObjectName("current_health")
        self.gridLayout.addWidget(self.current_health, 3, 1, 1, 1)
        self.energy = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.energy.setObjectName("energy")
        self.gridLayout.addWidget(self.energy, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.openfile = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.openfile.setObjectName("openfile")
        self.gridLayout.addWidget(self.openfile, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.max_health = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.max_health.setObjectName("max_health")
        self.gridLayout.addWidget(self.max_health, 2, 1, 1, 1)
        self.gold = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gold.setObjectName("gold")
        self.gridLayout.addWidget(self.gold, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(300, 80, 175, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.encodeJson = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.encodeJson.setObjectName("encodeJson")
        self.gridLayout_2.addWidget(self.encodeJson, 1, 0, 1, 1)
        self.decodeautosave = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.decodeautosave.setObjectName("decodeautosave")
        self.gridLayout_2.addWidget(self.decodeautosave, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "GodSlayTheSpire"))
        self.writefile.setText(_translate("Dialog", "写回存档"))
        self.label.setText(_translate("Dialog", "血量上限:"))
        self.openfile.setText(_translate("Dialog", "读取存档"))
        self.label_3.setText(_translate("Dialog", "能量上限:"))
        self.label_2.setText(_translate("Dialog", "当前血量:"))
        self.label_4.setText(_translate("Dialog", "金钱数量:"))
        self.encodeJson.setText(_translate("Dialog", "Json编码为autosave"))
        self.decodeautosave.setText(_translate("Dialog", "存档解码到Json"))

