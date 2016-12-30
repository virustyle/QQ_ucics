#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-1-14

@author: ヽoo悾絔℅o。

@email: 892768447@qq.com

@description: 自定义用户item
'''
'''
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QTreeWidgetItem, QWidget
'''
# 自定义的子Item控件

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem

from ucicslib import cache
from ucicsui.ui_item import Ui_Item


class Child_Item(QWidget, Ui_Item):

    def __init__(self, parent = None, userhead = "", name = "", mood = "", times = "", which = 0):
        # print(type(parent))
        super(Child_Item, self).__init__(parent)
        self.setupUi(self, userhead, name, mood, times, which)

class User_Item(QTreeWidgetItem):

    def __init__(self, parent = None, text = "", which = 0):
        # print(type(parent))
        QTreeWidgetItem.__init__(self, parent)
        self.setSizeHint(0, QSize(280, 30))    # 设置Item大小
        self.setTitle(text)    # 设置该Item的文字
        self.setIcon(0, cache.item_icon)    # 设置展开和关闭时候的图标
        self.which = which

    def setTitle(self, text = ""):
        self.setText(0, text)

    def setUsers(self, users = None):
        for user in users:
            # print(user)
            childItem = QTreeWidgetItem(self)
            childWidget = Child_Item(None, user.head, user.name, user.mood, user.time, self.which)
            self.treeWidget().setItemWidget(childItem, 0, childWidget)
        cache.user_items.append(self)    # 把该节点保存到数组用(方便下次启动快速显示)
