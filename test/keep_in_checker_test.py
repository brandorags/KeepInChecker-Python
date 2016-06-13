import unittest

from utilities import email_utilities
from datetime import datetime
from time import sleep


class KeepInCheckerTest(unittest.TestCase):

    def test_send_scheduled_email(self):
        email_attempt_passes = 0
        email_sent_counter = 0

        while email_attempt_passes <= 4:
            if email_attempt_passes == 2:
                sleep(6)

            time_of_last_email_sent_to_now = datetime.now() - email_utilities.date_last_email_was_sent
            if time_of_last_email_sent_to_now.seconds >= 5:
                email_utilities.has_email_been_sent = False

            if not email_utilities.has_email_been_sent:
                email_sent_counter += 1

                email_utilities.has_email_been_sent = True
                email_utilities.date_last_email_was_sent = datetime.now()

            email_attempt_passes += 1

        self.assertEqual(email_sent_counter, 1)


if __name__ == '__main__':
    unittest.main()
