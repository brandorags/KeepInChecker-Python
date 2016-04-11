import base64


def encode(string, key):
    """
    implements the Vignere cipher to encode strings
    credit - ilogik (https://gist.github.com/ilogik/6f9431e4588015ecb194)

    :param string - the string to encode
    :param key - the value used against the string to create the cipher
    :return an encoded string
    """
    encoded_chars = []
    for i in xrange(len(string)):
        key_char = key[i % len(key)]
        encoded_char = chr(ord(string[i]) + ord(key_char) % 256)
        encoded_chars.append(encoded_char)

    encoded_string = base64.urlsafe_b64encode(''.join(encoded_chars))

    return encoded_string


def decode(string, key):
    """
    implements the Vignere cipher to decode strings
    credit - ilogik (https://gist.github.com/ilogik/6f9431e4588015ecb194)

    :param string - the string to decode
    :param key - the value used against the string to create the cipher
    :return an decoded string
    """
    decoded_chars = []
    string = base64.urlsafe_b64decode(str(string))
    for i in xrange(len(string)):
        key_char = key[i % len(key)]
        encoded_char = chr(abs(ord(string[i]) - ord(key_char) % 256))
        decoded_chars.append(encoded_char)

    decoded_string = ''.join(decoded_chars)

    return decoded_string
