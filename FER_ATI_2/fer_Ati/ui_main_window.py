# # -*- coding: utf-8 -*-

# ################################################################################
# ## Form generated from reading UI file 'main_windowEmrZUZ.ui'
# ##
# ## Created by: Qt User Interface Compiler version 5.15.2
# ##
# ## WARNING! All changes made in this file will be lost when recompiling UI file!
# ################################################################################

# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *

# from QGraphViz.QGraphViz import QGraphViz, QGraphVizManipulationMode
# from QGraphViz.DotParser import Graph, GraphType
# from QGraphViz.Engines import Dot

# from PyQt5.QtGui import QFontMetrics, QFont, QImage


# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         if not MainWindow.objectName():
#             MainWindow.setObjectName(u"MainWindow")
#         MainWindow.resize(831, 600)
#         self.centralwidget = QWidget(MainWindow)
#         self.centralwidget.setObjectName(u"centralwidget")
#         self.verticalLayout = QVBoxLayout(self.centralwidget)
#         self.verticalLayout.setObjectName(u"verticalLayout")
#         self.qgv = QGraphViz.QGraphViz(self.centralwidget)
#         self.qgv.setObjectName(u"qgv")
#         self.qgv.setStyleSheet(u"background-color:white;")

#         self.verticalLayout.addWidget(self.qgv)

#         self.horizontalLayout = QHBoxLayout()
#         self.horizontalLayout.setObjectName(u"horizontalLayout")
#         self.btnNew = QPushButton(self.centralwidget)
#         self.btnNew.setObjectName(u"btnNew")

#         self.horizontalLayout.addWidget(self.btnNew)

#         self.btnOpen = QPushButton(self.centralwidget)
#         self.btnOpen.setObjectName(u"btnOpen")

#         self.horizontalLayout.addWidget(self.btnOpen)

#         self.btnSave = QPushButton(self.centralwidget)
#         self.btnSave.setObjectName(u"btnSave")

#         self.horizontalLayout.addWidget(self.btnSave)

#         self.btnManip = QPushButton(self.centralwidget)
#         self.btnManip.setObjectName(u"btnManip")
#         self.btnManip.setCheckable(True)
#         self.btnManip.setChecked(True)

#         self.horizontalLayout.addWidget(self.btnManip)

#         self.btnAddNode = QPushButton(self.centralwidget)
#         self.btnAddNode.setObjectName(u"btnAddNode")

#         self.horizontalLayout.addWidget(self.btnAddNode)

#         self.btnRemNode = QPushButton(self.centralwidget)
#         self.btnRemNode.setObjectName(u"btnRemNode")
#         self.btnRemNode.setCheckable(True)

#         self.horizontalLayout.addWidget(self.btnRemNode)

#         self.btnAddEdge = QPushButton(self.centralwidget)
#         self.btnAddEdge.setObjectName(u"btnAddEdge")
#         self.btnAddEdge.setCheckable(True)

#         self.horizontalLayout.addWidget(self.btnAddEdge)

#         self.btnRemEdge = QPushButton(self.centralwidget)
#         self.btnRemEdge.setObjectName(u"btnRemEdge")
#         self.btnRemEdge.setCheckable(True)

#         self.horizontalLayout.addWidget(self.btnRemEdge)

#         self.btnAddSubGraph = QPushButton(self.centralwidget)
#         self.btnAddSubGraph.setObjectName(u"btnAddSubGraph")

#         self.horizontalLayout.addWidget(self.btnAddSubGraph)

#         self.btnRemSubGraph = QPushButton(self.centralwidget)
#         self.btnRemSubGraph.setObjectName(u"btnRemSubGraph")
#         self.btnRemSubGraph.setCheckable(True)

#         self.horizontalLayout.addWidget(self.btnRemSubGraph)


#         self.verticalLayout.addLayout(self.horizontalLayout)

#         MainWindow.setCentralWidget(self.centralwidget)

#         self.retranslateUi(MainWindow)

#         QMetaObject.connectSlotsByName(MainWindow)
#     # setupUi

#     def retranslateUi(self, MainWindow):
#         MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simple", None))
#         self.btnNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#         self.btnOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#         self.btnSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#         self.btnManip.setText(QCoreApplication.translate("MainWindow", u"Manipulate", None))
#         self.btnAddNode.setText(QCoreApplication.translate("MainWindow", u"Add Node", None))
#         self.btnRemNode.setText(QCoreApplication.translate("MainWindow", u"Rem Node", None))
#         self.btnAddEdge.setText(QCoreApplication.translate("MainWindow", u"Add Edge", None))
#         self.btnRemEdge.setText(QCoreApplication.translate("MainWindow", u"Rem Edge", None))
#         self.btnAddSubGraph.setText(QCoreApplication.translate("MainWindow", u"Add Subgraph", None))
#         self.btnRemSubGraph.setText(QCoreApplication.translate("MainWindow", u"Rem Subgraph", None))
#     # retranslateUi

