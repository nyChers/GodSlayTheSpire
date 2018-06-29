#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:  NingYu Zhang
# @Date:    Created on 2018/6/27 18:01
import json
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QTableWidget, QTableWidgetSelectionRange
from ui_MyWindow import Ui_Dialog
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import decode_encode

realdata = {}
cards_data = {}
relics_data = {}
potions_data = {}

cards = []
len_cards = 0
potions = []
len_potions = 0
relics = []
len_relics = 0


class MyWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 设置按钮连接
        self.ui.decodeautosave.clicked.connect(self.decodeautosave)
        self.ui.encodeJson.clicked.connect(self.encodeJson)
        self.ui.openfile.clicked.connect(self.openfile)
        self.ui.writefile.clicked.connect(self.writefile)

        self.ui.card_selectall.clicked.connect(self.card_selectall)
        self.ui.card_cancelall.clicked.connect(self.card_cancelall)
        self.ui.card_delete.clicked.connect(self.card_delete)
        self.ui.card_update.clicked.connect(self.card_update)
        self.ui.card_replace.clicked.connect(self.card_replace)
        self.ui.card_add.clicked.connect(self.card_add)

        # 设置cardstable
        # 列宽
        self.ui.curr_card_list.setColumnWidth(0, 170)
        self.ui.curr_card_list.setColumnWidth(1, 50)
        self.ui.curr_card_list.setColumnWidth(2, 140)
        self.ui.curr_card_list.setColumnWidth(3, 300)
        # 不可编辑
        self.ui.curr_card_list.setEditTriggers(QTableWidget.NoEditTriggers)

        # 读取数据
        global cards_data
        with open('cards.json', 'r', encoding='utf-8') as f:
            cards_data = json.load(f)
        global relics_data
        with open('relics.json', 'r', encoding='utf-8') as f:
            relics_data = json.load(f)
        global potions_data
        with open('potions.json', 'r', encoding='utf-8') as f:
            potions_data = json.load(f)

    # 读取存档写到json文件
    def decodeautosave(self):
        fileName1 = QFileDialog.getOpenFileName(self, "选取存档", "./", "存档 (*.autosave)")  # 设置文件扩展名过滤,注意用双分号间隔
        if fileName1[0] == '':
            return
        with open(fileName1[0], "rb") as f:
            old_autosave = f.read()
        # print(old_autosave)

        old_json = decode_encode.decode(old_autosave, "key")
        old_json = str(old_json, 'utf-8')
        # print(old_json)

        data = json.loads(old_json)
        # print(data)

        fileName2 = QFileDialog.getSaveFileName(self, "选取存档", "./", "存档 (*.json)")
        if fileName2[0] == '':
            return
        with open(fileName2[0], 'w') as f:
            json.dump(data, f, indent=2)

    # 将json文件转回autosave
    def encodeJson(self):
        fileName2 = QFileDialog.getOpenFileName(self, "选取Json", "./", "数据 (*.json)")
        if fileName2[0] == '':
            return
        with open(fileName2[0], 'r') as f:
            data = f.read()

        resave = decode_encode.encode(data, "key")
        resave = str(resave, encoding='utf-8')

        fileName3 = QFileDialog.getSaveFileName(self, "保存存档", "./", "存档 (*.autosave)")
        if fileName3[0] == '':
            return
        with open(fileName3[0], 'w') as f:
            f.write(resave)

    # 打开存档解码并读入数据到realdata
    def openfile(self):
        fileName = QFileDialog.getOpenFileName(self, "选取存档", "./", "存档 (*.autosave)")
        if fileName[0] == '':
            return
        with open(fileName[0], "rb") as f:
            old_autosave = f.read()

        b_realdata = decode_encode.decode(old_autosave, "key")
        s_realdata = str(b_realdata, 'utf-8')
        global realdata
        realdata = json.loads(s_realdata)
        self.read_display()

    # 写回存档
    def writefile(self):
        self.modify_4Attributes()
        global realdata
        s_realdata = json.dumps(realdata, indent=2)
        new_autosave = decode_encode.encode(s_realdata, "key")
        resave = str(new_autosave, encoding='utf-8')
        fileName = QFileDialog.getSaveFileName(self, "保存存档", "./", "存档 (*.autosave)")
        if fileName[0] == '':
            return
        with open(fileName[0], 'w') as f:
            f.write(resave)

    # 读取并显示数据
    def read_display(self):
        global cards_data, relics_data

        self.ui.max_health.setText(str(realdata['max_health']))
        self.ui.current_health.setText(str(realdata['current_health']))
        self.ui.gold.setText(str(realdata['gold']))
        self.ui.energy.setText(str(realdata['red']))

        global cards, len_cards
        cards = realdata['cards']
        len_cards = len(cards)

        ui_cardtable = self.ui.curr_card_list
        ui_cardtable.setRowCount(len_cards)
        for i in range(len_cards):
            ui_cardtable.setItem(i, 0, QTableWidgetItem(cards[i]['id']))
            ui_cardtable.setItem(i, 1, QTableWidgetItem(str(cards[i]['upgrades'])))
            ui_cardtable.setItem(i, 2, QTableWidgetItem(cards_data[cards[i]['id']]['NAME']))
            ui_cardtable.setItem(i, 3, QTableWidgetItem(cards_data[cards[i]['id']]['DESCRIPTION']))

    # 修改基础四属性
    def modify_4Attributes(self):
        global realdata
        realdata['max_health'] = int(self.ui.max_health.text())
        realdata['current_health'] = int(self.ui.current_health.text())
        realdata['gold'] = int(self.ui.gold.text())
        realdata['red'] = int(self.ui.energy.text())

    # 全选卡牌
    def card_selectall(self):
        ui_cardtable = self.ui.curr_card_list
        ui_cardtable.setRangeSelected(QTableWidgetSelectionRange(0, 0, len_cards - 1, 3), True)

    # 取消全选卡牌
    def card_cancelall(self):
        ui_cardtable = self.ui.curr_card_list
        ui_cardtable.setRangeSelected(QTableWidgetSelectionRange(0, 0, len_cards - 1, 3), False)

    # 获取选中卡牌
    def get_cardselect(self):
        ui_cardtable = self.ui.curr_card_list
        list_items = ui_cardtable.selectedItems()
        cnt_items = len(list_items)
        cnt_cards = int(cnt_items / 4)
        index = []
        for i in range(cnt_cards):
            index.append(ui_cardtable.row(list_items[4 * i]))
        return index

    # 删除选中卡牌
    def card_delete(self):
        ui_cardtable = self.ui.curr_card_list
        index = self.get_cardselect()
        index.reverse()
        for i in index:
            cards.pop(i)
        for i in index:
            ui_cardtable.removeRow(i)

    # 升级选中卡牌
    def card_update(self):
        ui_cardtable = self.ui.curr_card_list
        index = self.get_cardselect()
        pass

    # 替换选中卡牌
    def card_replace(self):
        ui_cardtable = self.ui.curr_card_list
        index = self.get_cardselect()
        pass

    # 添加卡牌
    def card_add(self):
        pass
