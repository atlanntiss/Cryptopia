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
from modules.extra_modules.crypto_math import random_string

## MD4.

def md4(mode):
    """
    The MD4 function.
    """

    return get_hash("md4", mode, new=True)

def md4_manual():
    """
    The function, which returns the 
    MD5 hash function manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
MD4 HASH FUNCTION MANUAL.
{delimiter}
The MD4 (message-digest 4 algorithm) is a 128-bit hash function,
which was developed by Ronald Rivest in 1990.
{delimiter}
Security.
The security level of the MD4 is low. Full collision attacks may
be performed against this algorithm."""
    manual = f"\n{INDENT}".join(manual.split("\n"))
    return manual

## MD5.

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
function, which was developed by Ronald Rivest in 1991. The MD5
was widely used for hashing passwords in databases and verifying
data integrity.
{delimiter}
Security.
The security level of the MD5 was compromised, so now this is not
secure enough to use this for hashing passwords at all."""
    manual = f"\n{INDENT}".join((manual.split("\n")))
    return manual

## SHA1.

def sha1(mode):
    """
    The SHA1 function.
    """

    return get_hash("sha1", mode)

def sha1_manual():
    """
    The function, which returns the 
    SHA1 hash function manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
SHA1 HASH FUNCTION MANUAL.
{delimiter}
The SHA1 (secure hash algorithm 1) is a 160-bit hash function,
which was developed by the NSA and published in 1995.
{delimiter}
Security.
The algorithm was not considered to be a hash function of high-level
security. Also, it is possible to perform a collision attack against
SHA1, so it was done by Google and CWI Amsterdam in 2017."""
    manual = f"\n{INDENT}".join((manual.split("\n")))
    return manual

## SHA224.

def sha224(mode):
    """
    The SHA224 function.
    """

    return get_hash("sha224", mode)

def sha224_manual():
    """
    The function, which returns the 
    SHA224 hash function manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
SHA224 HASH FUNCTION MANUAL.
{delimiter}
The SHA224 (224 bit) is a part of the SHA2 hash functions set,
which was developed by the NSA and published in 2001."""
    manual = f"\n{INDENT}".join((manual.split("\n")))
    return manual

## SHA256.

def sha256(mode):
    """
    The SHA256 function.
    """

    return get_hash("sha256", mode)

def sha256_manual():
    """
    The function, which returns the 
    SHA256 hash function manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
SHA256 HASH FUNCTION MANUAL.
{delimiter}
The SHA256 (256 bit) is a part of the SHA2 hash functions set,
which was developed by the NSA and published in 2001."""
    manual = f"\n{INDENT}".join((manual.split("\n")))
    return manual

## SHA384.

def sha384(mode):
    """
    The SHA384 function.
    """

    return get_hash("sha384", mode)

def sha384_manual():
    """
    The function, which returns the 
    SHA384 hash function manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
SHA384 HASH FUNCTION MANUAL.
{delimiter}
The SHA384 (384 bit) is a part of the SHA2 hash functions set,
which was developed by the NSA and published in 2001."""
    manual = f"\n{INDENT}".join((manual.split("\n")))
    return manual

## SHA512.

def sha512(mode):
    """
    The SHA512 function.
    """

    return get_hash("sha512", mode)

def sha512_manual():
    """
    The function, which returns the 
    SHA512 hash function manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
SHA512 HASH FUNCTION MANUAL.
{delimiter}
The SHA512 (512 bit) is a part of the SHA2 hash functions set,
which was developed by the NSA and published in 2001."""
    manual = f"\n{INDENT}".join((manual.split("\n")))
    return manual

## Ripemd160.

def ripemd160(mode):
    """
    The RIMEPD160 function.
    """

    return get_hash("ripemd160", mode, new=True)

def ripemd160_manual():
    """
    The function, which returns the 
    RIMEPD160 hash function manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
RIPEMD160 HASH FUNCTION MANUAL.
{delimiter}
The RIPEMD160 (160 bit) is a part of the RIMEPD hash functions
set, which was developed at the COSIC research group at the 
Katholieke Universiteit Leuven in Belgium and published in 1996.
The RIPEMD160 was created in contrast to the SHA1 and SHA2,
designed by the NSA.
{delimiter}
Security.
There were no any collisions reported to the RIPEMD160."""
    manual = f"\n{INDENT}".join((manual.split("\n")))
    return manual

def get_hash(hash_function, mode, new=False):
    """
    The main function for almost all the hashing functions.
    It was defined since almost all the hashing algorithms 
    in this program have the same pattern of the code.
    """

    # We have an argument new since there are some functions
    # executable only by hashlib.new(name).

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
        
        ## Hashing.
        
        # Checking whether a function defined as a 
        # "new" one or not in the hashlib module.
        if new:
            result = hashlib.new(hash_function)
        else:
            result = getattr(hashlib, hash_function)()

        if mode == "hash_str":
            result.update(target.encode("UTF-8"))
            if input_data["salt_y_or_n"] == "y":
                salt = output_data["salt"] = random_string(32)
                result.update(salt.encode("UTF-8"))
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
