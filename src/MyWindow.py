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

    def decodeautosave(self):
        fileName1 = QFileDialog.getOpenFileName(self, "选取存档", "./", "存档 (*.autosave)")  # 设置文件扩展名过滤,注意用双分号间隔

        with open(fileName1[0], "rb") as f:
            old_autosave = f.read()
        # print(old_autosave)

        old_json = decode_encode.decode(old_autosave, "key")
        old_json = str(old_json, 'utf-8')
        # print(old_json)

        global realdata
        realdata = json.loads(old_json)
        # print(realdata)

        with open('data.json', 'w') as f:
            json.dump(realdata, f, indent=2)

    def encodeJson(self):
        fileName2 = QFileDialog.getOpenFileName(self, "选取Json", "./", "数据 (*.json)")

        with open(fileName2[0], 'r') as f:
            data = f.read()

        # global realdata
        # data = json.dumps(realdata, indent=2)
        # print(data)
        pos = []
        for i in range(len(data)):
            if data[i] == "'":
                pos.append(i)
        # print(pos)
        redata = data[:pos[0]] + "\\u0027" + data[pos[0] + 1:pos[1]] + "\\u0027" + data[pos[1] + 1:pos[
            2]] + "\\u0027" + data[pos[2] + 1:pos[3]] + "\\u0027" + data[pos[3] + 1:]

        resave = decode_encode.encode(redata, "key")
        resave = str(resave, encoding='utf-8')
        # print(resave)

        fileName3 = QFileDialog.getSaveFileName(self, "保存存档", "./", "存档 (*.autosave)")
        with open(fileName3[0], 'w') as f:
            f.write(resave)
