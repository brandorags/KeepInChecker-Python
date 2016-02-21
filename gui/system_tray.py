import sys

from settings_dialog import SettingsDialog
from PySide.QtGui import *


class SystemTray(object):
    def __init__(self):
        self.app = QApplication(sys.argv)

        menu = QMenu()
        settings_action = menu.addAction('Settings...')
        settings_action.triggered.connect(self.settings)
        quit_action = menu.addAction('Quit KeepInChecker')
        quit_action.triggered.connect(self.quit)

        icon = QIcon('./images/font-awesome-10-25186.png')
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
        self.settings_dialog.show()
        self.settings_dialog.activateWindow()
        self.settings_dialog.raise_()

    def quit(self):
        sys.exit()


if __name__ == '__main__':
    system_tray_gui = SystemTray()
    system_tray_gui.app.setQuitOnLastWindowClosed(False)
    system_tray_gui.run()
