#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-1-16

@author: ヽoo悾絔℅o。

@email: 892768447@qq.com

@description: 
'''
from PyQt5.QtCore import QSize, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel


class Ui_Tip(object):
    def setupUi(self, Tip, name = "", head = "", mood = "", pic1 = "", pic2 = "", pic3 = ""):
        Tip.setObjectName("Tip")
        Tip.resize(275, 180)
        size = QSize(275, 180)
        Tip.setMinimumSize(size)
        Tip.setMaximumSize(size)
        Tip.setWindowTitle("")
        self.name = name
        self.head = head
        self.mood = mood
        self.pic1 = pic1
        self.pic2 = pic2
        self.pic3 = pic3

        self.mainWidget = QWidget(Tip)
        self.mainWidget.setObjectName("tip")

        self.verticalLayout = QVBoxLayout(self.mainWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QWidget(self.mainWidget)
        self.widget.setObjectName("widget")
        self.widget.setMinimumHeight(80)
        self.widget.setMaximumHeight(80)

        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.itemHeadLabel = QLabel(self.widget)
        self.itemHeadLabel.setMinimumSize(QSize(80, 80))
        self.itemHeadLabel.setMaximumSize(QSize(80, 80))
        self.itemHeadLabel.setOpenExternalLinks(True)
        self.itemHeadLabel.setObjectName("itemHeadLabel")
        self.horizontalLayout_2.addWidget(self.itemHeadLabel)
        self.widget_3 = QWidget(self.widget)

        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.itemNameLabel = QLabel(self.widget_3)

        # self.itemNameLabel.setOpenExternalLinks(True)
        self.itemNameLabel.setObjectName("itemNameLabel")
        self.verticalLayout_2.addWidget(self.itemNameLabel)
        self.itemMoodLabel = QLabel(self.widget_3)

        # self.itemMoodLabel.setOpenExternalLinks(True)
        self.itemMoodLabel.setObjectName("itemMoodLabel")
        self.verticalLayout_2.addWidget(self.itemMoodLabel)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QWidget(self.mainWidget)
        self.widget_2.setMinimumSize(QSize(0, 80))
        self.widget_2.setMaximumSize(QSize(16777215, 80))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.itemPicLabel_1 = QLabel(self.widget_2)
        self.itemPicLabel_1.setObjectName("itemPicLabel_1")
        self.horizontalLayout.addWidget(self.itemPicLabel_1)
        self.itemPicLabel_2 = QLabel(self.widget_2)
        self.itemPicLabel_2.setObjectName("itemPicLabel_2")
        self.horizontalLayout.addWidget(self.itemPicLabel_2)
        self.itemPicLabel_3 = QLabel(self.widget_2)
        self.itemPicLabel_3.setObjectName("itemPicLabel_3")
        self.horizontalLayout.addWidget(self.itemPicLabel_3)
        self.verticalLayout.addWidget(self.widget_2)

        self.mainWidget.setLayout(self.verticalLayout)

        self.retranslateUi(self.mainWidget)
        QMetaObject.connectSlotsByName(Tip)

    def retranslateUi(self, Tip):
        _translate = QCoreApplication.translate
        if self.head:
            self.itemHeadLabel.setStyleSheet("QLabel#itemHeadLabel {\n    image: url(%s);\n}" % self.head)
        self.itemHeadLabel.setToolTip(_translate("Tip", "进入空间"))
        if self.name:
            self.itemNameLabel.setToolTip(_translate("Tip", "%s 点击查看详细资料" % self.name))
            self.itemNameLabel.setText(_translate("Tip", "<html><head/><body><p><a href=\"http://www.baidu.com\"><span style=\"color: black;text-decoration: none;text-overflow: ellipsis;white-space: nowrap;overflow: hidden;\">%s</span></a></p></body></html>" % self.name))
        self.itemMoodLabel.setToolTip(_translate("Tip", "点击查看心情"))
        self.itemMoodLabel.setText(_translate("Tip", "<html><head/><body><p><a href=\"http://www.baidu.com\"><span style=\"color: black;text-decoration: none;text-overflow: ellipsis;white-space: nowrap;overflow: hidden;\">%s</span></a></p></body></html>" % self.mood if self.mood else "这个家伙太懒!什么都没说..."))
