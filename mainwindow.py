# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v1_7mainwindow.ui'
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
        MainWindow.resize(480, 640)
        self.actioncreate = QAction(MainWindow)
        self.actioncreate.setObjectName(u"actioncreate")
        self.actionbrowse = QAction(MainWindow)
        self.actionbrowse.setObjectName(u"actionbrowse")
        self.actionsettings = QAction(MainWindow)
        self.actionsettings.setObjectName(u"actionsettings")
        self.actioncollision = QAction(MainWindow)
        self.actioncollision.setObjectName(u"actioncollision")
        self.actionoptions = QAction(MainWindow)
        self.actionoptions.setObjectName(u"actionoptions")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.displaybutton = QPushButton(self.centralwidget)
        self.displaybutton.setObjectName(u"displaybutton")
        self.displaybutton.setGeometry(QRect(330, 520, 113, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 22))
        self.menuball = QMenu(self.menubar)
        self.menuball.setObjectName(u"menuball")
        self.menuother_options = QMenu(self.menuball)
        self.menuother_options.setObjectName(u"menuother_options")
        self.menufloor = QMenu(self.menubar)
        self.menufloor.setObjectName(u"menufloor")
        self.menugraph = QMenu(self.menubar)
        self.menugraph.setObjectName(u"menugraph")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuball.menuAction())
        self.menubar.addAction(self.menufloor.menuAction())
        self.menubar.addAction(self.menugraph.menuAction())
        self.menuball.addAction(self.actioncreate)
        self.menuball.addAction(self.actionbrowse)
        self.menuball.addAction(self.menuother_options.menuAction())
        self.menuother_options.addAction(self.actioncollision)
        self.menufloor.addAction(self.actionsettings)
        self.menugraph.addAction(self.actionoptions)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actioncreate.setText(QCoreApplication.translate("MainWindow", u"create", None))
        self.actionbrowse.setText(QCoreApplication.translate("MainWindow", u"browse", None))
        self.actionsettings.setText(QCoreApplication.translate("MainWindow", u"settings", None))
        self.actioncollision.setText(QCoreApplication.translate("MainWindow", u"collision", None))
        self.actionoptions.setText(QCoreApplication.translate("MainWindow", u"options", None))
        self.displaybutton.setText(QCoreApplication.translate("MainWindow", u"display", None))
        self.menuball.setTitle(QCoreApplication.translate("MainWindow", u"ball", None))
        self.menuother_options.setTitle(QCoreApplication.translate("MainWindow", u"other options", None))
        self.menufloor.setTitle(QCoreApplication.translate("MainWindow", u"floor", None))
        self.menugraph.setTitle(QCoreApplication.translate("MainWindow", u"graph", None))
    # retranslateUi

