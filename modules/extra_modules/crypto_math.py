##################################################
##
## Crypto_math module
## This module defines all the mathematical
## functions such as secure random generation.
##
##################################################

## Standard modules.
from os import urandom

def random_string(length):
    """
    Returns a random symbol, which was generated using the 
    secure system random method.
    """

    if length > 1:
        result = list()
        for step in range(length):
            # We do not need any spaces in a string, so we 
            # do the process below to avoid them.
            char = " "
            while char in ["\n", "\t", "\v", "\b", "\r", " "]:
                char = chr(ord(urandom(1)))
            # And also strip() just to make sure.
            result.append(char.strip())
        result = "".join(result)
    elif length == 1:
        result = chr(ord(urandom(length)))
    
    return result