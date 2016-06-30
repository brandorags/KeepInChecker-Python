import base64

from constants import secret_key
from Crypto.Cipher import AES


key = secret_key.key
iv = secret_key.iv


def encrypt(value):
    """
    Encrypts the data.

    :param value: the data to encrypt
    :return: an encrypted value of
    the parameter passed in
    """
    cipher = AES.new(key, AES.MODE_CFB, iv)
    encrypted_value = cipher.encrypt(value)

    return base64.b64encode(encrypted_value)


def decrypt(value):
    """
    Decrypts the data.

    :param value: encrypted data
    :return: a decrypted value of
    the parameter passed in
    """
    cipher = AES.new(key, AES.MODE_CFB, iv)
    decrypted_value = cipher.decrypt(base64.b64decode(value))

    return decrypted_value
