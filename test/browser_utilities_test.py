import unittest

from utilities import browser_utilities


class BrowserUtilitiesTest(unittest.TestCase):

    def test_is_browser_open(self):
        # NOTE: the browser must be opened manually
        is_open = browser_utilities.is_browser_open()
        self.assertEqual(is_open, True, 'Browser should be open')


if __name__ == '__main__':
    unittest.main()
