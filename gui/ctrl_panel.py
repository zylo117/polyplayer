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
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.horizontalLayout_3.addWidget(self.title)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.global_search = QtWidgets.QLineEdit(self.centralwidget)
        self.global_search.setText("")
        self.global_search.setMaxLength(32)
        self.global_search.setDragEnabled(True)
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
        self.horizontalLayout.addWidget(self.dl_source)
        self.pushButton_download = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_download.setObjectName("pushButton_download")
        self.horizontalLayout.addWidget(self.pushButton_download)
        self.pushButton_minimize = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minimize.setObjectName("pushButton_minimize")
        self.horizontalLayout.addWidget(self.pushButton_minimize)
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout.addWidget(self.pushButton_exit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.playlist = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.playlist.setFont(font)
        self.playlist.setTabletTracking(True)
        self.playlist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.playlist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.playlist.setShowGrid(True)
        self.playlist.setObjectName("playlist")
        self.playlist.setColumnCount(8)
        self.playlist.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.playlist.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.playlist.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.playlist.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.playlist.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.playlist.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.playlist.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.playlist.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.playlist.setHorizontalHeaderItem(7, item)
        self.playlist.horizontalHeader().setVisible(True)
        self.playlist.horizontalHeader().setCascadingSectionResizes(True)
        self.playlist.horizontalHeader().setDefaultSectionSize(80)
        self.playlist.horizontalHeader().setHighlightSections(True)
        self.playlist.horizontalHeader().setMinimumSectionSize(36)
        self.playlist.horizontalHeader().setSortIndicatorShown(True)
        self.playlist.horizontalHeader().setStretchLastSection(True)
        self.playlist.verticalHeader().setVisible(True)
        self.playlist.verticalHeader().setCascadingSectionResizes(True)
        self.playlist.verticalHeader().setDefaultSectionSize(30)
        self.playlist.verticalHeader().setSortIndicatorShown(False)
        self.playlist.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.playlist)
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_current_play_time = QtWidgets.QLabel(self.centralwidget)
        self.label_current_play_time.setObjectName("label_current_play_time")
        self.horizontalLayout_2.addWidget(self.label_current_play_time)
        self.horizontalSlider_current_play_time_slider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_current_play_time_slider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_current_play_time_slider.setInvertedAppearance(False)
        self.horizontalSlider_current_play_time_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_current_play_time_slider.setObjectName("horizontalSlider_current_play_time_slider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider_current_play_time_slider)
        self.label_total_play_time = QtWidgets.QLabel(self.centralwidget)
        self.label_total_play_time.setObjectName("label_total_play_time")
        self.horizontalLayout_2.addWidget(self.label_total_play_time)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_mute = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mute.setObjectName("pushButton_mute")
        self.horizontalLayout_2.addWidget(self.pushButton_mute)
        self.horizontalSlider_volume = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_volume.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_volume.setSizePolicy(sizePolicy)
        self.horizontalSlider_volume.setProperty("value", 49)
        self.horizontalSlider_volume.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_volume.setObjectName("horizontalSlider_volume")
        self.horizontalLayout_2.addWidget(self.horizontalSlider_volume)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButton_playmode = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_playmode.setObjectName("pushButton_playmode")
        self.horizontalLayout_2.addWidget(self.pushButton_playmode)
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
        self.dl_source.setItemText(2, _translate("MainWindow", "qq"))
        self.dl_source.setItemText(3, _translate("MainWindow", "migu"))
        self.dl_source.setItemText(4, _translate("MainWindow", "baidu"))
        self.dl_source.setItemText(5, _translate("MainWindow", "kugou"))
        self.pushButton_download.setText(_translate("MainWindow", "↓"))
        self.pushButton_minimize.setText(_translate("MainWindow", "-"))
        self.pushButton_exit.setText(_translate("MainWindow", "×"))
        self.playlist.setSortingEnabled(True)
        item = self.playlist.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "❤"))
        item = self.playlist.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "↓"))
        item = self.playlist.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Title"))
        item = self.playlist.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Artist"))
        item = self.playlist.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Album"))
        item = self.playlist.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Duration"))
        item = self.playlist.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Filesize"))
        item = self.playlist.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Source"))
        self.pushButton_prev.setText(_translate("MainWindow", "Prev"))
        self.pushButton_play.setText(_translate("MainWindow", "Play"))
        self.pushButton_next.setText(_translate("MainWindow", "Next"))
        self.label_current_play_time.setText(_translate("MainWindow", "00:00"))
        self.label_total_play_time.setText(_translate("MainWindow", "03:00"))
        self.pushButton_mute.setText(_translate("MainWindow", "Mute"))
        self.pushButton_playmode.setText(_translate("MainWindow", "Mode"))
