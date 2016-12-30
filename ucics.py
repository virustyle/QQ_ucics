#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-1-9

@author: ヽoo悾絔℅o。

@email: 892768447@qq.com

@description: 主程序
'''

# import ctypes.wintypes
import pickle
import sqlite3
import sys

from PyQt5.QtCore import Qt, QFile, QTextStream
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication

from ucicslib import cache
from ucicslib.entity import Users, Groups
from ucicslib.skylark import Database
from ucicslib.user_item import User_Item
from ucicsui.ui_ucics import Ui_Ucics


class Ucics(QWidget, Ui_Ucics):

    def __init__(self, parent = None):
        super(Ucics, self).__init__(parent)
        desktop = QApplication.desktop()
        self.dwidth = desktop.width()    # 获取桌面宽度
        self.dheight = desktop.height()    # 获取桌面高度
        self.setupUi(self)    # 初始化界面
        self.initPos()    # 初始化位置
        self.initSkin()    # 初始化皮肤
        # 背景透明 圆角窗口
        self.setAttribute(Qt.WA_TranslucentBackground)
        # self.installEventFilter(self)
        # self.headLabel.installEventFilter(self)

    # win32gui.PostMessage(hWnd,message,wParam,lParam)
#    def nativeEvent(self, eventType, message):
#        retval, result = super(Ucics, self).nativeEvent(eventType, message)
#        if eventType == "windows_generic_MSG":
#            msg = ctypes.wintypes.MSG.from_address(message.__int__())
#             print("hWnd: ", msg.hWnd)
#             print("lParam: ", msg.lParam)
#             print("message: ", msg.message)
#             print("pt: ", msg.pt)
#             print("time: ", msg.time)
#             print("wParam: ", msg.wParam)
#        return retval, result

    def closeEvent(self, event):
        # 拦截关闭,保存窗口位置
        with open("pos.dat", "wb") as fp:
            pickle.dump(cache.globalPos, fp)
        QApplication.instance().quit()
        # return QWidget.closeEvent(self, event)

    # def eventFilter(self, s, e):
        # print(s, e)
        # if s == self.headLabel and e.type() == QEvent.Enter:
            # t = ToolTip(self, "ヽoo悾絔℅o。", "resources/icon.ico", "", "data/head/1.png" "data/head/2.png" "data/head/3.png").show(s, self.frameGeometry().topLeft().x(), e.globalPos().y(), self.width(), self.dheight)
            # t.move(938, 120)
            # t.show()
        # return super(Ucics, self).eventFilter(s, e)

    # 鼠标按下事件
    def mousePressEvent(self, event):
        # 鼠标点击事件
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            cache.globalPos = event.globalPos() - self.dragPosition
            self.move(cache.globalPos)
            event.accept()

    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        print("mouse release: ", self.x(), self.y())
        if self.y() < 1:    # 上边
            # self.resize(self.width(), 1)
            self.move(self.x(), 1 - self.height())
        elif self.x() < 1:    # 左边
            # self.resize(1, self.height())
            self.move(1 - self.width(), self.y())
        elif self.x() > (self.dwidth - self.width()):    # 右边
            # self.resize(1, self.height())
            self.move(self.dwidth - 1 , self.y())
        event.accept()

    # 鼠标进入事件
    def enterEvent(self, event):
        print("enterEvent: ", self.x(), self.y())
        if self.y() <= 1 - self.height():
            # 鼠标进入上方
            self.move(self.x(), 0)
        elif self.x() <= 1 - self.width():
            # 鼠标进入左边
            self.move(0, self.y())
        elif self.x() >= self.x() >= self.dwidth - 1:
            # 鼠标进入右边
            self.move(self.dwidth - self.width(), self.y())

    # 鼠标移出
    def leaveEvent(self, event):
        if self.y() == 0:
            # self.resize(self.width(), 1)
            self.move(self.x(), 1 - self.height())
        elif self.x() == 0:
            # self.resize(1, self.height())
            self.move(1 - self.width(), self.y())
        elif self.x() == self.dwidth - self.width():
            # self.resize(1, self.height())
            self.move(self.dwidth - 1, self.y())

    # 最小化单击事件
    def on_minButton_clicked(self):
        self.showMinimized()

    # 关闭点击事件
    def on_closeButton_clicked(self):
        self.close()

    def on_groupTreeWidget_itemExpanded(self, item):
        print("展开: ", item)

    def on_groupTreeWidget_itemCollapsed(self, item):
        print("关闭: ", item)

    # QTreeWidget父节点单击事件
    def on_groupTreeWidget_itemClicked(self, item, column):
        # print(item.isExpanded())
        if item.childCount() > 0:
            # 如果含有child则展开或者关闭
            if item.isExpanded():
                # 如果展开则关闭
                item.setExpanded(False)
            else:
                item.setExpanded(True)

    def test(self):
        self.nameLabel.setText("ヽoo悾絔℅o。")

    def initPos(self):
        try:
            with open("pos.dat", "rb") as fp:
                try:
                    pos = pickle.load(fp)
                    fp.close()
                    cache.globalPos = pos
                    self.setGeometry(pos.x(), pos.y(), self.width(), self.height())
                except Exception as e:
                    print(e)
        except FileNotFoundError as e:
            print(e)

    # 初始化界面皮肤
    def initSkin(self):
        skin = QFile("resources/themes/default.qss")
        if not skin.exists() or not skin.open(QFile.ReadOnly | QFile.Text):
            del skin
        else:
            qts = QTextStream(skin)
            qts.setCodec("UTF-8")
            data = qts.readAll()
            skin.close()
            del skin
            self.setStyleSheet(data)

    def initData(self):
        # 初始化分组arrow图标
        icon = QIcon()
        icon.addPixmap(QPixmap("resources/arrow_right.png"), state = QIcon.Off)
        icon.addPixmap (QPixmap("resources/arrow_down.png"), state = QIcon.On)
        cache.item_icon = icon
        del icon
        groups = Groups.select()    # 查询所有分组
        print(groups.sql)
        for group in groups:
            print(group.id, group.name)
            # 根据数据动态生成item
            item = User_Item(self.groupTreeWidget, group.name)
            item.setUsers(Users.where(Users.gid == group.id).select())
            print (Users)

if __name__ == "__main__":
    Database.set_dbapi(sqlite3)
    Database.set_autocommit(True)
    Database.config(db = "database/data.sqlite3")
    app = QApplication(sys.argv)
    window = Ucics()
    window.test()
    window.show()
    window.initData()
    sys.exit(app.exec_())
