# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(480, 390)
        MainWindow.setMinimumSize(QtCore.QSize(480, 390))
        MainWindow.setMaximumSize(QtCore.QSize(480, 390))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_Source = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Source.setGeometry(QtCore.QRect(100, 8, 371, 27))
        self.lineEdit_Source.setObjectName("lineEdit_Source")
        self.lineEdit_Destination = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Destination.setGeometry(QtCore.QRect(100, 48, 371, 27))
        self.lineEdit_Destination.setObjectName("lineEdit_Destination")
        self.pushButton_Destination = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Destination.setGeometry(QtCore.QRect(10, 48, 85, 27))
        self.pushButton_Destination.setObjectName("pushButton_Destination")
        self.label_X = QtWidgets.QLabel(self.centralwidget)
        self.label_X.setGeometry(QtCore.QRect(139, 139, 16, 21))
        self.label_X.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X.setObjectName("label_X")
        self.comboBox_Preset = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Preset.setGeometry(QtCore.QRect(70, 88, 401, 33))
        self.comboBox_Preset.setObjectName("comboBox_Preset")
        self.comboBox_Preset.addItem("")
        self.comboBox_Preset.addItem("")
        self.comboBox_Preset.addItem("")
        self.comboBox_Preset.addItem("")
        self.spinBox_Height = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_Height.setGeometry(QtCore.QRect(160, 138, 61, 27))
        self.spinBox_Height.setMinimum(1)
        self.spinBox_Height.setMaximum(9999)
        self.spinBox_Height.setObjectName("spinBox_Height")
        self.label_Preset = QtWidgets.QLabel(self.centralwidget)
        self.label_Preset.setGeometry(QtCore.QRect(10, 93, 54, 21))
        self.label_Preset.setObjectName("label_Preset")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(100, 180, 371, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_Start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Start.setGeometry(QtCore.QRect(10, 178, 85, 27))
        self.pushButton_Start.setObjectName("pushButton_Start")
        self.spinBox_Quality = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_Quality.setGeometry(QtCore.QRect(350, 138, 51, 27))
        self.spinBox_Quality.setMinimum(1)
        self.spinBox_Quality.setMaximum(100)
        self.spinBox_Quality.setObjectName("spinBox_Quality")
        self.label_Size = QtWidgets.QLabel(self.centralwidget)
        self.label_Size.setGeometry(QtCore.QRect(10, 140, 54, 21))
        self.label_Size.setObjectName("label_Size")
        self.spinBox_Width = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_Width.setGeometry(QtCore.QRect(70, 138, 61, 27))
        self.spinBox_Width.setMinimum(1)
        self.spinBox_Width.setMaximum(9999)
        self.spinBox_Width.setObjectName("spinBox_Width")
        self.pushButton_Source = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Source.setGeometry(QtCore.QRect(10, 8, 85, 27))
        self.pushButton_Source.setObjectName("pushButton_Source")
        self.plainTextEdit_Output = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_Output.setGeometry(QtCore.QRect(10, 218, 461, 121))
        self.plainTextEdit_Output.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_Output.setReadOnly(True)
        self.plainTextEdit_Output.setObjectName("plainTextEdit_Output")
        self.label_Quality = QtWidgets.QLabel(self.centralwidget)
        self.label_Quality.setGeometry(QtCore.QRect(240, 140, 101, 21))
        self.label_Quality.setObjectName("label_Quality")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 27))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Batch Image Resize"))
        self.pushButton_Destination.setText(_translate("MainWindow", "Результат"))
        self.label_X.setText(_translate("MainWindow", "Х"))
        self.comboBox_Preset.setItemText(0, _translate("MainWindow", "1280x720_90 - HD. Оптимальное качество фото."))
        self.comboBox_Preset.setItemText(1, _translate("MainWindow", "1920x1080_90 - FullHD. Оптимальное качество фото."))
        self.comboBox_Preset.setItemText(2, _translate("MainWindow", "2048x1152_90 - 2K UHD. Оптимальное качество фото."))
        self.comboBox_Preset.setItemText(3, _translate("MainWindow", "4096x2304_90 - 4K UHD. Оптимальное качество фото."))
        self.label_Preset.setText(_translate("MainWindow", "Пресет:"))
        self.pushButton_Start.setText(_translate("MainWindow", "Старт"))
        self.label_Size.setText(_translate("MainWindow", "Размер:"))
        self.pushButton_Source.setText(_translate("MainWindow", "Источник"))
        self.label_Quality.setText(_translate("MainWindow", "Качество (JPEG):"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Справка"))
        self.action.setText(_translate("MainWindow", "Выход"))
        self.action_2.setText(_translate("MainWindow", "О программе"))

