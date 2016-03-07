from cryptography.fernet import Fernet
from secret_key import key


"""
objectionable_words_list - list that contains words/phrases that are
considered objectionable content
"""
objectionable_words_list = ['stackoverflow', 'imgur', 'reddit', 'awesome']

"""
whitelisted_websites - list that contains websited that don't need to
be sniffed
"""
whitelisted_websites = []

"""
packet_keywords - list that's used to parse through relevant packet data
"""
packet_keywords = ['GET', 'Host', 'Referer']

"""
current_user - the cached user object that contains the user's
current credentials
"""
current_user = None

"""
cryptographer - object used for encrypting/decrypting data before it
gets sent to the database
"""
cryptographer = Fernet(key)
