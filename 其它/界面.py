# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '界面.ui'
#
# Created: Thu Jan 15 18:54:16 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ucics(object):
    def setupUi(self, ucics):
        ucics.setObjectName("ucics")
        ucics.setWindowModality(QtCore.Qt.NonModal)
        ucics.resize(280, 650)
        ucics.setMinimumSize(QtCore.QSize(280, 650))
        ucics.setMaximumSize(QtCore.QSize(280, 650))
        ucics.setMouseTracking(True)
        ucics.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ucics.setWindowIcon(icon)
        ucics.setStyleSheet("QWidget {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QWidget#ucics {\n"
"    image: url(:/res/resources/themes/default/bg.jpg);\n"
"    qproperty-windowIcon: url(resources/icon.ico);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(ucics)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.operationLayout = QtWidgets.QHBoxLayout()
        self.operationLayout.setSpacing(1)
        self.operationLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.operationLayout.setContentsMargins(0, -1, 0, -1)
        self.operationLayout.setObjectName("operationLayout")
        self.iconLabel = QtWidgets.QLabel(ucics)
        self.iconLabel.setMinimumSize(QtCore.QSize(25, 25))
        self.iconLabel.setMaximumSize(QtCore.QSize(25, 25))
        self.iconLabel.setStyleSheet("QLabel#iconLabel {\n"
"    image: url(:/res/resources/icon.ico);\n"
"    padding: 2px;\n"
"}")
        self.iconLabel.setText("")
        self.iconLabel.setObjectName("iconLabel")
        self.operationLayout.addWidget(self.iconLabel)
        self.minButton = QtWidgets.QPushButton(ucics)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minButton.sizePolicy().hasHeightForWidth())
        self.minButton.setSizePolicy(sizePolicy)
        self.minButton.setMinimumSize(QtCore.QSize(25, 25))
        self.minButton.setMaximumSize(QtCore.QSize(25, 25))
        self.minButton.setStyleSheet("/*最小化按钮*/\n"
"QPushButton#minButton {\n"
"    image: url(:/res/resources/min_button.png);\n"
"    background: transparent;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton#minButton:hover {\n"
"    image: url(:/res/resources/min_button.png);\n"
"    background: rgba(255, 255, 255, 100);\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"}")
        self.minButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Administrator/.designer/close_normal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minButton.setIcon(icon1)
        self.minButton.setAutoDefault(False)
        self.minButton.setDefault(False)
        self.minButton.setFlat(False)
        self.minButton.setObjectName("minButton")
        self.operationLayout.addWidget(self.minButton)
        self.closeButton = QtWidgets.QPushButton(ucics)
        self.closeButton.setMinimumSize(QtCore.QSize(25, 25))
        self.closeButton.setMaximumSize(QtCore.QSize(25, 25))
        self.closeButton.setStyleSheet("/*关闭按钮*/\n"
"QPushButton#closeButton {\n"
"    image: url(:/res/resources/close_button.png);\n"
"    background: transparent;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton#closeButton:hover {\n"
"    image: url(:/res/resources/close_button.png);\n"
"    background: #D44027;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"}")
        self.closeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Administrator/.designer/min_normal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setObjectName("closeButton")
        self.operationLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.operationLayout)
        self.headWidget = QtWidgets.QWidget(ucics)
        self.headWidget.setMinimumSize(QtCore.QSize(0, 90))
        self.headWidget.setMaximumSize(QtCore.QSize(16777215, 90))
        self.headWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.headWidget.setObjectName("headWidget")
        self.headLayout = QtWidgets.QHBoxLayout(self.headWidget)
        self.headLayout.setContentsMargins(-1, 20, -1, 6)
        self.headLayout.setObjectName("headLayout")
        self.headLabel = QtWidgets.QLabel(self.headWidget)
        self.headLabel.setMinimumSize(QtCore.QSize(60, 0))
        self.headLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.headLabel.setStyleSheet("QLabel#headLabel {\n"
"    image: url(:/res/resources/icon.ico);\n"
"}\n"
"QLabel#headLabel:hover {\n"
"    border-color: rgb(0, 170, 255);\n"
"}")
        self.headLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.headLabel.setLineWidth(0)
        self.headLabel.setText("")
        self.headLabel.setPixmap(QtGui.QPixmap(":/res/icon.ico"))
        self.headLabel.setObjectName("headLabel")
        self.headLayout.addWidget(self.headLabel)
        self.headInfoLayout = QtWidgets.QVBoxLayout()
        self.headInfoLayout.setSpacing(1)
        self.headInfoLayout.setObjectName("headInfoLayout")
        self.nameEdit = QtWidgets.QLineEdit(self.headWidget)
        self.nameEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.nameEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.nameEdit.setFrame(False)
        self.nameEdit.setReadOnly(True)
        self.nameEdit.setObjectName("nameEdit")
        self.headInfoLayout.addWidget(self.nameEdit)
        self.moodEdit = QtWidgets.QLineEdit(self.headWidget)
        self.moodEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.moodEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.moodEdit.setStyleSheet("QLineEdit#moodEdit {\n"
"    \n"
"    border-color: rgb(255, 255, 0);\n"
"}")
        self.moodEdit.setFrame(False)
        self.moodEdit.setDragEnabled(False)
        self.moodEdit.setClearButtonEnabled(True)
        self.moodEdit.setObjectName("moodEdit")
        self.headInfoLayout.addWidget(self.moodEdit)
        self.toolWidget = QtWidgets.QWidget(self.headWidget)
        self.toolWidget.setMinimumSize(QtCore.QSize(0, 20))
        self.toolWidget.setMaximumSize(QtCore.QSize(16777215, 20))
        self.toolWidget.setObjectName("toolWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.toolWidget)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.qzoneButton = QtWidgets.QPushButton(self.toolWidget)
        self.qzoneButton.setMinimumSize(QtCore.QSize(20, 20))
        self.qzoneButton.setMaximumSize(QtCore.QSize(20, 20))
        self.qzoneButton.setText("")
        self.qzoneButton.setObjectName("qzoneButton")
        self.horizontalLayout.addWidget(self.qzoneButton)
        self.skinButton = QtWidgets.QPushButton(self.toolWidget)
        self.skinButton.setMinimumSize(QtCore.QSize(20, 20))
        self.skinButton.setMaximumSize(QtCore.QSize(20, 20))
        self.skinButton.setText("")
        self.skinButton.setObjectName("skinButton")
        self.horizontalLayout.addWidget(self.skinButton)
        self.headInfoLayout.addWidget(self.toolWidget)
        self.headLayout.addLayout(self.headInfoLayout)
        self.weatherLabel = QtWidgets.QLabel(self.headWidget)
        self.weatherLabel.setMinimumSize(QtCore.QSize(60, 0))
        self.weatherLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.weatherLabel.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.weatherLabel.setText("")
        self.weatherLabel.setObjectName("weatherLabel")
        self.headLayout.addWidget(self.weatherLabel)
        self.verticalLayout.addWidget(self.headWidget)
        self.searchEdit = QtWidgets.QLineEdit(ucics)
        self.searchEdit.setStyleSheet("/*\n"
"输入框样式\n"
"选中的文字颜色\n"
"selection-color: white;\n"
"选中的文字背景底色\n"
"selection-background-color: blue;\n"
"*/\n"
"QLineEdit#searchEdit {\n"
"    height: 30px;\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(0, 0, 0, 70);\n"
"    qproperty-placeholderText:  \"搜索: 联系人\";\n"
"}\n"
"/*输入框鼠标悬停样式*/\n"
"QLineEdit#searchEdit:hover {\n"
"    background: rgba(0, 0, 0, 60);\n"
"}")
        self.searchEdit.setInputMask("")
        self.searchEdit.setMaxLength(32767)
        self.searchEdit.setFrame(False)
        self.searchEdit.setClearButtonEnabled(True)
        self.searchEdit.setObjectName("searchEdit")
        self.verticalLayout.addWidget(self.searchEdit)
        self.tabWidget = QtWidgets.QTabWidget(ucics)
        self.tabWidget.setStyleSheet("/*tab*/\n"
"QTabWidget::tab-bar {\n"
"    height: 35px;\n"
"    alignment: center;\n"
"}\n"
"QTabWidget#tabWidget QTabBar::tab {\n"
"    width: 140px;\n"
"    height: 35px;\n"
"}\n"
"/*第一个tab*/\n"
"QTabWidget#tabWidget QTabBar::tab:first {\n"
"    background: transparent url(:/res/resources/group_normal.png) no-repeat center center;\n"
"}\n"
"QTabWidget#tabWidget QTabBar::tab:first:hover {\n"
"    background: transparent url(:/res/resources/group_hover.png) no-repeat center center;\n"
"}\n"
"QTabWidget#tabWidget QTabBar::tab:first:selected {\n"
"    background: transparent url(:/res/resources/group_pressed.png) no-repeat center center;\n"
"}\n"
"/*第二个tab*/\n"
"QTabWidget#tabWidget QTabBar::tab:last {\n"
"    background: transparent url(:/res/resources/history_normal.png) no-repeat center center;\n"
"}\n"
"QTabWidget#tabWidget QTabBar::tab:last:hover {\n"
"    background: transparent url(:/res/resources/history_hover.png) no-repeat center center;\n"
"}\n"
"QTabWidget#tabWidget QTabBar::tab:last:selected {\n"
"    background: transparent url(:/res/resources/history_pressed.png) no-repeat center center;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabGroup = QtWidgets.QWidget()
        self.tabGroup.setStyleSheet("")
        self.tabGroup.setObjectName("tabGroup")
        self.groupVerticalLayout = QtWidgets.QVBoxLayout(self.tabGroup)
        self.groupVerticalLayout.setSpacing(0)
        self.groupVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupVerticalLayout.setObjectName("groupVerticalLayout")
        self.groupTreeWidget = QtWidgets.QTreeWidget(self.tabGroup)
        self.groupTreeWidget.setStyleSheet("\n"
"QTreeWidget::branch {\n"
"    image: none;\n"
"}\n"
"\n"
"QTreeWidget::item:hover {\n"
"    color: black;\n"
"    background: rgba(0, 0, 0, 20);\n"
"}\n"
"\n"
"QTreeWidget::item:selected{\n"
"    color: black;\n"
"    border-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTreeWidget::item:selected:active{\n"
"    color: black;\n"
"    border-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));\n"
"    background: transparent;\n"
"}\n"
"\n"
"QLabel#moodLabel {\n"
"    color: gray\n"
"}")
        self.groupTreeWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.groupTreeWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.groupTreeWidget.setLineWidth(0)
        self.groupTreeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.groupTreeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.groupTreeWidget.setIndentation(0)
        self.groupTreeWidget.setRootIsDecorated(False)
        self.groupTreeWidget.setExpandsOnDoubleClick(False)
        self.groupTreeWidget.setObjectName("groupTreeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.groupTreeWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/res/arrow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap(":/res/arrow_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon3)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.groupTreeWidget)
        item_0.setIcon(0, icon3)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.groupTreeWidget.header().setVisible(False)
        self.groupVerticalLayout.addWidget(self.groupTreeWidget)
        self.tabWidget.addTab(self.tabGroup, "")
        self.tabHistory = QtWidgets.QWidget()
        self.tabHistory.setStyleSheet("")
        self.tabHistory.setObjectName("tabHistory")
        self.historyVerticalLayout = QtWidgets.QVBoxLayout(self.tabHistory)
        self.historyVerticalLayout.setSpacing(0)
        self.historyVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.historyVerticalLayout.setObjectName("historyVerticalLayout")
        self.historyTreeWidget = QtWidgets.QTreeWidget(self.tabHistory)
        self.historyTreeWidget.setStyleSheet("QListWidget#historyListWidget {\n"
"    background: rgba(255, 255, 255, 100);\n"
"}")
        self.historyTreeWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.historyTreeWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyTreeWidget.setLineWidth(0)
        self.historyTreeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.historyTreeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.historyTreeWidget.setIndentation(0)
        self.historyTreeWidget.setObjectName("historyTreeWidget")
        self.historyTreeWidget.headerItem().setText(0, "1")
        self.historyTreeWidget.header().setVisible(False)
        self.historyVerticalLayout.addWidget(self.historyTreeWidget)
        self.tabWidget.addTab(self.tabHistory, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(ucics)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ucics)

    def retranslateUi(self, ucics):
        _translate = QtCore.QCoreApplication.translate
        ucics.setWindowTitle(_translate("ucics", "UCICS"))
        self.nameEdit.setText(_translate("ucics", "ヽoo悾絔℅o。"))
        self.moodEdit.setPlaceholderText(_translate("ucics", "编辑个性签名"))
        self.searchEdit.setPlaceholderText(_translate("ucics", "搜索: 联系人"))
        self.groupTreeWidget.headerItem().setText(0, _translate("ucics", "1"))
        __sortingEnabled = self.groupTreeWidget.isSortingEnabled()
        self.groupTreeWidget.setSortingEnabled(False)
        self.groupTreeWidget.topLevelItem(0).setText(0, _translate("ucics", "111"))
        self.groupTreeWidget.topLevelItem(0).child(0).setText(0, _translate("ucics", "222"))
        self.groupTreeWidget.topLevelItem(1).setText(0, _translate("ucics", "222"))
        self.groupTreeWidget.topLevelItem(1).child(0).setText(0, _translate("ucics", "222"))
        self.groupTreeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tabGroup), _translate("ucics", "分组"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tabHistory), _translate("ucics", "历史"))
