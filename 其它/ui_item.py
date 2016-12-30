# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_item.ui'
#
# Created: Thu Jan 15 01:31:11 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(280, 50)
        Form.setMinimumSize(QtCore.QSize(280, 50))
        Form.setMaximumSize(QtCore.QSize(280, 50))
        self.itemLayout = QtWidgets.QHBoxLayout(Form)
        self.itemLayout.setSpacing(5)
        self.itemLayout.setContentsMargins(10, 5, 15, 5)
        self.itemLayout.setObjectName("itemLayout")
        self.userLabel = QtWidgets.QLabel(Form)
        self.userLabel.setMinimumSize(QtCore.QSize(40, 40))
        self.userLabel.setMaximumSize(QtCore.QSize(40, 40))
        self.userLabel.setStyleSheet("QLabel#userLabel {\n"
"    image: url(:/res/resources/icon.ico);\n"
"}")
        self.userLabel.setLineWidth(0)
        self.userLabel.setText("")
        self.userLabel.setObjectName("userLabel")
        self.itemLayout.addWidget(self.userLabel)
        self.infoWidget = QtWidgets.QWidget(Form)
        self.infoWidget.setObjectName("infoWidget")
        self.infoLayout = QtWidgets.QVBoxLayout(self.infoWidget)
        self.infoLayout.setSpacing(2)
        self.infoLayout.setContentsMargins(3, 2, 0, 2)
        self.infoLayout.setObjectName("infoLayout")
        self.nameLabel = QtWidgets.QLabel(self.infoWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.infoLayout.addWidget(self.nameLabel)
        self.moodLabel = QtWidgets.QLabel(self.infoWidget)
        self.moodLabel.setStyleSheet("color: rgb(188, 188, 188);")
        self.moodLabel.setObjectName("moodLabel")
        self.infoLayout.addWidget(self.moodLabel)
        self.itemLayout.addWidget(self.infoWidget)
        self.timeLabel = QtWidgets.QLabel(Form)
        self.timeLabel.setMinimumSize(QtCore.QSize(30, 0))
        self.timeLabel.setMaximumSize(QtCore.QSize(30, 16777215))
        self.timeLabel.setStyleSheet("color: rgb(188, 188, 188);")
        self.timeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.timeLabel.setObjectName("timeLabel")
        self.itemLayout.addWidget(self.timeLabel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nameLabel.setText(_translate("Form", "ヽoo悾絔℅o。"))
        self.moodLabel.setText(_translate("Form", "<html><head/><body><a href=\"http://www.baidu.com\"><img src=\":/res/resources/icon_qzone.png\"/></a>发表图片</body></html>"))
        self.timeLabel.setText(_translate("Form", "昨天"))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

