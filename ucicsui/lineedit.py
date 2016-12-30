#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-1-15

@author: ヽoo悾絔℅o。

@email: 892768447@qq.com

@description: QLineEdit重写焦点事件
'''
from PyQt5.QtWidgets import QLineEdit


class LineEdit(QLineEdit):

    def __init__(self, parent = None):
        super(LineEdit, self).__init__(parent)

    def focusOutEvent(self, event):
        self.setClearButtonEnabled(False)    # 设置清空按钮隐藏
        super(LineEdit, self).focusOutEvent(event)

    def focusInEvent(self, event):
        self.setClearButtonEnabled(True)    # 显示可清空按钮
        super(LineEdit, self).focusInEvent(event)
