# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualistation_gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(997, 828)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.frame)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.dumaTab = QtWidgets.QWidget()
        self.dumaTab.setObjectName("dumaTab")
        self.tabWidget_2.addTab(self.dumaTab, "")
        self.standardPlotsTab = QtWidgets.QWidget()
        self.standardPlotsTab.setObjectName("standardPlotsTab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.standardPlotsTab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.standardPlotWidget = MplWidget(self.standardPlotsTab)
        self.standardPlotWidget.setObjectName("standardPlotWidget")
        self.horizontalLayout_5.addWidget(self.standardPlotWidget)
        self.frame_2 = QtWidgets.QFrame(self.standardPlotsTab)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.defaultHealthPushButton = QtWidgets.QPushButton(self.frame_2)
        self.defaultHealthPushButton.setObjectName("defaultHealthPushButton")
        self.verticalLayout_15.addWidget(self.defaultHealthPushButton)
        self.defaultShelterPushButton = QtWidgets.QPushButton(self.frame_2)
        self.defaultShelterPushButton.setObjectName("defaultShelterPushButton")
        self.verticalLayout_15.addWidget(self.defaultShelterPushButton)
        self.defaultFoodPushButton = QtWidgets.QPushButton(self.frame_2)
        self.defaultFoodPushButton.setObjectName("defaultFoodPushButton")
        self.verticalLayout_15.addWidget(self.defaultFoodPushButton)
        self.defaultPushButton1 = QtWidgets.QPushButton(self.frame_2)
        self.defaultPushButton1.setObjectName("defaultPushButton1")
        self.verticalLayout_15.addWidget(self.defaultPushButton1)
        self.defaultPushButton2 = QtWidgets.QPushButton(self.frame_2)
        self.defaultPushButton2.setObjectName("defaultPushButton2")
        self.verticalLayout_15.addWidget(self.defaultPushButton2)
        self.defaultPushButton3 = QtWidgets.QPushButton(self.frame_2)
        self.defaultPushButton3.setObjectName("defaultPushButton3")
        self.verticalLayout_15.addWidget(self.defaultPushButton3)
        self.defaultPushButton4 = QtWidgets.QPushButton(self.frame_2)
        self.defaultPushButton4.setObjectName("defaultPushButton4")
        self.verticalLayout_15.addWidget(self.defaultPushButton4)
        self.defaultPushButton5 = QtWidgets.QPushButton(self.frame_2)
        self.defaultPushButton5.setObjectName("defaultPushButton5")
        self.verticalLayout_15.addWidget(self.defaultPushButton5)
        self.defaultPushButton6 = QtWidgets.QPushButton(self.frame_2)
        self.defaultPushButton6.setObjectName("defaultPushButton6")
        self.verticalLayout_15.addWidget(self.defaultPushButton6)
        self.defaultPushButton7 = QtWidgets.QPushButton(self.frame_2)
        self.defaultPushButton7.setObjectName("defaultPushButton7")
        self.verticalLayout_15.addWidget(self.defaultPushButton7)
        self.exportAllPushButton = QtWidgets.QPushButton(self.frame_2)
        self.exportAllPushButton.setObjectName("exportAllPushButton")
        self.verticalLayout_15.addWidget(self.exportAllPushButton)
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.tabWidget_2.addTab(self.standardPlotsTab, "")
        self.customPlotTab = QtWidgets.QWidget()
        self.customPlotTab.setObjectName("customPlotTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.customPlotTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(self.customPlotTab)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.customPlotWidget = MplWidget(self.frame_5)
        self.customPlotWidget.setObjectName("customPlotWidget")
        self.verticalLayout_5.addWidget(self.customPlotWidget)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.minDay = QtWidgets.QLabel(self.frame_6)
        self.minDay.setObjectName("minDay")
        self.horizontalLayout_3.addWidget(self.minDay)
        self.horizontalSlider = QtWidgets.QSlider(self.frame_6)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider.setTickInterval(5)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_3.addWidget(self.horizontalSlider)
        self.maxDay = QtWidgets.QLabel(self.frame_6)
        self.maxDay.setObjectName("maxDay")
        self.horizontalLayout_3.addWidget(self.maxDay)
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setMinimumSize(QtCore.QSize(60, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setLineWidth(0)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.dayLabel = QtWidgets.QLabel(self.frame_7)
        self.dayLabel.setObjectName("dayLabel")
        self.verticalLayout_6.addWidget(self.dayLabel)
        self.daySpinBox = QtWidgets.QSpinBox(self.frame_7)
        self.daySpinBox.setEnabled(False)
        self.daySpinBox.setObjectName("daySpinBox")
        self.verticalLayout_6.addWidget(self.daySpinBox)
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.frame_5)
        self.frame_3 = QtWidgets.QFrame(self.customPlotTab)
        self.frame_3.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_3)
        self.tabWidget.setObjectName("tabWidget")
        self.plotTab = QtWidgets.QWidget()
        self.plotTab.setObjectName("plotTab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.plotTab)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gifButton = QtWidgets.QPushButton(self.plotTab)
        self.gifButton.setEnabled(False)
        self.gifButton.setObjectName("gifButton")
        self.verticalLayout_10.addWidget(self.gifButton)
        self.plotTypeGroup = QtWidgets.QGroupBox(self.plotTab)
        self.plotTypeGroup.setObjectName("plotTypeGroup")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.plotTypeGroup)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.plotTypeComboBox = QtWidgets.QComboBox(self.plotTypeGroup)
        self.plotTypeComboBox.setEnabled(False)
        self.plotTypeComboBox.setObjectName("plotTypeComboBox")
        self.verticalLayout_8.addWidget(self.plotTypeComboBox)
        self.label_11 = QtWidgets.QLabel(self.plotTypeGroup)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11)
        self.agentComboBox = QtWidgets.QComboBox(self.plotTypeGroup)
        self.agentComboBox.setEnabled(False)
        self.agentComboBox.setObjectName("agentComboBox")
        self.verticalLayout_8.addWidget(self.agentComboBox)
        self.addAgentPushButton = QtWidgets.QPushButton(self.plotTypeGroup)
        self.addAgentPushButton.setEnabled(False)
        self.addAgentPushButton.setObjectName("addAgentPushButton")
        self.verticalLayout_8.addWidget(self.addAgentPushButton)
        self.clearAgentsPushButton = QtWidgets.QPushButton(self.plotTypeGroup)
        self.clearAgentsPushButton.setEnabled(False)
        self.clearAgentsPushButton.setObjectName("clearAgentsPushButton")
        self.verticalLayout_8.addWidget(self.clearAgentsPushButton)
        self.label_7 = QtWidgets.QLabel(self.plotTypeGroup)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.colourComboBox = QtWidgets.QComboBox(self.plotTypeGroup)
        self.colourComboBox.setEnabled(False)
        self.colourComboBox.setObjectName("colourComboBox")
        self.verticalLayout_8.addWidget(self.colourComboBox)
        self.averageBox = QtWidgets.QGroupBox(self.plotTypeGroup)
        self.averageBox.setMinimumSize(QtCore.QSize(0, 100))
        self.averageBox.setObjectName("averageBox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.averageBox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.noneRadio = QtWidgets.QRadioButton(self.averageBox)
        self.noneRadio.setEnabled(False)
        self.noneRadio.setChecked(True)
        self.noneRadio.setObjectName("noneRadio")
        self.verticalLayout_9.addWidget(self.noneRadio)
        self.agentAverageRadio = QtWidgets.QRadioButton(self.averageBox)
        self.agentAverageRadio.setEnabled(False)
        self.agentAverageRadio.setObjectName("agentAverageRadio")
        self.verticalLayout_9.addWidget(self.agentAverageRadio)
        self.timeAverageRadio = QtWidgets.QRadioButton(self.averageBox)
        self.timeAverageRadio.setEnabled(False)
        self.timeAverageRadio.setObjectName("timeAverageRadio")
        self.verticalLayout_9.addWidget(self.timeAverageRadio)
        self.verticalLayout_8.addWidget(self.averageBox)
        self.verticalLayout_10.addWidget(self.plotTypeGroup)
        self.axesGroup = QtWidgets.QGroupBox(self.plotTab)
        self.axesGroup.setObjectName("axesGroup")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.axesGroup)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.axesGroup)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.xComboBox = QtWidgets.QComboBox(self.axesGroup)
        self.xComboBox.setEnabled(False)
        self.xComboBox.setObjectName("xComboBox")
        self.verticalLayout_4.addWidget(self.xComboBox)
        self.label_3 = QtWidgets.QLabel(self.axesGroup)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.yComboBox = QtWidgets.QComboBox(self.axesGroup)
        self.yComboBox.setEnabled(False)
        self.yComboBox.setObjectName("yComboBox")
        self.verticalLayout_4.addWidget(self.yComboBox)
        self.verticalLayout_10.addWidget(self.axesGroup)
        self.tabWidget.addTab(self.plotTab, "")
        self.filtersTab = QtWidgets.QWidget()
        self.filtersTab.setObjectName("filtersTab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.filtersTab)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_4 = QtWidgets.QLabel(self.filtersTab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_11.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.filtersTab)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_11.addWidget(self.comboBox)
        self.label_5 = QtWidgets.QLabel(self.filtersTab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_11.addWidget(self.label_5)
        self.frame_9 = QtWidgets.QFrame(self.filtersTab)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.filterNumSpinBox = QtWidgets.QSpinBox(self.frame_10)
        self.filterNumSpinBox.setEnabled(False)
        self.filterNumSpinBox.setObjectName("filterNumSpinBox")
        self.horizontalLayout_4.addWidget(self.filterNumSpinBox)
        self.filterComboBox = QtWidgets.QComboBox(self.frame_10)
        self.filterComboBox.setEnabled(False)
        self.filterComboBox.setObjectName("filterComboBox")
        self.horizontalLayout_4.addWidget(self.filterComboBox)
        self.verticalLayout_12.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_9)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.withRadioButton = QtWidgets.QRadioButton(self.frame_11)
        self.withRadioButton.setChecked(True)
        self.withRadioButton.setObjectName("withRadioButton")
        self.verticalLayout_13.addWidget(self.withRadioButton)
        self.withoutRadioButton = QtWidgets.QRadioButton(self.frame_11)
        self.withoutRadioButton.setObjectName("withoutRadioButton")
        self.verticalLayout_13.addWidget(self.withoutRadioButton)
        self.verticalLayout_12.addWidget(self.frame_11)
        self.verticalLayout_11.addWidget(self.frame_9)
        self.addFilterPushButton = QtWidgets.QPushButton(self.filtersTab)
        self.addFilterPushButton.setObjectName("addFilterPushButton")
        self.verticalLayout_11.addWidget(self.addFilterPushButton)
        self.clearFiltersPushButton = QtWidgets.QPushButton(self.filtersTab)
        self.clearFiltersPushButton.setObjectName("clearFiltersPushButton")
        self.verticalLayout_11.addWidget(self.clearFiltersPushButton)
        self.label_6 = QtWidgets.QLabel(self.filtersTab)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_11.addWidget(self.label_6)
        self.filterBrowser = QtWidgets.QTextBrowser(self.filtersTab)
        self.filterBrowser.setObjectName("filterBrowser")
        self.verticalLayout_11.addWidget(self.filterBrowser)
        self.tabWidget.addTab(self.filtersTab, "")
        self.statsTab = QtWidgets.QWidget()
        self.statsTab.setObjectName("statsTab")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.statsTab)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_12 = QtWidgets.QLabel(self.statsTab)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_14.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.statsTab)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_14.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.statsTab)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_14.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.statsTab)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_14.addWidget(self.label_15)
        self.label_8 = QtWidgets.QLabel(self.statsTab)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_14.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.statsTab)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_14.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.statsTab)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_14.addWidget(self.label_10)
        self.ruleBrowser = QtWidgets.QTextBrowser(self.statsTab)
        self.ruleBrowser.setObjectName("ruleBrowser")
        self.verticalLayout_14.addWidget(self.ruleBrowser)
        self.tabWidget.addTab(self.statsTab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout.addWidget(self.frame_3)
        self.tabWidget_2.addTab(self.customPlotTab, "")
        self.verticalLayout_2.addWidget(self.tabWidget_2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 997, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(MainWindow.browseSlot)
        self.lineEdit.returnPressed.connect(MainWindow.returnPressedSlot)
        self.addAgentPushButton.clicked.connect(MainWindow.addAgentSlot)
        self.noneRadio.clicked.connect(MainWindow.noneAverageSelected)
        self.daySpinBox.valueChanged['int'].connect(self.horizontalSlider.setValue)
        self.gifButton.clicked.connect(MainWindow.exportGifSlot)
        self.horizontalSlider.valueChanged['int'].connect(self.daySpinBox.setValue)
        self.agentAverageRadio.clicked.connect(MainWindow.agentAverageSelected)
        self.timeAverageRadio.clicked.connect(MainWindow.timeAverageSelected)
        self.plotTypeComboBox.activated['QString'].connect(MainWindow.plotTypeSlot)
        self.xComboBox.activated['QString'].connect(MainWindow.xAxisSlot)
        self.yComboBox.activated['QString'].connect(MainWindow.yAxisSlot)
        self.addFilterPushButton.clicked.connect(MainWindow.addFilterSlot)
        self.clearFiltersPushButton.clicked.connect(MainWindow.removeAllFiltersSlot)
        self.comboBox.activated['QString'].connect(MainWindow.filterParameterSelectedSlot)
        self.colourComboBox.activated['QString'].connect(MainWindow.plotColourSlot)
        self.exportAllPushButton.clicked.connect(MainWindow.exportAllSlot)
        self.defaultHealthPushButton.clicked.connect(MainWindow.defaultHealthSlot)
        self.defaultShelterPushButton.clicked.connect(MainWindow.defaultShelterSlot)
        self.defaultFoodPushButton.clicked.connect(MainWindow.defaultFoodSlot)
        self.defaultPushButton1.clicked.connect(MainWindow.defaultPlaceholderSlot)
        self.defaultPushButton2.clicked.connect(MainWindow.defaultPlaceholderSlot)
        self.defaultPushButton3.clicked.connect(MainWindow.defaultPlaceholderSlot)
        self.defaultPushButton4.clicked.connect(MainWindow.defaultPlaceholderSlot)
        self.defaultPushButton5.clicked.connect(MainWindow.defaultPlaceholderSlot)
        self.defaultPushButton6.clicked.connect(MainWindow.defaultPlaceholderSlot)
        self.defaultPushButton7.clicked.connect(MainWindow.defaultPlaceholderSlot)
        self.horizontalSlider.valueChanged['int'].connect(MainWindow.dayChangedSlot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "File Name"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.dumaTab), _translate("MainWindow", "Duma"))
        self.defaultHealthPushButton.setText(_translate("MainWindow", "Average Health"))
        self.defaultShelterPushButton.setText(_translate("MainWindow", "Average Shelter"))
        self.defaultFoodPushButton.setText(_translate("MainWindow", "Food Gathered"))
        self.defaultPushButton1.setText(_translate("MainWindow", "PushButton"))
        self.defaultPushButton2.setText(_translate("MainWindow", "PushButton"))
        self.defaultPushButton3.setText(_translate("MainWindow", "PushButton"))
        self.defaultPushButton4.setText(_translate("MainWindow", "PushButton"))
        self.defaultPushButton5.setText(_translate("MainWindow", "PushButton"))
        self.defaultPushButton6.setText(_translate("MainWindow", "PushButton"))
        self.defaultPushButton7.setText(_translate("MainWindow", "PushButton"))
        self.exportAllPushButton.setText(_translate("MainWindow", "Export all"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.standardPlotsTab), _translate("MainWindow", "Standard Plots"))
        self.minDay.setText(_translate("MainWindow", "0"))
        self.maxDay.setText(_translate("MainWindow", "0"))
        self.dayLabel.setText(_translate("MainWindow", "DAY"))
        self.gifButton.setText(_translate("MainWindow", "Export GIF"))
        self.plotTypeGroup.setTitle(_translate("MainWindow", "Plot Type"))
        self.label_11.setText(_translate("MainWindow", "Select agent"))
        self.addAgentPushButton.setText(_translate("MainWindow", "Add agent to plot"))
        self.clearAgentsPushButton.setText(_translate("MainWindow", "Clear all agents"))
        self.label_7.setText(_translate("MainWindow", "Colour by..."))
        self.averageBox.setTitle(_translate("MainWindow", "Average"))
        self.noneRadio.setText(_translate("MainWindow", "None"))
        self.agentAverageRadio.setText(_translate("MainWindow", "Agent Average"))
        self.timeAverageRadio.setText(_translate("MainWindow", "Time Average"))
        self.axesGroup.setTitle(_translate("MainWindow", "Axes"))
        self.label_2.setText(_translate("MainWindow", "x parameter"))
        self.label_3.setText(_translate("MainWindow", "y parameter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plotTab), _translate("MainWindow", "Plot"))
        self.label_4.setText(_translate("MainWindow", "Parameter"))
        self.label_5.setText(_translate("MainWindow", "Filter by"))
        self.withRadioButton.setText(_translate("MainWindow", "With"))
        self.withoutRadioButton.setText(_translate("MainWindow", "Without"))
        self.addFilterPushButton.setText(_translate("MainWindow", "Add filter"))
        self.clearFiltersPushButton.setText(_translate("MainWindow", "Clear all filters"))
        self.label_6.setText(_translate("MainWindow", "Active filters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.filtersTab), _translate("MainWindow", "Filters"))
        self.label_12.setText(_translate("MainWindow", "Duma chair"))
        self.label_13.setText(_translate("MainWindow", "N/A"))
        self.label_14.setText(_translate("MainWindow", "Number of dead agents"))
        self.label_15.setText(_translate("MainWindow", "N/A"))
        self.label_8.setText(_translate("MainWindow", "Mean/mode"))
        self.label_9.setText(_translate("MainWindow", "N/A"))
        self.label_10.setText(_translate("MainWindow", "Current ruleset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.statsTab), _translate("MainWindow", "Stats"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.customPlotTab), _translate("MainWindow", "Custom Plot"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
from mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
