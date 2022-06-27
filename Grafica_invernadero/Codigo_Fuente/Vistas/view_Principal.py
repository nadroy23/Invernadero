# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view_PrincipalgPkvhP.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(700, 480)
        Dialog.setMinimumSize(QSize(700, 480))
        Dialog.setMaximumSize(QSize(700, 480))
        Dialog.setCursor(QCursor(Qt.CrossCursor))
        self.frame_base = QFrame(Dialog)
        self.frame_base.setObjectName(u"frame_base")
        self.frame_base.setEnabled(True)
        self.frame_base.setGeometry(QRect(-1, -1, 700, 480))
        self.frame_base.setMinimumSize(QSize(700, 480))
        self.frame_base.setMaximumSize(QSize(700, 480))
        font = QFont()
        font.setItalic(True)
        self.frame_base.setFont(font)
        self.frame_base.setCursor(QCursor(Qt.CrossCursor))
        self.frame_base.setMouseTracking(False)
        self.frame_base.setStyleSheet(u"background-color: rgb(224, 239, 255);")
        self.frame_base.setFrameShape(QFrame.StyledPanel)
        self.frame_base.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frame_base)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 19, 641, 91))
        self.frame.setStyleSheet(u"background-color: rgb(196, 214, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 10, 571, 71))
        font1 = QFont()
        font1.setFamily(u"MS UI Gothic")
        font1.setPointSize(47)
        font1.setItalic(True)
        self.label.setFont(font1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Graficas Invernadero", None))
    # retranslateUi

