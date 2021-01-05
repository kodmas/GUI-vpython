# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'characteristc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 640)
        self.radius = QLineEdit(Form)
        self.radius.setObjectName(u"radius")
        self.radius.setGeometry(QRect(160, 70, 113, 21))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 70, 71, 31))
        self.position = QLineEdit(Form)
        self.position.setObjectName(u"position")
        self.position.setGeometry(QRect(170, 110, 113, 21))
        self.velocity = QLineEdit(Form)
        self.velocity.setObjectName(u"velocity")
        self.velocity.setGeometry(QRect(170, 150, 113, 21))
        self.acceleration = QLineEdit(Form)
        self.acceleration.setObjectName(u"acceleration")
        self.acceleration.setGeometry(QRect(170, 210, 113, 21))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 150, 71, 31))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 110, 71, 31))
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 200, 101, 31))
        self.buttonBox = QDialogButtonBox(Form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(280, 280, 164, 32))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
    

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    #def quit():

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">radius</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">velocity</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">position</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">accleration</span></p></body></html>", None))
    # retranslateUi

