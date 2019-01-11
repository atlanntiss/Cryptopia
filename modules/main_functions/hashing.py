######################################################
##
## Hashing module.
## This module defines all the hashing functions of 
## Cryptopia.
##
######################################################

# Standard library modules.
import hashlib
from os.path import getsize

# Modules of the project.
from modules.data_input import get_input_data
from modules.config import ALL_FUNCTIONS, INDENT

def md5(mode):
    """
    The MD5 function.
    """

    return get_hash("md5", mode)

def md5_manual():
    """
    The function, which returns the 
    MD5 hash function manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
MD5 HASH FUNCTION MANUAL.
{delimiter}
The MD5 (message-digest 5 algorithm) is a popular 128-bit hash
function, which was developed by Ronald Rivest in 1991. The
MD5 was widely used for hashing passwords in databases and
verifying data integrity.
{delimiter}
Security.
The security level of MD5 was compromised, so now this is not
secure to use this for hashing passwords at all."""
    manual = f"\n{INDENT}".join((manual.split("\n")))
    return manual

def get_hash(hash_function, mode):
    """
    The main function for almost all the hashing functions.
    It was defined since almost all the hashing algorithms 
    in this program have the same pattern of the code.
    """

    output_data = dict()

    if mode == "man":
        output_data["manual"] = globals()[hash_function + "_manual"]()
        return output_data

    # Getting all the data required to implement the 
    # Caesar cipher algorithm.
    input_data = get_input_data(ALL_FUNCTIONS["hashing"]["functions"][hash_function][mode])

    if "ERROR" not in input_data:
        # We have to decide here whether we calculate 
        # the hash sum of a file or text.
        if "text" in input_data:
            target = output_data["plaintext"] = input_data["text"]
        elif "file" in input_data:
            target = output_data["file"] = input_data["file"]
        
        # Hashing.
        result = getattr(hashlib, hash_function)()
        if mode == "hash_str":
            result.update(target.encode("UTF-8"))
        elif mode == "hash_file":
            with open(target, "rb") as file:
                if (getsize(target) / 1024 / 1024) >= 1024:
                    # If the file size is greater than or equal to 
                    # 1 gigabyte, we apply a hash function to the 
                    # file through blocks.
                    BLOCKSIZE = 2 ** 20
                    content = file.read(BLOCKSIZE)
                    while len(content) > 0:
                        result.update(content)
                        content = file.read(BLOCKSIZE)
                else:
                    content = file.read()
                    result.update(content)

        output_data["hash sum"] = result.hexdigest()
    else:
        # Handling errors.
        output_data["ERROR"] = input_data["ERROR"]
    
    return output_data