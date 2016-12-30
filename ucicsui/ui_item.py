#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-1-9

@author: ヽoo悾絔℅o。

@email: 892768447@qq.com

@description: item布局
'''
from PyQt5.QtCore import QSize, Qt, QCoreApplication, QMetaObject
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout


class Ui_Item(object):

    def setupUi(self, Item, userhead, name, mood, times, which = 0):
        size_280_50 = QSize(280, 50)
        Item.setObjectName("Item")
        Item.resize(size_280_50)    # 窗口大小
        Item.setMinimumSize(size_280_50)    # 设置最小大小
        Item.setMaximumSize(size_280_50)    # 设置最大大小
        Item.setWindowFlags(Qt.FramelessWindowHint)    # 无边框

        # 由于父QWidget无法通过样式设置背景
        # 所以这里把所有控件放到子QWidget中
        self.itemWidget = QWidget(Item)
        self.itemWidget.setObjectName("childItem")

        # 用户头像
        self.userLabel = QLabel(self.itemWidget)
        self.userLabel.setMinimumSize(QSize(40, 40))
        self.userLabel.setMaximumSize(QSize(40, 40))
        self.userLabel.setLineWidth(0)
        self.userLabel.setObjectName("userLabel")

        # 用户昵称和说说
        self.infoWidget = QWidget(self.itemWidget)
        self.infoWidget.setObjectName("infoWidget")
        # --昵称
        self.nameLabel = QLabel(self.infoWidget)
        self.nameLabel.setObjectName("nameLabel")
        # --说说
        self.moodLabel = QLabel(self.infoWidget)
        self.moodLabel.setObjectName("moodLabel")
        # --布局
        infoLayout = QVBoxLayout(self.infoWidget)
        infoLayout.setSpacing(2)
        infoLayout.setContentsMargins(3, 2, 0, 2)
        # 添加到布局中
        infoLayout.addWidget(self.nameLabel)
        infoLayout.addWidget(self.moodLabel)

        # 时间
        self.timeLabel = QLabel(self.itemWidget)
        self.timeLabel.setMinimumWidth(30)
        self.timeLabel.setMaximumWidth(30)
        self.timeLabel.setAlignment(Qt.AlignRight | Qt.AlignTop)
        self.timeLabel.setObjectName("timeLabel")

        # 整体布局
        itemLayout = QHBoxLayout(self.itemWidget)
        itemLayout.setSpacing(5)
        itemLayout.setContentsMargins(10, 5, 15, 5)

        # 添加到布局中
        itemLayout.addWidget(self.userLabel)
        itemLayout.addWidget(self.infoWidget)
        itemLayout.addWidget(self.timeLabel)

        layout = QHBoxLayout(Item)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.itemWidget)

        # 初始化一些设置
        _translate = QCoreApplication.translate
        self.userLabel.setStyleSheet("QLabel#userLabel {\n    image: url(%s);\n}" % userhead)
        self.nameLabel.setText(_translate("Item", name))
        self.moodLabel.setText(_translate("Item", mood))
        if which:
            self.timeLabel.setText(_translate("Item", times))
        QMetaObject.connectSlotsByName(Item)
