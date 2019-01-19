##################################################
##
## Crypto_math module
## This module defines all the mathematical
## functions such as secure random generation.
##
##################################################

## Standard modules.
from os import urandom
from string import ascii_letters, punctuation, digits

def random_string(length):
    """
    Returns a random symbol, which was generated using the 
    secure system random method.
    """

    result = list()
    for step in range(length):
        # We do not need any spaces in a string, so we 
        # do the process below to avoid them.
        char = " "
        while char not in (ascii_letters + punctuation + digits):
            # And also strip() just to make sure.
            char = chr(ord(urandom(1))).strip()
        result.append(char)
    result = "".join(result)
    return result