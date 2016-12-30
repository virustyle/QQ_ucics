# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tip.ui'
#
# Created: Fri Jan 16 19:51:40 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(275, 184)
        Dialog.setMinimumSize(QtCore.QSize(275, 180))
        Dialog.setMaximumSize(QtCore.QSize(275, 184))
        Dialog.setWindowTitle("")
        Dialog.setStyleSheet("QDialog {\n"
"    background: transparent url(:/res/bg.jpg) no-repeat center center;\n"
"}\n"
"\n"
"QDialog > QWidget#widget_2 > QLabel {\n"
"    image: url(:/res/icon.ico);\n"
"}")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setMinimumSize(QtCore.QSize(0, 80))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.itemHeadLabel = QtWidgets.QLabel(self.widget)
        self.itemHeadLabel.setMinimumSize(QtCore.QSize(80, 80))
        self.itemHeadLabel.setMaximumSize(QtCore.QSize(80, 80))
        self.itemHeadLabel.setStyleSheet("QLabel#itemHeadLabel {\n"
"    background: transparent;\n"
"    image: url(:/res/icon.ico);\n"
"}")
        self.itemHeadLabel.setText("")
        self.itemHeadLabel.setOpenExternalLinks(True)
        self.itemHeadLabel.setObjectName("itemHeadLabel")
        self.horizontalLayout_2.addWidget(self.itemHeadLabel)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.itemNameLabel = QtWidgets.QLabel(self.widget_3)
        self.itemNameLabel.setStyleSheet("QLabel#itemNameLabel {\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.itemNameLabel.setOpenExternalLinks(True)
        self.itemNameLabel.setObjectName("itemNameLabel")
        self.verticalLayout_2.addWidget(self.itemNameLabel)
        self.itemMoodLabel = QtWidgets.QLabel(self.widget_3)
        self.itemMoodLabel.setStyleSheet("QLabel#itemMoodLabel {\n"
"    color: black;\n"
"}")
        self.itemMoodLabel.setOpenExternalLinks(True)
        self.itemMoodLabel.setObjectName("itemMoodLabel")
        self.verticalLayout_2.addWidget(self.itemMoodLabel)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.itemPicLabel_1 = QtWidgets.QLabel(self.widget_2)
        self.itemPicLabel_1.setText("")
        self.itemPicLabel_1.setObjectName("itemPicLabel_1")
        self.horizontalLayout.addWidget(self.itemPicLabel_1)
        self.itemPicLabel_2 = QtWidgets.QLabel(self.widget_2)
        self.itemPicLabel_2.setText("")
        self.itemPicLabel_2.setObjectName("itemPicLabel_2")
        self.horizontalLayout.addWidget(self.itemPicLabel_2)
        self.itemPicLabel_3 = QtWidgets.QLabel(self.widget_2)
        self.itemPicLabel_3.setText("")
        self.itemPicLabel_3.setObjectName("itemPicLabel_3")
        self.horizontalLayout.addWidget(self.itemPicLabel_3)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.itemHeadLabel.setToolTip(_translate("Dialog", "进入空间"))
        self.itemNameLabel.setToolTip(_translate("Dialog", "ヽoo悾絔℅o。 点击查看详细资料"))
        self.itemNameLabel.setText(_translate("Dialog", "<html><head/><body><p><a href=\"http://www.baidu.com\"><span style=\"color: black;text-decoration: none;text-overflow: ellipsis;white-space: nowrap;overflow: hidden;\">ヽoo悾絔℅o。</span></a></p></body></html>"))
        self.itemMoodLabel.setToolTip(_translate("Dialog", "点击查看心情"))
        self.itemMoodLabel.setText(_translate("Dialog", "<html><head/><body><p><a href=\"http://www.baidu.com\"><span style=\"color: black;text-decoration: none;text-overflow: ellipsis;white-space: nowrap;overflow: hidden;\">这个家伙太懒!什么都没说...</span></a></p></body></html>"))

import res_rc
