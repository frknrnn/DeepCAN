# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainNYMolx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(779, 512)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(49, 51, 50);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_titleBar = QFrame(self.frame)
        self.frame_titleBar.setObjectName(u"frame_titleBar")
        self.frame_titleBar.setMinimumSize(QSize(0, 40))
        self.frame_titleBar.setMaximumSize(QSize(16777215, 40))
        self.frame_titleBar.setFrameShape(QFrame.NoFrame)
        self.frame_titleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_titleBar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_titleBar)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_total = QLabel(self.frame_4)
        self.label_total.setObjectName(u"label_total")
        self.label_total.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.label_total)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_titleBar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_titleBar)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_titleBar)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exit = QPushButton(self.frame_7)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setMinimumSize(QSize(50, 30))
        self.pushButton_exit.setMaximumSize(QSize(50, 30))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255,150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_exit)


        self.horizontalLayout_2.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_titleBar)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgba(0, 122, 204,150);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 100))
        self.frame_9.setMaximumSize(QSize(16777215, 100))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.frame_9)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(26)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(10)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel{\n"
"\n"
"border-radius:40px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"	font: 87 26pt \"Segoe UI\";\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setSpacing(40)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_12)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(130, 0))
        self.label_2.setMaximumSize(QSize(150, 16777215))
        self.label_2.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.lineEdit_image = QLineEdit(self.frame_12)
        self.lineEdit_image.setObjectName(u"lineEdit_image")
        self.lineEdit_image.setMinimumSize(QSize(300, 0))
        self.lineEdit_image.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_image.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.lineEdit_image)

        self.pushButton_selectImage = QPushButton(self.frame_12)
        self.pushButton_selectImage.setObjectName(u"pushButton_selectImage")
        self.pushButton_selectImage.setMinimumSize(QSize(120, 25))
        self.pushButton_selectImage.setMaximumSize(QSize(120, 25))
        self.pushButton_selectImage.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_selectImage)


        self.verticalLayout_7.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_5.setSpacing(40)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(130, 0))
        self.label_3.setMaximumSize(QSize(150, 16777215))
        self.label_3.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEdit_outputFolder = QLineEdit(self.frame_13)
        self.lineEdit_outputFolder.setObjectName(u"lineEdit_outputFolder")
        self.lineEdit_outputFolder.setMinimumSize(QSize(300, 0))
        self.lineEdit_outputFolder.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_outputFolder.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.lineEdit_outputFolder)

        self.pushButton_selectOutputFolder = QPushButton(self.frame_13)
        self.pushButton_selectOutputFolder.setObjectName(u"pushButton_selectOutputFolder")
        self.pushButton_selectOutputFolder.setMinimumSize(QSize(120, 25))
        self.pushButton_selectOutputFolder.setMaximumSize(QSize(120, 25))
        self.pushButton_selectOutputFolder.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_selectOutputFolder)


        self.verticalLayout_7.addWidget(self.frame_13)

        self.frame_25 = QFrame(self.frame_10)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_10.setSpacing(40)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_25)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(130, 0))
        self.label_4.setMaximumSize(QSize(150, 16777215))
        self.label_4.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.label_4)

        self.lineEdit_modelFolder = QLineEdit(self.frame_25)
        self.lineEdit_modelFolder.setObjectName(u"lineEdit_modelFolder")
        self.lineEdit_modelFolder.setMinimumSize(QSize(300, 0))
        self.lineEdit_modelFolder.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_modelFolder.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.lineEdit_modelFolder)

        self.pushButton_selectModelFolder = QPushButton(self.frame_25)
        self.pushButton_selectModelFolder.setObjectName(u"pushButton_selectModelFolder")
        self.pushButton_selectModelFolder.setMinimumSize(QSize(120, 25))
        self.pushButton_selectModelFolder.setMaximumSize(QSize(120, 25))
        self.pushButton_selectModelFolder.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_selectModelFolder)


        self.verticalLayout_7.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_10)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_11.setSpacing(40)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_26)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(130, 0))
        self.label_5.setMaximumSize(QSize(150, 16777215))
        self.label_5.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.comboBox = QComboBox(self.frame_26)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(100, 0))
        self.comboBox.setMaximumSize(QSize(100, 16777215))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"}\n"
