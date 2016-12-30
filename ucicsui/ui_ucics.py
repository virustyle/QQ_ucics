#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-1-9

@author: ヽoo悾絔℅o。

@email: 892768447@qq.com

@description: 界面布局
'''


from PyQt5.QtCore import QSize, Qt, QCoreApplication, QMetaObject
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, \
    QVBoxLayout, QTabWidget, QTreeWidget, QFrame

from .lineedit import LineEdit


class Ui_Ucics(object):

    def setupUi(self, Ucics):
        size_280_650 = QSize(280, 650)
        size_20_20 = QSize(20, 20)
        size_25_25 = QSize(25, 25)
        Ucics.setObjectName("Ucics")
        Ucics.resize(size_280_650)    # 窗口大小
        Ucics.setMinimumSize(size_280_650)    # 设置最小大小
        Ucics.setMaximumSize(size_280_650)    # 设置最大大小
        Ucics.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)    # 无边框
        Ucics.setMouseTracking(True)    # 可拖动
        Ucics.setContextMenuPolicy(Qt.NoContextMenu)    # 禁止上下文菜单

        # 由于父QWidget无法通过样式设置背景
        # 所以这里把所有控件放到子QWidget中
        self.bgWidget = QWidget(Ucics)
        self.bgWidget.setObjectName("bgWidget")

        # 顶部标题图标 最小化 关闭
        self.topWidget = QWidget(self.bgWidget)
        self.topWidget.setMaximumHeight(25)
        self.topWidget.setObjectName("topWidget")
        # --布局
        topLayout = QHBoxLayout(self.topWidget)
        topLayout.setSpacing(1)
        topLayout.setContentsMargins(0, 0, 0, 0)
        topLayout.setObjectName("topLayout")
        # ----icon
        self.iconLabel = QLabel(self.bgWidget)
        self.iconLabel.setMinimumSize(size_25_25)
        self.iconLabel.setMaximumSize(size_25_25)
        self.iconLabel.setObjectName("iconLabel")
        # ----最小化按钮
        self.minButton = QPushButton(self.bgWidget)
        self.minButton.setMinimumSize(size_25_25)
        self.minButton.setMaximumSize(size_25_25)
        self.minButton.setObjectName("minButton")
        # ----关闭按钮
        self.closeButton = QPushButton(self.bgWidget)
        self.closeButton.setMinimumSize(size_25_25)
        self.closeButton.setMaximumSize(size_25_25)
        self.closeButton.setObjectName("closeButton")
        # ----添加到布局中
        topLayout.addWidget(self.iconLabel, 0, Qt.AlignLeft)
        topLayout.addWidget(self.minButton, 1, Qt.AlignRight)
        topLayout.addWidget(self.closeButton, 0, Qt.AlignRight)

        # 头像 昵称 心情 天气等
        self.headWidget = QWidget(self.bgWidget)
        self.headWidget.setMinimumHeight(90)
        self.headWidget.setMaximumHeight(90)
        self.headWidget.setObjectName("headWidget")
        # --布局
        headLayout = QHBoxLayout(self.headWidget)
        headLayout.setSpacing(6)
        headLayout.setContentsMargins(9, 20, 9, 6)
        headLayout.setObjectName("headLayout")
        # ----头像
        self.headLabel = QLabel(self.headWidget)
        self.headLabel.setMinimumWidth(60)
        self.headLabel.setMaximumWidth(60)
        self.headLabel.setToolTip("")
        self.headLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.headLabel.setObjectName("headLabel")
        # ----中间部分(昵称和签名等)
        self.headInfoWidget = QWidget(self.headWidget)
        self.headInfoWidget.setObjectName("headInfoWidget")
        # ------中间部分布局
        headInfoLayout = QVBoxLayout(self.headInfoWidget)
        headInfoLayout.setSpacing(1)
        headInfoLayout.setContentsMargins(0, 0, 0, 0)
        headInfoLayout.setObjectName("headInfoLayout")
        # --------昵称
        self.nameLabel = QLabel(self.headInfoWidget)
        self.nameLabel.setMinimumHeight(20)
        self.nameLabel.setMaximumHeight(20)
        self.nameLabel.setObjectName("nameLabel")
        # --------签名
        self.moodEdit = LineEdit(self.headInfoWidget)
        self.moodEdit.setMinimumHeight(20)
        self.moodEdit.setMaximumHeight(20)
        self.moodEdit.setFrame(False)    # 去掉边框
        # self.moodEdit.setClearButtonEnabled(True)    # 添加清除按钮
        self.moodEdit.setObjectName("moodEdit")
        # --------工具
        self.toolWidget = QWidget(self.headInfoWidget)
        self.toolWidget.setMinimumHeight(20)
        self.toolWidget.setMaximumHeight(20)
        self.toolWidget.setObjectName("toolWidget")
        # ----------工具布局
        toolLayout = QHBoxLayout(self.toolWidget)
        toolLayout.setSpacing(1)
        toolLayout.setContentsMargins(0, 0, 0, 0)
        toolLayout.setObjectName("toolLayout")
        # ------------空间
        self.qzoneButton = QPushButton(self.toolWidget)
        self.qzoneButton.setMinimumSize(size_20_20)
        self.qzoneButton.setMaximumSize(size_20_20)
        self.qzoneButton.setObjectName("qzoneButton")
        # ------------皮肤
        self.skinButton = QPushButton(self.toolWidget)
        self.skinButton.setMinimumSize(size_20_20)
        self.skinButton.setMaximumSize(size_20_20)
        self.skinButton.setObjectName("skinButton")
        # ------------添加到布局
        toolLayout.addWidget(self.qzoneButton, 0, Qt.AlignLeft)
        toolLayout.addWidget(self.skinButton, 1, Qt.AlignLeft)
        # --------添加到布局
        headInfoLayout.addWidget(self.nameLabel)
        headInfoLayout.addWidget(self.moodEdit)
        headInfoLayout.addWidget(self.toolWidget)
        # ----天气
        self.weatherLabel = QLabel(self.headWidget)
        self.weatherLabel.setMinimumWidth(60)
        self.weatherLabel.setMaximumWidth(60)
        self.weatherLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.weatherLabel.setObjectName("weatherLabel")
        # ----添加到布局中
        headLayout.addWidget(self.headLabel, 0, Qt.AlignLeft)
        headLayout.addWidget(self.headInfoWidget, 0, Qt.AlignCenter)
        headLayout.addWidget(self.weatherLabel, 0, Qt.AlignRight)

        # 搜索输入框
        self.searchEdit = LineEdit(self.bgWidget)
        self.searchEdit.setFrame(False)
        # self.searchEdit.setClearButtonEnabled(True)
        self.searchEdit.setObjectName("searchEdit")

        # tab
        self.tabWidget = QTabWidget(self.bgWidget)
        self.tabWidget.setUsesScrollButtons(False)    # 取消两个切换按钮
        self.tabWidget.setDocumentMode(True)    # 取消边框
        self.tabWidget.setObjectName("tabWidget")
        # --分组
        self.tabGroup = QWidget(self.tabWidget)
        self.tabGroup.setObjectName("tabGroup")
        # ----分组布局
        groupVerticalLayout = QVBoxLayout(self.tabGroup)
        groupVerticalLayout.setSpacing(0)
        groupVerticalLayout.setContentsMargins(0, 0, 0, 0)
        groupVerticalLayout.setObjectName("groupVerticalLayout")
        # ------分组list控件
        self.groupTreeWidget = QTreeWidget(self.tabGroup)
        self.groupTreeWidget.setFrameShape(QFrame.NoFrame)
        self.groupTreeWidget.setFrameStyle(QFrame.NoFrame)
        self.groupTreeWidget.setLineWidth(0)
        self.groupTreeWidget.setIndentation(0)
        self.groupTreeWidget.setRootIsDecorated(False)
        self.groupTreeWidget.setExpandsOnDoubleClick(False)
        self.groupTreeWidget.header().setVisible(False)
        self.groupTreeWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.groupTreeWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.groupTreeWidget.setObjectName("groupTreeWidget")
        # ----添加到布局
        groupVerticalLayout.addWidget(self.groupTreeWidget)
        # --历史
        self.tabHistory = QWidget(self.tabWidget)
        self.tabHistory.setObjectName("tabHistory")
        # ----历史布局
        historyVerticalLayout = QVBoxLayout(self.tabHistory)
        historyVerticalLayout.setSpacing(0)
        historyVerticalLayout.setContentsMargins(0, 0, 0, 0)
        historyVerticalLayout.setObjectName("historyVerticalLayout")
        # ------历史list控件
        self.historyTreeWidget = QTreeWidget(self.tabHistory)
        self.historyTreeWidget.setFrameShape(QFrame.NoFrame)
        self.historyTreeWidget.setFrameStyle(QFrame.NoFrame)
        self.historyTreeWidget.setLineWidth(0)
        self.historyTreeWidget.setIndentation(0)
        self.historyTreeWidget.setRootIsDecorated(False)
        self.historyTreeWidget.setExpandsOnDoubleClick(False)
        self.historyTreeWidget.header().setVisible(False)
        self.historyTreeWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.historyTreeWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.historyTreeWidget.setObjectName("historyTreeWidget")
        # ----添加到布局
        historyVerticalLayout.addWidget(self.historyTreeWidget)
        # 添加到tab中
        self.tabWidget.addTab(self.tabGroup, "")
        self.tabWidget.addTab(self.tabHistory, "")

        # 整体布局
        verticalLayout = QVBoxLayout(self.bgWidget)
        verticalLayout.setSpacing(0)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setObjectName("verticalLayout")
        verticalLayout.addWidget(self.topWidget)
        verticalLayout.addWidget(self.headWidget)
        verticalLayout.addWidget(self.searchEdit)
        verticalLayout.addWidget(self.tabWidget)

        # bg
        layout = QVBoxLayout(Ucics)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.bgWidget)

        # 初始化一些设置
        _translate = QCoreApplication.translate
        Ucics.setWindowTitle(_translate("Ucics", "UCICS"))
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tabGroup), _translate("tabGroup", "分组"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tabHistory), _translate("tabHistory", "历史"))
        QMetaObject.connectSlotsByName(Ucics)
