import sqlite3
import os

from constants import constants


class DbSession(object):
    """
    This class provides a layer of abstraction for
    when performing database transactions.
    """

    def __init__(self):
        """
        Makes the connection to the database, which allows for
        transactions to take place.
        """
        if constants.database_path:
            self.connection = sqlite3.connect(constants.database_path)
        else:
            self.connection = sqlite3.connect(self._get_database_path(self))

        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def commit(self):
        """
        Commits the database transaction. close(self) must be called after
        this method to successfully disconnect from the database.

        :return:
        """
        self.connection.commit()

    def close(self):
        """
        Terminates the connection to the database.

        :return:
        """
        self.cursor.close()
        self.connection.close()

    def create_tables_if_none_exist(self):
        """
        Creates the tables Packet and User if they don't already exist.

        :return:
        """
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
        """
        Gets the number of rows for a given table.

        :param table_name: the name of the table
        :return: a number which represents the row count of the table
        """
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

        self.cursor.execute('SELECT * FROM ' + table_name)
        row = self.cursor.fetchone()

        self.connection.close()

        return len(row)

    @staticmethod
    def _get_database_path(self):
        """
        Attempts to find the path of the database. This method will create
        a new database if one doesn't already exist.

        :param self:
        :return: the path to the database
        """
        if not os.path.exists('C:\\Program Files\\KeepInChecker\\KeepInChecker.sqlite'):
            os.mkdir('C:\\Program Files\\KeepInChecker\\')

        constants.database_path = 'C:\\Program Files\\KeepInChecker\\KeepInChecker.sqlite'

        return constants.database_path
