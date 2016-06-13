import unittest

from utilities.security_utilities import encrypt, decrypt


url = 'http://example.com/example/123456/page?test=14'
name = 'John Doe'
various_characters = '1234567890!@#$%^&*()_+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}:"<>?[];\',./'


class SecurityUtilitiesTest(unittest.TestCase):

    def test_encrypt(self):
        encrypted_url = encrypt(url)
        self.assertNotEqual(encrypted_url, url, 'Strings should not be the same')

        encrypted_name = encrypt(name)
        self.assertNotEqual(encrypted_name, name, 'Strings should not be the same')

        encrypted_various_characters = encrypt(various_characters)
        self.assertNotEqual(encrypted_various_characters, various_characters, 'Strings should not be the same')

    def test_decrypt(self):
        encrypted_url = encrypt(url)
        decrypted_url = decrypt(encrypted_url)
        self.assertEqual(decrypted_url, url, 'Strings should be the same')

        encrypted_name = encrypt(name)
        decrypted_name = decrypt(encrypted_name)
        self.assertEqual(decrypted_name, name, 'Strings should be the same')

        encrypted_various_characters = encrypt(various_characters)
        decrypted_various_characters = decrypt(encrypted_various_characters)
        self.assertEqual(decrypted_various_characters, various_characters, 'Strings should be the same')


if __name__ == '__main__':
    unittest.main()
