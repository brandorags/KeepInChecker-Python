# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui_files/launcher_dialog.ui'
#
# Created: Wed Apr 13 23:22:23 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

import multiprocessing
import subprocess
import platform
import sys
import os

from PySide import QtCore, QtGui


class LauncherDialog(QtGui.QWidget):

    def __init__(self):
        super(LauncherDialog, self).__init__()
        self.setup_ui(self)

    def setup_ui(self, launcher_dialog):
        launcher_dialog.setObjectName('launcher_dialog')
        launcher_dialog.resize(313, 191)
        self.verticalLayoutWidget = QtGui.QWidget(launcher_dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 0, 271, 41))
        self.verticalLayoutWidget.setObjectName('verticalLayoutWidget')
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName('verticalLayout')
        self.launcher_description_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.launcher_description_label.setObjectName('launcher_description_label')
        self.verticalLayout.addWidget(self.launcher_description_label)
        self.horizontalLayoutWidget = QtGui.QWidget(launcher_dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 261, 51))
        self.horizontalLayoutWidget.setObjectName('horizontalLayoutWidget')
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.password_label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.password_label.setObjectName('password_label')
        self.horizontalLayout_2.addWidget(self.password_label)
        self.password_textbox = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.password_textbox.setEchoMode(QtGui.QLineEdit.Password)
        self.password_textbox.setObjectName('password_textbox')
        self.horizontalLayout_2.addWidget(self.password_textbox)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(launcher_dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 90, 271, 80))
        self.horizontalLayoutWidget_2.setObjectName('horizontalLayoutWidget_2')
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName('horizontalLayout_3')
        self.ok_button = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.ok_button.setObjectName('ok_button')
        self.ok_button.clicked.connect(self.launch_application)
        self.horizontalLayout_3.addWidget(self.ok_button)
        self.cancel_button = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.cancel_button.setObjectName('cancel_button')
        self.cancel_button.clicked.connect(self.cancel)
        self.horizontalLayout_3.addWidget(self.cancel_button)

        self.retranslate_ui(launcher_dialog)
        QtCore.QMetaObject.connectSlotsByName(launcher_dialog)

        self.password_textbox.returnPressed.connect(self.launch_application)

        self.move(QtGui.QApplication.desktop().screen().rect().center() - self.rect().center())

    def retranslate_ui(self, launcher_dialog):
        launcher_dialog.setWindowTitle(QtGui.QApplication.translate('launcher_dialog', 'KeepInChecker Launcher', None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.launcher_description_label.setText(QtGui.QApplication.translate('launcher_dialog',
                                                                             'KeepInChecker requires authentication to run.',
                                                                             None, QtGui.QApplication.UnicodeUTF8))
        self.password_label.setText(QtGui.QApplication.translate('launcher_dialog', 'Password:', None,
                                                                 QtGui.QApplication.UnicodeUTF8))
        self.ok_button.setText(QtGui.QApplication.translate('launcher_dialog', 'Ok', None,
                                                            QtGui.QApplication.UnicodeUTF8))
        self.cancel_button.setText(QtGui.QApplication.translate('launcher_dialog', 'Cancel', None,
                                                                QtGui.QApplication.UnicodeUTF8))

    def launch_application(self):
        password = self.password_textbox.text()
        operating_system = platform.system()

        if 'darwin' in operating_system.lower():
            if not self._is_password_correct(password):
                sys.exit()

            # because of how the path is generated with .app files, we need to remove the directories
            # from the launcher's path to correctly form the path where the app resides
            # so, original path = /Users/User/Launcher.app/Contents/MacOS
            # and new_path = /Users/User
            path_to_app = self._format_path(os.path.realpath(os.path.dirname(sys.argv[0])), 3)

            cmd = 'echo "' + password + '" | sudo -S ' + path_to_app + '/KeepInChecker.app/Contents' \
                '/MacOS/KeepInChecker.app &'
            os.system(cmd)

            remove_command_process = multiprocessing.Process(target=self._remove_command_from_shell_history)
            remove_command_process.start()

        sys.exit()

    def cancel(self):
        sys.exit()

    def _is_password_correct(self, password):
        os.system('echo ' + password + ' | sudo -S -k mkdir /opt/KeepInCheckerTestTestTest')

        dirs = subprocess.check_output('ls /opt', stderr=subprocess.PIPE, shell=True)
        if 'KeepInCheckerTestTestTest' in dirs:
            os.system('echo ' + password + ' | sudo -S -k rmdir /opt/KeepInCheckerTestTestTest')
            return True

        return False

    def _format_path(self, path, number_of_dirs_to_remove_from_path):
        formatted_path = path.split('/')

        for i in xrange(0, number_of_dirs_to_remove_from_path):
            del formatted_path[len(formatted_path) - 1]

        return '/'.join(formatted_path)

    def _get_shell_type(self):
        return os.getenv('SHELL').split('/')[2]

    def _remove_command_from_shell_history(self):
        current_username = os.popen('whoami').read().strip()
        hist_file_path = '/Users/' + current_username + '/.' + self._get_shell_type() + '_history'
        hist_file = open(hist_file_path, 'r')

        lines = hist_file.readlines()
        hist_file.close()

        hist_file = open(hist_file_path, 'w')
        for i in xrange(0, len(lines)):
            if i != len(lines) - 1:
                hist_file.write(lines[i])
            elif 'keepinchecker' not in lines[i].lower():
                hist_file.write(lines[i])

        hist_file.truncate()
        hist_file.close()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    launcher_dialog = LauncherDialog()
    launcher_dialog.show()
    launcher_dialog.activateWindow()
    launcher_dialog.raise_()
    sys.exit(app.exec_())
