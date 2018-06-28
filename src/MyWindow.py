#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:  NingYu Zhang
# @Date:    Created on 2018/6/27 18:01
import json
from PyQt5.QtWidgets import QFileDialog
from ui_MyWindow import Ui_Dialog
from PyQt5 import QtWidgets
import decode_encode

realdata = {}


class MyWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.decodeautosave.clicked.connect(self.decodeautosave)
        self.ui.encodeJson.clicked.connect(self.encodeJson)
        self.ui.openfile.clicked.connect(self.openfile)
        self.ui.writefile.clicked.connect(self.writefile)

    # 读取存档写到json文件
    def decodeautosave(self):
        fileName1 = QFileDialog.getOpenFileName(self, "选取存档", "./", "存档 (*.autosave)")  # 设置文件扩展名过滤,注意用双分号间隔

        with open(fileName1[0], "rb") as f:
            old_autosave = f.read()
        # print(old_autosave)

        old_json = decode_encode.decode(old_autosave, "key")
        old_json = str(old_json, 'utf-8')
        # print(old_json)

        data = json.loads(old_json)
        # print(data)

        fileName2 = QFileDialog.getOpenFileName(self, "选取存档", "./", "存档 (*.json)")

        with open(fileName2[0], 'w') as f:
            json.dump(data, f, indent=2)

    # 将json文件转回autosave
    def encodeJson(self):
        fileName2 = QFileDialog.getOpenFileName(self, "选取Json", "./", "数据 (*.json)")

        with open(fileName2[0], 'r') as f:
            data = f.read()

        resave = decode_encode.encode(data, "key")
        resave = str(resave, encoding='utf-8')

        fileName3 = QFileDialog.getSaveFileName(self, "保存存档", "./", "存档 (*.autosave)")
        with open(fileName3[0], 'w') as f:
            f.write(resave)

    # 打开存档解码并读入数据到realdata
    def openfile(self):
        fileName = QFileDialog.getOpenFileName(self, "选取存档", "./", "存档 (*.autosave)")
        with open(fileName[0], "rb") as f:
            old_autosave = f.read()

        b_realdata = decode_encode.decode(old_autosave, "key")
        s_realdata = str(b_realdata, 'utf-8')
        global realdata
        realdata = json.loads(s_realdata)
        self.ui.max_health.setText(str(realdata['max_health']))
        self.ui.current_health.setText(str(realdata['current_health']))
        self.ui.gold.setText(str(realdata['gold']))
        self.ui.energy.setText(str(realdata['red']))

    # 写回存档
    def writefile(self):
        self.modify_4Attributes()
        global realdata
        s_realdata = json.dumps(realdata, indent=2)
        new_autosave = decode_encode.encode(s_realdata, "key")
        resave = str(new_autosave, encoding='utf-8')
        fileName = QFileDialog.getSaveFileName(self, "保存存档", "./", "存档 (*.autosave)")
        with open(fileName[0], 'w') as f:
            f.write(resave)

    # 修改基础四属性
    def modify_4Attributes(self):
        global realdata
        print(realdata['max_health'])
        realdata['max_health'] = int(self.ui.max_health.text())
        realdata['current_health'] = int(self.ui.current_health.text())
        realdata['gold'] = int(self.ui.gold.text())
        realdata['red'] = int(self.ui.energy.text())
