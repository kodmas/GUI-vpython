# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'floor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_floor(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 640)
        self.width = QLineEdit(Form)
        self.width.setObjectName(u"width")
        self.width.setGeometry(QRect(180, 100, 113, 21))
        self.length = QLineEdit(Form)
        self.length.setObjectName(u"length")
        self.length.setGeometry(QRect(180, 160, 113, 21))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 100, 60, 31))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 160, 60, 21))
        self.buttonBox = QDialogButtonBox(Form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(270, 240, 164, 32))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">width</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">length</span></p></body></html>", None))
    # retranslateUi

