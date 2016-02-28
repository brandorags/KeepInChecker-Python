# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/settings_dialog.ui'
#
# Created: Mon Feb 22 23:53:47 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

import threading
import re
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from PySide import QtCore, QtGui
from database import queries


class SettingsDialog(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setup_ui(self)

        self.email_regex = re.compile('^[\w\.\+\-]+@[\w]+\.[a-z]{2,3}$')

    def setup_ui(self, settings_dialog):
        settings_dialog.setObjectName('settings_dialog')
        settings_dialog.resize(408, 279)
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
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 100, 381, 91))
        self.horizontalLayoutWidget_4.setObjectName('horizontalLayoutWidget_4')
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName('horizontalLayout_5')
        self.partner_email_label = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.partner_email_label.setObjectName('partner_email_label')
        self.horizontalLayout_5.addWidget(self.partner_email_label)
        spacerItem3 = QtGui.QSpacerItem(10, 9, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.partner_email_table = QtGui.QTableWidget(self.horizontalLayoutWidget_4)
        self.partner_email_table.setShowGrid(False)
        self.partner_email_table.setRowCount(3)
        self.partner_email_table.setColumnCount(1)
        self.partner_email_table.setObjectName('partner_email_table')
        self.partner_email_table.setColumnCount(1)
        self.partner_email_table.setRowCount(10)
        item = QtGui.QTableWidgetItem()
        self.partner_email_table.setHorizontalHeaderItem(0, item)
        self.partner_email_table.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_5.addWidget(self.partner_email_table)
        self.horizontalLayoutWidget_6 = QtGui.QWidget(settings_dialog)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 220, 381, 51))
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
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 190, 223, 29))
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

        self.retranslate_ui(settings_dialog)
        QtCore.QMetaObject.connectSlotsByName(settings_dialog)
        settings_dialog.setTabOrder(self.name_textbox, self.email_textbox)
        settings_dialog.setTabOrder(self.email_textbox, self.password_textbox)
        settings_dialog.setTabOrder(self.password_textbox, self.partner_email_table)
        settings_dialog.setTabOrder(self.partner_email_table, self.email_frequency_combo_box)
        settings_dialog.setTabOrder(self.email_frequency_combo_box, self.save_button)
        settings_dialog.setTabOrder(self.save_button, self.cancel_button)

        self.move(QtGui.QApplication.desktop().screen().rect().center() - self.rect().center())

    def retranslate_ui(self, settings_dialog):
        settings_dialog.setWindowTitle(QtGui.QApplication.translate('settings_dialog', 'Settings', None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.name_label.setText(QtGui.QApplication.translate('settings_dialog', 'Name:', None,
                                                             QtGui.QApplication.UnicodeUTF8))
        self.email_label.setText(QtGui.QApplication.translate('settings_dialog', 'Email:', None,
                                                              QtGui.QApplication.UnicodeUTF8))
        self.password_label.setText(QtGui.QApplication.translate('settings_dialog', 'Password:', None,
                                                                 QtGui.QApplication.UnicodeUTF8))
        self.partner_email_label.setText(QtGui.QApplication.translate('settings_dialog', 'Partners\' Emails:',
                                                                      None, QtGui.QApplication.UnicodeUTF8))
        self.partner_email_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate('settings_dialog',
                                                                                              'Email Address(es)', None,
                                                                                              QtGui.QApplication.UnicodeUTF8))
        self.save_button.setText(QtGui.QApplication.translate('settings_dialog', 'Save', None,
                                                              QtGui.QApplication.UnicodeUTF8))
        self.cancel_button.setText(QtGui.QApplication.translate('settings_dialog', 'Cancel', None,
                                                                QtGui.QApplication.UnicodeUTF8))
        self.email_frequency_label.setText(QtGui.QApplication.translate('settings_dialog', 'Email Frequency:', None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.email_frequency_combo_box.setItemText(0, QtGui.QApplication.translate('settings_dialog', 'Daily', None,
                                                                                   QtGui.QApplication.UnicodeUTF8))
        self.email_frequency_combo_box.setItemText(1, QtGui.QApplication.translate('settings_dialog', 'Weekly', None,
                                                                                   QtGui.QApplication.UnicodeUTF8))

    def save_user_settings(self):
        self.save_button.setDisabled(True)

        try:
            user_name = self.name_textbox.text()
            user_email = self.email_textbox.text()
            password = self.password_textbox.text()
            partner_email_table = self.partner_email_table
            email_frequency = self.email_frequency_combo_box.currentText()

            if self.are_fields_valid(user_name, user_email, password, partner_email_table):
                partner_emails = self.partner_emails_to_comma_separated_list(self, partner_email_table)

                save_user_thread = threading.Thread(target=queries.save_user_data,
                                                    args=(user_name, user_email, password,
                                                          partner_emails, email_frequency))
                save_user_thread.start()

                tray = QtGui.QSystemTrayIcon()
                tray.showMessage('Success', 'Your credentials have been saved')
        except:
            self.save_button.setDisabled(False)
            raise

        self.save_button.setDisabled(False)

    def are_fields_valid(self, user_name_text, user_email_text, password_text, partner_email_table):
        valid_fields = True

        # validate user name
        if not user_name_text:
            self.name_textbox.setStyleSheet(self.get_error_background_color(self))
            valid_fields = False
        else:
            self.name_textbox.setStyleSheet(self.get_successful_background_color(self))

        # validate email address
        validated_email_textbox = self.email_regex.match(user_email_text)
        if not validated_email_textbox:
            self.email_textbox.setStyleSheet(self.get_error_background_color(self))
            valid_fields = False
        else:
            self.email_textbox.setStyleSheet(self.get_successful_background_color(self))

        # validate password
        if not password_text:
            self.password_textbox.setStyleSheet(self.get_error_background_color(self))
            valid_fields = False
        else:
            self.password_textbox.setStyleSheet(self.get_successful_background_color(self))

        # validate partner emails
        column_index = 0
        is_table_empty = True
        is_item_selected = False
        for row in xrange(partner_email_table.rowCount()):
            email = partner_email_table.item(row, column_index)
            if not email or not email.text():
                continue

            is_table_empty = False
            validated_email_text = self.email_regex.match(str(email.text()))
            if not validated_email_text:
                email.setBackground(QtGui.QBrush(QtGui.QColor(255, 186, 186)))
                valid_fields = False
            else:
                email.setBackground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))

        for index in partner_email_table.selectedIndexes():  # check for emails that are currently selected
            is_item_selected = True
            selected_email = partner_email_table.item(index.row(), index.column())
            if not selected_email:
                if not is_table_empty:
                    partner_email_table.setItem(index.row(), index.column(), QtGui.QTableWidgetItem(''))
                    partner_email_table.itemAt(index.row(), index.column()).\
                        setBackground(QtGui.QBrush(QtGui.QColor(255, 186, 186)))
                    valid_fields = False
                else:
                    partner_email_table.setItem(0, 0, QtGui.QTableWidgetItem(''))
                    partner_email_table.itemAt(0, 0).setBackground(QtGui.QBrush(QtGui.QColor(255, 186, 186)))
                    valid_fields = False
            else:
                validated_selected_email_text = self.email_regex.match(str(selected_email.text()))
                if not validated_selected_email_text:
                    selected_email.setBackground(QtGui.QBrush(QtGui.QColor(255, 186, 186)))
                    valid_fields = False
                else:
                    selected_email.setBackground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))

        if is_table_empty and not is_item_selected:
            partner_email_table.setItem(0, 0, QtGui.QTableWidgetItem(''))
            partner_email_table.itemAt(0, 0).setBackground(QtGui.QBrush(QtGui.QColor(255, 186, 186)))

        return valid_fields

    def scroll_partner_email_table_to_top(self):
        self.partner_email_table.setItem(0, 0, QtGui.QTableWidgetItem(''))
        first_item = self.partner_email_table.item(0, 0)
        self.partner_email_table.scrollToItem(first_item, QtGui.QAbstractItemView.PositionAtTop)

    def cancel(self):
        self.name_textbox.setText('')
        self.name_textbox.setStyleSheet(self.get_successful_background_color(self))
        self.email_textbox.setText('')
        self.email_textbox.setStyleSheet(self.get_successful_background_color(self))
        self.password_textbox.setText('')
        self.password_textbox.setStyleSheet(self.get_successful_background_color(self))
        self.partner_email_table.clearContents()

        self.name_textbox.setFocus()

        self.close()

    @staticmethod
    def get_error_background_color(self):
        return 'background-color: rgb(255, 186, 186)'

    @staticmethod
    def get_successful_background_color(self):
        return 'background-color: rgb(255, 255, 255)'

    @staticmethod
    def partner_emails_to_comma_separated_list(self, partner_emails):
        partner_emails_as_comma_sep_list = ''

        column_index = 0
        for row in xrange(partner_emails.rowCount()):
            partner_email = partner_emails.item(row, column_index)
            if not partner_email:
                continue

            if partner_emails_as_comma_sep_list != '':
                partner_emails_as_comma_sep_list += ', ' + str(partner_email.text())
            else:
                partner_emails_as_comma_sep_list = str(partner_email.text())

        return partner_emails_as_comma_sep_list.strip()
