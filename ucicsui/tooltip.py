#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-1-16

@author: ヽoo悾絔℅o。

@email: 892768447@qq.com

@description: 个性化提示框ToolTip
'''


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from ucicslib.single import Single

from .ui_tip import Ui_Tip


class ToolTip(Single, QDialog, Ui_Tip):

    def __init__(self, parent = None, name = "", head = "", mood = "", pic1 = "", pic2 = "", pic3 = ""):
        super(ToolTip, self).__init__(parent)
        self.setWindowFlags(Qt.ToolTip | Qt.FramelessWindowHint)
        self.setupUi(self, name, head, mood, pic1, pic2, pic3)
        print("id: ", id(self))
        self.showing = False

    def isShow(self):
        return self.showing

    # 增加一个自定义show方法
    # obj控件对象--x坐标--y坐标--width主窗口宽度--height主窗口高度

    def show(self, obj, x, y, width, height):
        print(self.isShow())
        if self.isShow():
            self.hide()
            self.showing = False
        print("x: ", x, " y: ", y, " w: ", width, " h: ", height)
        # 判断应该显示的位置
        if x < self.width() + 10:
            # 如果当前主窗口的左边距离 < 提示框的宽度 + 10
            tx = x + width + 10    # 应该显示在窗口的右边---坐标为 x+ width + 10
            print("tx: ", tx)
        else:
            # 如果当前主窗口左边的距离 > 提示框的宽度 + 10
            tx = x - self.width() - 10    # 应该显示在窗口的左边---坐标为 x - self.width() - 10
            print("tx: ", tx)
        if y + self.height() > height:
            # 如果在最下面时
            ty = y - self.height()
            print("ty: ", ty)
        else:
            ty = y
            print("ty: ", ty)
        self.move(tx, ty)
        print(self.frameGeometry().topLeft())
        self.showing = True
        super(ToolTip, self).show()

