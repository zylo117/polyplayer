# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ctrl_panel.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.verticalLayout_2.addWidget(self.title)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.global_search = QtWidgets.QLineEdit(self.centralwidget)
        self.global_search.setText("")
        self.global_search.setMaxLength(32)
        self.global_search.setObjectName("global_search")
        self.horizontalLayout.addWidget(self.global_search)
        self.dl_source = QtWidgets.QComboBox(self.centralwidget)
        self.dl_source.setObjectName("dl_source")
        self.dl_source.addItem("")
        self.dl_source.addItem("")
        self.dl_source.addItem("")
        self.dl_source.addItem("")
        self.dl_source.addItem("")
        self.dl_source.addItem("")
        self.dl_source.addItem("")
        self.horizontalLayout.addWidget(self.dl_source)
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout.addWidget(self.pushButton_search)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout.addWidget(self.pushButton_add)
        self.pushButton_download = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_download.setObjectName("pushButton_download")
        self.horizontalLayout.addWidget(self.pushButton_download)
        self.pushButton_download_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_download_2.setObjectName("pushButton_download_2")
        self.horizontalLayout.addWidget(self.pushButton_download_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setTabletTracking(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_prev = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_prev.setObjectName("pushButton_prev")
        self.horizontalLayout_2.addWidget(self.pushButton_prev)
        self.pushButton_play = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_play.setObjectName("pushButton_play")
        self.horizontalLayout_2.addWidget(self.pushButton_play)
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout_2.addWidget(self.pushButton_next)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_current_play_time = QtWidgets.QLabel(self.centralwidget)
        self.label_current_play_time.setObjectName("label_current_play_time")
        self.horizontalLayout_2.addWidget(self.label_current_play_time)
        self.horizontalSlider_play_progress = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_play_progress.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_play_progress.setInvertedAppearance(False)
        self.horizontalSlider_play_progress.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_play_progress.setObjectName("horizontalSlider_play_progress")
        self.horizontalLayout_2.addWidget(self.horizontalSlider_play_progress)
        self.label_total_play_time = QtWidgets.QLabel(self.centralwidget)
        self.label_total_play_time.setObjectName("label_total_play_time")
        self.horizontalLayout_2.addWidget(self.label_total_play_time)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setProperty("value", 49)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "PolyPlayer"))
        self.global_search.setPlaceholderText(_translate("MainWindow", "I\'m feeling lucky..."))
        self.dl_source.setItemText(0, _translate("MainWindow", "all"))
        self.dl_source.setItemText(1, _translate("MainWindow", "netease"))
        self.dl_source.setItemText(2, _translate("MainWindow", "qqmusic"))
        self.dl_source.setItemText(3, _translate("MainWindow", "xiami"))
        self.dl_source.setItemText(4, _translate("MainWindow", "migu"))
        self.dl_source.setItemText(5, _translate("MainWindow", "baidu"))
        self.dl_source.setItemText(6, _translate("MainWindow", "kugou"))
        self.pushButton_search.setText(_translate("MainWindow", "Search"))
        self.pushButton_add.setText(_translate("MainWindow", "Add"))
        self.pushButton_download.setText(_translate("MainWindow", "Download"))
        self.pushButton_download_2.setText(_translate("MainWindow", "Remove"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Index"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Artist"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Album"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Duration"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Filesize"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Source"))
        self.pushButton_prev.setText(_translate("MainWindow", "Prev"))
        self.pushButton_play.setText(_translate("MainWindow", "Play"))
        self.pushButton_next.setText(_translate("MainWindow", "Next"))
        self.label_current_play_time.setText(_translate("MainWindow", "00:00"))
        self.label_total_play_time.setText(_translate("MainWindow", "03:00"))
        self.pushButton.setText(_translate("MainWindow", "Mute"))
        self.pushButton_2.setText(_translate("MainWindow", "Mode"))