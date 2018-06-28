# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_MyWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(245, 181)
        self.decodeautosave = QtWidgets.QPushButton(Dialog)
        self.decodeautosave.setGeometry(QtCore.QRect(10, 30, 221, 41))
        self.decodeautosave.setObjectName("decodeautosave")
        self.encodeJson = QtWidgets.QPushButton(Dialog)
        self.encodeJson.setGeometry(QtCore.QRect(10, 110, 221, 41))
        self.encodeJson.setObjectName("encodeJson")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "God"))
        self.decodeautosave.setText(_translate("Dialog", "存档解码"))
        self.encodeJson.setText(_translate("Dialog", "Json编码"))

