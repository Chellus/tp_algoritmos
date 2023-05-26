# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QHBoxLayout, QVBoxLayout, QSpacerItem
from PyQt5.QtWidgets import QApplication, QWidget, QSizePolicy
from PyQt5.QtGui import QCursor, QIcon, QFont
from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication, Qt, QSize
from PyQt5.QtCore import QMetaObject
from PyQt5 import QtWidgets, uic

class Ui_CentralWidget(object):
    def setupUi(self, CentralWidget):
        if not CentralWidget.objectName():
            CentralWidget.setObjectName(u"CentralWidget")
        CentralWidget.resize(733, 480)
        CentralWidget.setStyleSheet(u"#header,#main_body{\n"
"background-color:#27263c;\n"
"}\n"
"#CentralWidget{\n"
"background-color:#000;\n"
"}\n"
"QPushButton{\n"
"	text-align:left;\n"
"}")
        self.verticalLayout = QVBoxLayout(CentralWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(CentralWidget)
        self.header.setObjectName(u"header")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"#label{\n"
"color:white;\n"
"}")

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.main_body = QWidget(CentralWidget)
        self.main_body.setObjectName(u"main_body")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.main_body)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftmenu = QWidget(self.main_body)
        self.leftmenu.setObjectName(u"leftmenu")
        self.leftmenu.setMinimumSize(QSize(200, 0))
        self.verticalLayout_3 = QVBoxLayout(self.leftmenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.leftmenu)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.INICIO = QPushButton(self.frame_3)
        self.INICIO.setObjectName(u"INICIO")
        self.INICIO.setCursor(QCursor(Qt.PointingHandCursor))
        self.INICIO.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_5.addWidget(self.INICIO)
        #este es el boton para crear organigrama
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_5.addWidget(self.pushButton)

        self.INFORMES = QPushButton(self.frame_3)
        self.INFORMES.setObjectName(u"INFORMES")
        self.INFORMES.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.INFORMES)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.pushButton_9 = QPushButton(self.frame_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame_4)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.pushButton_10)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.leftmenu)

        self.mainbodycontent = QWidget(self.main_body)
        self.mainbodycontent.setObjectName(u"mainbodycontent")
        self.mainbodycontent.setMinimumSize(QSize(400, 400))
        self.verticalLayout_2 = QVBoxLayout(self.mainbodycontent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.mainbodycontent)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.mainbodycontent)

        self.rightmenu = QWidget(self.main_body)
        self.rightmenu.setObjectName(u"rightmenu")

        self.horizontalLayout_2.addWidget(self.rightmenu)


        self.verticalLayout.addWidget(self.main_body)


        self.retranslateUi(CentralWidget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CentralWidget)
    # setupUi

    def retranslateUi(self, CentralWidget):
        CentralWidget.setWindowTitle(QCoreApplication.translate("CentralWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("CentralWidget", u"ORGANIFILE", None))
        self.INICIO.setText(QCoreApplication.translate("CentralWidget", u"INICIO", None))
        self.pushButton.setText(QCoreApplication.translate("CentralWidget", u"CREAR ORGANIGRAMA", None))
        self.INFORMES.setText(QCoreApplication.translate("CentralWidget", u"ABRIR ORGANIGRAMA", None))
        self.pushButton_9.setText(QCoreApplication.translate("CentralWidget", u"AYUDA", None))
        self.pushButton_10.setText(QCoreApplication.translate("CentralWidget", u"SOBRE NOSOTROS", None))
    # retranslateUi
   