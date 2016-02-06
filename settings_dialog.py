# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Sun Jan 31 16:51:22 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class SettingsDialog(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    
    def setupUi(self, Dialog):
        Dialog.setObjectName('Dialog')
        Dialog.resize(408, 240)
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 31))
        self.horizontalLayoutWidget.setObjectName('horizontalLayoutWidget')
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.name_label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.name_label.setObjectName('name_label')
        self.horizontalLayout.addWidget(self.name_label)
        spacerItem = QtGui.QSpacerItem(38, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.name_textbox = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.name_textbox.setObjectName('name_textbox')
        self.horizontalLayout.addWidget(self.name_textbox)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 381, 31))
        self.horizontalLayoutWidget_2.setObjectName('horizontalLayoutWidget_2')
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.email_label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.email_label.setObjectName('email_label')
        self.horizontalLayout_2.addWidget(self.email_label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.email_textbox = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.email_textbox.setObjectName('email_textbox')
        self.horizontalLayout_2.addWidget(self.email_textbox)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 70, 381, 31))
        self.horizontalLayoutWidget_3.setObjectName('horizontalLayoutWidget_3')
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName('horizontalLayout_3')
        self.password_label = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.password_label.setObjectName('password_label')
        self.horizontalLayout_3.addWidget(self.password_label)
        spacerItem2 = QtGui.QSpacerItem(16, 9, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.password_textbox = QtGui.QLineEdit(self.horizontalLayoutWidget_3)
        self.password_textbox.setObjectName('password_textbox')
        self.horizontalLayout_3.addWidget(self.password_textbox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate('Dialog', 'Dialog', None, QtGui.QApplication.UnicodeUTF8))
        self.name_label.setText(QtGui.QApplication.translate('Dialog', 'Name:', None, QtGui.QApplication.UnicodeUTF8))
        self.email_label.setText(QtGui.QApplication.translate('Dialog', 'Email:', None, QtGui.QApplication.UnicodeUTF8))
        self.password_label.setText(QtGui.QApplication.translate('Dialog', 'Password:', None, QtGui.QApplication.UnicodeUTF8))
