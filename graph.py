# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graph.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_graph(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 640)
        self.v_tgraph = QCheckBox(Form)
        self.v_tgraph.setObjectName(u"v_tgraph")
        self.v_tgraph.setGeometry(QRect(160, 80, 87, 20))
        self.E_tgraph = QCheckBox(Form)
        self.E_tgraph.setObjectName(u"E_tgraph")
        self.E_tgraph.setGeometry(QRect(160, 130, 87, 20))
        self.buttonBox = QDialogButtonBox(Form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(280, 240, 164, 32))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.v_tgraph.setText(QCoreApplication.translate("Form", u"v-t graph", None))
        self.E_tgraph.setText(QCoreApplication.translate("Form", u"E-t graph", None))
    # retranslateUi

