# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_dialog.ui'
#
# Created: Tue Feb 16 00:07:33 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

import threading

from PySide import QtCore, QtGui
from database import queries


class SettingsDialog(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, settings_dialog):
        settings_dialog.setObjectName('settings_dialog')
        settings_dialog.resize(408, 240)
        self.horizontalLayoutWidget = QtGui.QWidget(settings_dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 31))
        self.horizontalLayoutWidget.setObjectName('horizontalLayoutWidget')
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.name_label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.name_label.setObjectName('name_label')
        self.horizontalLayout.addWidget(self.name_label)
        spacerItem = QtGui.QSpacerItem(68, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.name_textbox = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.name_textbox.setObjectName('name_textbox')
        self.horizontalLayout.addWidget(self.name_textbox)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(settings_dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 381, 31))
        self.horizontalLayoutWidget_2.setObjectName('horizontalLayoutWidget_2')
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.email_label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.email_label.setObjectName('email_label')
        self.horizontalLayout_2.addWidget(self.email_label)
        spacerItem1 = QtGui.QSpacerItem(70, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.email_textbox = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.email_textbox.setObjectName('email_textbox')
        self.horizontalLayout_2.addWidget(self.email_textbox)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(settings_dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 70, 381, 31))
        self.horizontalLayoutWidget_3.setObjectName('horizontalLayoutWidget_3')
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName('horizontalLayout_3')
        self.password_label = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.password_label.setObjectName('password_label')
        self.horizontalLayout_3.addWidget(self.password_label)
        spacerItem2 = QtGui.QSpacerItem(47, 9, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.password_textbox = QtGui.QLineEdit(self.horizontalLayoutWidget_3)
        self.password_textbox.setEchoMode(QtGui.QLineEdit.Password)
        self.password_textbox.setObjectName('password_textbox')
        self.horizontalLayout_3.addWidget(self.password_textbox)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(settings_dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 100, 381, 31))
        self.horizontalLayoutWidget_4.setObjectName('horizontalLayoutWidget_4')
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName('horizontalLayout_5')
        self.partner_email_label = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.partner_email_label.setObjectName('partner_email_label')
        self.horizontalLayout_5.addWidget(self.partner_email_label)
        spacerItem3 = QtGui.QSpacerItem(16, 9, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.partner_email_textbox = QtGui.QLineEdit(self.horizontalLayoutWidget_4)
        self.partner_email_textbox.setEchoMode(QtGui.QLineEdit.Normal)
        self.partner_email_textbox.setObjectName('partner_email_textbox')
        self.horizontalLayout_5.addWidget(self.partner_email_textbox)
        self.horizontalLayoutWidget_6 = QtGui.QWidget(settings_dialog)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 160, 381, 80))
        self.horizontalLayoutWidget_6.setObjectName('horizontalLayoutWidget_6')
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName('horizontalLayout_7')
        self.save_button = QtGui.QPushButton(self.horizontalLayoutWidget_6)
        self.save_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.save_button.setObjectName('save_button')
        self.save_button.clicked.connect(self.save_user_settings)
        self.horizontalLayout_7.addWidget(self.save_button)
        self.cancel_button = QtGui.QPushButton(self.horizontalLayoutWidget_6)
        self.cancel_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.cancel_button.setObjectName('cancel_button')
        self.cancel_button.clicked.connect(self.cancel)
        self.horizontalLayout_7.addWidget(self.cancel_button)
        self.horizontalLayoutWidget_5 = QtGui.QWidget(settings_dialog)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 130, 223, 29))
        self.horizontalLayoutWidget_5.setObjectName('horizontalLayoutWidget_5')
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName('horizontalLayout_6')
        self.email_frequency_label = QtGui.QLabel(self.horizontalLayoutWidget_5)
        self.email_frequency_label.setObjectName('email_frequency_label')
        self.horizontalLayout_6.addWidget(self.email_frequency_label)
        spacerItem4 = QtGui.QSpacerItem(6, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.email_frequency_combo_box = QtGui.QComboBox(self.horizontalLayoutWidget_5)
        self.email_frequency_combo_box.setCursor(QtCore.Qt.PointingHandCursor)
        self.email_frequency_combo_box.setObjectName('email_frequency_combo_box')
        self.email_frequency_combo_box.addItem('')
        self.email_frequency_combo_box.addItem('')
        self.horizontalLayout_6.addWidget(self.email_frequency_combo_box)

        self.retranslateUi(settings_dialog)
        QtCore.QMetaObject.connectSlotsByName(settings_dialog)
        settings_dialog.setTabOrder(self.name_textbox, self.email_textbox)
        settings_dialog.setTabOrder(self.email_textbox, self.password_textbox)
        settings_dialog.setTabOrder(self.password_textbox, self.partner_email_textbox)
        settings_dialog.setTabOrder(self.partner_email_textbox, self.email_frequency_combo_box)
        settings_dialog.setTabOrder(self.email_frequency_combo_box, self.save_button)
        settings_dialog.setTabOrder(self.save_button, self.cancel_button)

    def retranslateUi(self, settings_dialog):
        settings_dialog.setWindowTitle(QtGui.QApplication.translate('settings_dialog', 'Settings', None, QtGui.QApplication.UnicodeUTF8))
        self.name_label.setText(QtGui.QApplication.translate('settings_dialog', 'Name:', None, QtGui.QApplication.UnicodeUTF8))
        self.email_label.setText(QtGui.QApplication.translate('settings_dialog', 'Email:', None, QtGui.QApplication.UnicodeUTF8))
        self.password_label.setText(QtGui.QApplication.translate('settings_dialog', 'Password:', None, QtGui.QApplication.UnicodeUTF8))
        self.partner_email_label.setText(QtGui.QApplication.translate('settings_dialog', 'Partner\'s Email:', None, QtGui.QApplication.UnicodeUTF8))
        self.save_button.setText(QtGui.QApplication.translate('settings_dialog', 'Save', None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_button.setText(QtGui.QApplication.translate('settings_dialog', 'Cancel', None, QtGui.QApplication.UnicodeUTF8))
        self.email_frequency_label.setText(QtGui.QApplication.translate('settings_dialog', 'Email Frequency:', None, QtGui.QApplication.UnicodeUTF8))
        self.email_frequency_combo_box.setItemText(0, QtGui.QApplication.translate('settings_dialog', 'Daily', None, QtGui.QApplication.UnicodeUTF8))
        self.email_frequency_combo_box.setItemText(1, QtGui.QApplication.translate('settings_dialog', 'Weekly', None, QtGui.QApplication.UnicodeUTF8))

    def save_user_settings(self):
        self.save_button.setDisabled(True)

        try:
            user_name = self.name_textbox.text()
            user_email = self.email_textbox.text()
            password = self.password_textbox.text()
            partner_email = self.partner_email_textbox.text()
            email_frequency = self.email_frequency_combo_box.currentText()

            insert_user_thread = threading.Thread(target=queries.save_user_data, args=(user_name, user_email, password,
                                                                                       partner_email, email_frequency))
            insert_user_thread.start()
        except:
            self.save_button.setDisabled(False)
            raise

        self.save_button.setDisabled(False)

    def cancel(self):
        self.close()
