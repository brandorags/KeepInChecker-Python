import multiprocessing
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import keep_in_checker
import resources_rc

from settings_dialog import SettingsDialog
from PySide.QtGui import *


keep_in_checker_backend = multiprocessing.Process(target=keep_in_checker.main)


class SystemTray(object):
    def __init__(self):
        self.app = QApplication(sys.argv)

        menu = QMenu()
        settings_action = menu.addAction('Settings...')
        settings_action.triggered.connect(self.settings)
        quit_action = menu.addAction('Quit KeepInChecker')
        quit_action.triggered.connect(self.quit)

        icon = QIcon(':/gui/images/chevron-up.png')
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.setToolTip('KeepInChecker')
        self.tray.show()

        self.settings_dialog = SettingsDialog()

    def run(self):
        self.app.exec_()
        sys.exit()

    def settings(self):
        self.settings_dialog.scroll_partner_emails_table_to_top()
        self.settings_dialog.set_user_settings_on_open()
        self.settings_dialog.show()
        self.settings_dialog.activateWindow()
        self.settings_dialog.raise_()

    def quit(self):
        keep_in_checker_backend.terminate()
        sys.exit()


if __name__ == '__main__':
    keep_in_checker_backend.start()

    system_tray_gui = SystemTray()
    system_tray_gui.app.setQuitOnLastWindowClosed(False)
    system_tray_gui.run()
