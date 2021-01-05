# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v1_4mainwindow.ui'
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.displaybutton = QPushButton(self.centralwidget)
        self.displaybutton.setObjectName(u"displaybutton")
        self.displaybutton.setGeometry(QRect(330, 520, 113, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 22))
        self.menuball = QMenu(self.menubar)
        self.menuball.setObjectName(u"menuball")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuball.menuAction())
        self.menuball.addAction(self.actioncreate)
        self.menuball.addAction(self.actionbrowse)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actioncreate.setText(QCoreApplication.translate("MainWindow", u"create", None))
        self.actionbrowse.setText(QCoreApplication.translate("MainWindow", u"browse", None))
        self.displaybutton.setText(QCoreApplication.translate("MainWindow", u"display", None))
        self.menuball.setTitle(QCoreApplication.translate("MainWindow", u"ball", None))
    # retranslateUi