"QComboBox QAbstractItemView{border: 0px;color:white}")

        self.horizontalLayout_11.addWidget(self.comboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addWidget(self.frame_26)


        self.verticalLayout_4.addWidget(self.frame_10, 0, Qt.AlignHCenter)

        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 100))
        self.frame_11.setMaximumSize(QSize(16777215, 100))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_start = QPushButton(self.frame_11)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(120, 35))
        self.pushButton_start.setMaximumSize(QSize(120, 35))
        self.pushButton_start.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton_start)


        self.verticalLayout_4.addWidget(self.frame_11, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.page_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(200, 0))
        self.frame_15.setMaximumSize(QSize(200, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_20 = QFrame(self.frame_15)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_20)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_std = QLabel(self.frame_20)
        self.label_std.setObjectName(u"label_std")
        self.label_std.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(85, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_std)

        self.label_average = QLabel(self.frame_20)
        self.label_average.setObjectName(u"label_average")
        self.label_average.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(85, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_average)


        self.verticalLayout_10.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_15)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 250))
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_21)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_totalCell = QLabel(self.frame_21)
        self.label_totalCell.setObjectName(u"label_totalCell")
        self.label_totalCell.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.label_totalCell)

        self.label_liveCell = QLabel(self.frame_21)
        self.label_liveCell.setObjectName(u"label_liveCell")
        self.label_liveCell.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(0, 255, 0);")

        self.verticalLayout_13.addWidget(self.label_liveCell)

        self.label_deadCell = QLabel(self.frame_21)
        self.label_deadCell.setObjectName(u"label_deadCell")
        self.label_deadCell.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 0, 0);")

        self.verticalLayout_13.addWidget(self.label_deadCell)

        self.label_viability = QLabel(self.frame_21)
        self.label_viability.setObjectName(u"label_viability")
        self.label_viability.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 0);")

        self.verticalLayout_13.addWidget(self.label_viability)


        self.verticalLayout_10.addWidget(self.frame_21)


        self.horizontalLayout_6.addWidget(self.frame_15)

        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(350, 0))
        self.frame_17.setMaximumSize(QSize(350, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_17)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(350, 350))
        self.frame_18.setMaximumSize(QSize(350, 350))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pictureBox = QLabel(self.frame_18)
        self.pictureBox.setObjectName(u"pictureBox")
        self.pictureBox.setMinimumSize(QSize(350, 350))
        self.pictureBox.setMaximumSize(QSize(350, 350))

        self.horizontalLayout_7.addWidget(self.pictureBox)


        self.verticalLayout_9.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_live = QPushButton(self.frame_19)
        self.pushButton_live.setObjectName(u"pushButton_live")
        self.pushButton_live.setMinimumSize(QSize(75, 35))
        self.pushButton_live.setMaximumSize(QSize(75, 35))
        self.pushButton_live.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 255, 0, 100);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButton_live)

        self.pushButton_dead = QPushButton(self.frame_19)
        self.pushButton_dead.setObjectName(u"pushButton_dead")
        self.pushButton_dead.setMinimumSize(QSize(75, 35))
        self.pushButton_dead.setMaximumSize(QSize(75, 35))
        self.pushButton_dead.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(255, 0, 0, 100);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButton_dead)

        self.pushButton_null = QPushButton(self.frame_19)
        self.pushButton_null.setObjectName(u"pushButton_null")
        self.pushButton_null.setMinimumSize(QSize(75, 35))
        self.pushButton_null.setMaximumSize(QSize(75, 35))
        self.pushButton_null.setToolTipDuration(-1)
        self.pushButton_null.setStyleSheet(u"QPushButton{\n"
"\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButton_null)


        self.verticalLayout_9.addWidget(self.frame_19)


        self.horizontalLayout_6.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_16)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_16)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 150))
        self.frame_22.setMaximumSize(QSize(16777215, 150))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_22)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_liveCell_2 = QLabel(self.frame_22)
        self.label_liveCell_2.setObjectName(u"label_liveCell_2")
        self.label_liveCell_2.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(0, 255, 0);")

        self.verticalLayout_16.addWidget(self.label_liveCell_2)

        self.listWidget_Live = QListWidget(self.frame_22)
        self.listWidget_Live.setObjectName(u"listWidget_Live")
        self.listWidget_Live.setStyleSheet(u"QListWidget{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
" QScrollBar:vertical\n"
" {\n"
"	background-color: rgb(49, 51, 50);\n"
"\n"
"     width: 15px;\n"
"\n"
"     margin: 15px 3px 15px 3px;\n"
"\n"
"     border: 1px transparent #2A2929;\n"
"\n"
"     border-radius: 4px;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::handle:vertical\n"
"\n"
" {\n"
"\n"
"     background-color: white;         /* #605F5F; */\n"
"\n"
"     min-height: 5px;\n"
"\n"
"     border-radius: 4px;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::sub-line:vertical\n"
"\n"
" {\n"
"\n"
"     margin: 3px 0px 3px 0px;\n"
"\n"
"     border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: top;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::add-line:vertical\n"
"\n"
" {\n"
"\n"
"     margin: 3px 0px 3px 0px;\n"
"\n"
"     border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width:"
                        " 10px;\n"
"\n"
"     subcontrol-position: bottom;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"\n"
" {\n"
"\n"
"\n"
"\n"
"     border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: top;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"\n"
" {\n"
"\n"
"     border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: bottom;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"\n"
" {\n"
"\n"
"     background: none;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"\n"
" {\n"
"\n"
"     background: none;\n"
""
                        "\n"
" }")

        self.verticalLayout_16.addWidget(self.listWidget_Live)


        self.verticalLayout_11.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_16)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 150))
        self.frame_23.setMaximumSize(QSize(16777215, 150))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_23)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_deadCell_2 = QLabel(self.frame_23)
        self.label_deadCell_2.setObjectName(u"label_deadCell_2")
        self.label_deadCell_2.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 0, 0);")

        self.verticalLayout_17.addWidget(self.label_deadCell_2)

        self.listWidget_dead = QListWidget(self.frame_23)
        self.listWidget_dead.setObjectName(u"listWidget_dead")
        self.listWidget_dead.setStyleSheet(u"QListWidget{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
" QScrollBar:vertical\n"
" {\n"
"	background-color: rgb(49, 51, 50);\n"
"\n"
"     width: 15px;\n"
"\n"
"     margin: 15px 3px 15px 3px;\n"
"\n"
"     border: 1px transparent #2A2929;\n"
"\n"
"     border-radius: 4px;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::handle:vertical\n"
"\n"
" {\n"
"\n"
"     background-color: white;         /* #605F5F; */\n"
"\n"
"     min-height: 5px;\n"
"\n"
"     border-radius: 4px;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::sub-line:vertical\n"
"\n"
" {\n"
"\n"
"     margin: 3px 0px 3px 0px;\n"
"\n"
"     border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: top;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::add-line:vertical\n"
"\n"
" {\n"
"\n"
"     margin: 3px 0px 3px 0px;\n"
"\n"
"     border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width:"
                        " 10px;\n"
"\n"
"     subcontrol-position: bottom;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"\n"
" {\n"
"\n"
"\n"
"\n"
"     border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: top;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"\n"
" {\n"
"\n"
"     border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: bottom;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"\n"
" {\n"
"\n"
"     background: none;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"\n"
" {\n"
"\n"
"     background: none;\n"
""
                        "\n"
" }")
        self.listWidget_dead.setFrameShape(QFrame.StyledPanel)

        self.verticalLayout_17.addWidget(self.listWidget_dead)


        self.verticalLayout_11.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_16)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 150))
        self.frame_24.setMaximumSize(QSize(16777215, 150))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_24)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pushButton_save = QPushButton(self.frame_24)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(120, 35))
        self.pushButton_save.setMaximumSize(QSize(120, 35))
        self.pushButton_save.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.verticalLayout_12.addWidget(self.pushButton_save)

        self.pushButton_new = QPushButton(self.frame_24)
        self.pushButton_new.setObjectName(u"pushButton_new")
        self.pushButton_new.setMinimumSize(QSize(120, 35))
        self.pushButton_new.setMaximumSize(QSize(120, 35))
        self.pushButton_new.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.verticalLayout_12.addWidget(self.pushButton_new)


        self.verticalLayout_11.addWidget(self.frame_24, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.frame_16)


        self.verticalLayout_8.addWidget(self.frame_14)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_15 = QVBoxLayout(self.page_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_2 = QFrame(self.page_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_total.setText(QCoreApplication.translate("MainWindow", u"0 / 300", None))
        self.pushButton_exit.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"DeepCAN Labeling APP", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cell Image", None))
        self.pushButton_selectImage.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Output Folder", None))
        self.pushButton_selectOutputFolder.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.pushButton_selectModelFolder.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"30", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"40", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"50", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"60", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"70", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"80", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"90", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"100", None))

        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_std.setText(QCoreApplication.translate("MainWindow", u"Std : ", None))
        self.label_average.setText(QCoreApplication.translate("MainWindow", u"Average : ", None))
        self.label_totalCell.setText(QCoreApplication.translate("MainWindow", u"Total: ", None))
        self.label_liveCell.setText(QCoreApplication.translate("MainWindow", u"Live : ", None))
        self.label_deadCell.setText(QCoreApplication.translate("MainWindow", u"Dead : ", None))
        self.label_viability.setText(QCoreApplication.translate("MainWindow", u"Viability : ", None))
        self.pictureBox.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_live.setToolTip(QCoreApplication.translate("MainWindow", u"Key: A", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_live.setText(QCoreApplication.translate("MainWindow", u"Live", None))
#if QT_CONFIG(tooltip)
        self.pushButton_dead.setToolTip(QCoreApplication.translate("MainWindow", u"Key : S", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_dead.setText(QCoreApplication.translate("MainWindow", u"Dead", None))
#if QT_CONFIG(tooltip)
        self.pushButton_null.setToolTip(QCoreApplication.translate("MainWindow", u"Key : D", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_null.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.label_liveCell_2.setText(QCoreApplication.translate("MainWindow", u"Live : ", None))
        self.label_deadCell_2.setText(QCoreApplication.translate("MainWindow", u"Dead : ", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.pushButton_new.setText(QCoreApplication.translate("MainWindow", u"NEW", None))
    # retranslateUi

