import hashlib
import random


def hash_str(string, char_slice_num):
    """
    char_slice_num is the number of characters to be sliced off
    starting from the last character of the string
    """
    try:
        char_slice_num = int(char_slice_num)
        salt = hashlib.sha1(str(random.random())).hexdigest()[:char_slice_num]
        hashed_str = hashlib.sha1(salt + string).hexdigest()
        return hashed_str
    except ValueError as e:
        raise e
