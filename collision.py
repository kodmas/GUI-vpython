# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'collision.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_collision(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 640)
        self.ball_collision = QCheckBox(Form)
        self.ball_collision.setObjectName(u"ball_collision")
        self.ball_collision.setGeometry(QRect(130, 110, 101, 41))
        self.buttonBox = QDialogButtonBox(Form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(280, 230, 164, 32))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ball_collision.setText(QCoreApplication.translate("Form", u"ball collision", None))
    # retranslateUi

