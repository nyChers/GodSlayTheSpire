#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:  NingYu Zhang
# @Date:    Created on 2018/6/27 17:42

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

import MyWindow
import sys





def main():
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow.MyWindow()
    mywindow.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint | Qt.WindowCloseButtonHint)
    mywindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
