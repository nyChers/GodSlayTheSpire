#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:  NingYu Zhang
# @Date:    Created on 2018/6/27 17:42

from PyQt5 import QtWidgets
import MyWindow
import sys





def main():
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow.MyWindow()
    mywindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
