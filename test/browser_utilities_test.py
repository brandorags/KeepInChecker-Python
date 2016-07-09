import unittest

from utilities import browser_utilities


class BrowserUtilitiesTest(unittest.TestCase):

    def test_remove_redundant_packets(self):
        packets = [{'07-11-2016 23:45:53': ['/questions/3287038/cron-and-virtualenv?rq=1', 'stackoverflow.com', 'http://stackoverflow.com/questions/990754/how-to-leave-exit-deactivate-a-python-virtualenv?rq=1']},
                   {'07-11-2016 23:45:59': ['', 'stackoverflow.com', 'http://stackoverflow.com/questions/38245784/different-letter-size-when-using-uppercase-letters']},
                   {'07-11-2016 23:45:55': ['/img/openid/new-login-sprite.png?v=79224c9ea1cb', 'cdn.sstatic.net', 'http://cdn.sstatic.net/Sites/stackoverflow/all.css?v=44a73cad850d']},
                   {'07-11-2016 23:45:57': ['/xqoqk.png', 'i.stack.imgur.com', 'http://stackoverflow.com/']},
                   {'07-11-2016 23:45:59': ['/FSlZ6.jpg', 'i.stack.imgur.com', 'http://stackoverflow.com/questions/38245784/different-letter-size-when-using-uppercase-letters']},
                   {'07-11-2016 23:46:13': ['', 'stackoverflow.com', 'http://stackoverflow.com/']},
                   {'07-11-2016 23:45:59': ['/img/openid/new-login-sprite.png?v=79224c9ea1cb', 'cdn.sstatic.net', 'http://cdn.sstatic.net/Sites/stackoverflow/all.css?v=44a73cad850d']},
                   {'07-11-2016 23:46:10': ['/favicon.ico', 'stackoverflow.com', '']},
                   {'07-11-2016 23:45:58': ['/questions/38245784/different-letter-size-when-using-uppercase-letters', 'stackoverflow.com', 'http://stackoverflow.com/']},
                   {'07-11-2016 23:45:57': ['/IOseh.png', 'i.stack.imgur.com', 'http://stackoverflow.com/']}]

        not_redundant_packet_list = browser_utilities.remove_redundant_packets(packets)
        self.assertEqual(len(not_redundant_packet_list), 7, 'All redundant packets should have been removed')


if __name__ == '__main__':
    unittest.main()
