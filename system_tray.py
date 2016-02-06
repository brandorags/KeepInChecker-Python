import sys

from settings_dialog import SettingsDialog
from PySide.QtCore import *
from PySide.QtGui import *


class SystemTrayGui(object):
    def __init__(self):
        self.app = QApplication(sys.argv)

        menu = QMenu()
        settings_action = menu.addAction('Settings...')
        settings_action.triggered.connect(self.settings)
        quit_action = menu.addAction('Quit KeepInChecker')
        quit_action.triggered.connect(self.exit)

        icon = QIcon('Wu1QtZW.jpg')
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.show()

    def run(self):
        self.app.exec_()
        sys.exit()

    def settings(self):
        self.dialog = SettingsDialog()
        self.dialog.show()

    def exit(self):
        sys.exit()


if __name__ == '__main__':
    system_tray_gui = SystemTrayGui()
    system_tray_gui.app.setQuitOnLastWindowClosed(False)
    system_tray_gui.run()
