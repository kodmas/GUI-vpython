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
        #self.radius = QLineEdit("2")
        self.radius.setText("10")
        self.radius.setObjectName(u"radius")
        self.radius.setGeometry(QRect(170, 90, 113, 21))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 90, 71, 31))
        self.position = QLineEdit(Form)
        self.position.setText("(10,10,0)")
        self.position.setObjectName(u"position")
        self.position.setGeometry(QRect(170, 130, 113, 21))
        self.velocity = QLineEdit(Form)
        self.velocity.setText("(10,0,0)")
        self.velocity.setObjectName(u"velocity")
        self.velocity.setGeometry(QRect(170, 170, 113, 21))
        self.acceleration = QLineEdit(Form)
        self.acceleration.setText("(0,-9.8,0)")
        self.acceleration.setObjectName(u"acceleration")
        self.acceleration.setGeometry(QRect(170, 210, 113, 21))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 170, 71, 31))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 130, 71, 31))
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 210, 101, 31))
        self.buttonBox = QDialogButtonBox(Form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(300, 370, 164, 32))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.mass = QLineEdit(Form)
        self.mass.setText("20")
        self.mass.setObjectName(u"mass")
        self.mass.setGeometry(QRect(170, 260, 113, 21))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 260, 60, 21))
        self.make_Trail = QCheckBox(Form)
        self.make_Trail.setObjectName(u"make_Trail")
        self.make_Trail.setGeometry(QRect(80, 300, 181, 51))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">radius</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">velocity</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">position</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">accleration</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">mass</span></p></body></html>", None))
        self.make_Trail.setText(QCoreApplication.translate("Form", u"      make_Trail", None))
    # retranslateUi

