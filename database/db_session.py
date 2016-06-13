import sqlite3
import os

from constants import constants


class DbSession(object):

    def __init__(self):
        if constants.database_path:
            self.connection = sqlite3.connect(constants.database_path)
        else:
            self.connection = sqlite3.connect(self._get_database_path(self))

        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def create_tables_if_none_exist(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS "Packet" (
                                    `PacketId` INTEGER NOT NULL,
                                    `DateReceived` TEXT NOT NULL,
                                    `Timezone` TEXT,
                                    `Get` TEXT,
                                    `Host` TEXT,
                                    `Referer` TEXT,
                                    PRIMARY KEY(PacketId)
                                )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS "User" (
                                    `UserId` INTEGER NOT NULL,
                                    `UserName` TEXT NOT NULL,
                                    `UserEmail` TEXT NOT NULL,
                                    `UserEmailPassword` TEXT NOT NULL,
                                    `PartnerEmails` TEXT NOT NULL,
                                    `EmailFrequency` TEXT NOT NULL,
                                    PRIMARY KEY(UserId)
                                )''')

        self.commit()
        self.close()

    def _get_column_count(self, table_name):
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

        self.cursor.execute('SELECT * FROM ' + table_name)
        row = self.cursor.fetchone()

        self.connection.close()

        return len(row)

    @staticmethod
    def _get_database_path(self):
        if not os.path.exists('/usr/local/.KeepInChecker/KeepInChecker.sqlite'):
            os.system('mkdir /usr/local/.KeepInChecker')

        constants.database_path = '/usr/local/.KeepInChecker/KeepInChecker.sqlite'

        return constants.database_path
