import unittest

from utilities import email_utilities


class EmailUtilitiesTest(unittest.TestCase):

    def test_get_mail_server(self):
        gmail_address = 'test@gmail.com'
        self.assertEqual(email_utilities.get_mail_server(gmail_address), 'smtp.gmail.com',
                         'Strings should be equal')

        yahoo_address = 'test@yahoo.com'
        self.assertEqual(email_utilities.get_mail_server(yahoo_address), 'smtp.mail.yahoo.com',
                         'Strings should be equal')

        outlook_address = 'test@outlook.com'
        self.assertEqual(email_utilities.get_mail_server(outlook_address), 'smtp-mail.outlook.com',
                         'Strings should be equal')

    def test_get_port(self):
        gmail_mail_server = 'smtp.gmail.com'
        self.assertEqual(email_utilities.get_port(gmail_mail_server), 587, 'Integers should be equal')

        verizon_mail_server = 'smtp.verizon.net'
        self.assertEqual(email_utilities.get_port(verizon_mail_server), 465, 'Integers should be equal')


if __name__ == '__main__':
    unittest.main()
