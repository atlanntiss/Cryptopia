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
from binascii import hexlify

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
    manual = f"\n{INDENT}".join(manual.split("\n"))
    return manual

## SHA3-224.

def sha3_224(mode):
    """
    The SHA3-224 function.
    """

    return get_hash("sha3_224", mode)

def sha3_224_manual():
    """
    The function, which returns the
    SHA3-224 hash function manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
SHA3-224 HASH FUNCTION MANUAL.
{delimiter}
The SHA3-224 (224 bit) is a part of the SHA3 hash functions set,
which was developed by the NIST and first published in 2015. SHA3
is the latest memeber of the SHA family."""
    manual = f"\n{INDENT}".join(manual.split("\n"))
    return manual

## SHA3-256.

def sha3_256(mode):
    """
    The SHA3-256 function.
    """

    return get_hash("sha3_256", mode)

def sha3_256_manual():
    """
    The function, which returns the
    SHA3-256 hash function manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
SHA3-256 HASH FUNCTION MANUAL.
{delimiter}
The SHA3-256 (256 bit) is a part of the SHA3 hash functions set,
which was developed by the NIST and first published in 2015. SHA3
is the latest memeber of the SHA family."""
    manual = f"\n{INDENT}".join(manual.split("\n"))
    return manual

## SHA3-384.

def sha3_384(mode):
    """
    The SHA3-384 function.
    """

    return get_hash("sha3_384", mode)

def sha3_384_manual():
    """
    The function, which returns the
    SHA3-384 hash function manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
SHA3-384 HASH FUNCTION MANUAL.
{delimiter}
The SHA3-384 (384 bit) is a part of the SHA3 hash functions set,
which was developed by the NIST and first published in 2015. SHA3
is the latest memeber of the SHA family."""
    manual = f"\n{INDENT}".join(manual.split("\n"))
    return manual

## SHA3-512.

def sha3_512(mode):
    """
    The SHA3-512 function.
    """

    return get_hash("sha3_512", mode)

def sha3_512_manual():
    """
    The function, which returns the
    SHA3-512 hash function manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
SHA3-512 HASH FUNCTION MANUAL.
{delimiter}
The SHA3-512 (512 bit) is a part of the SHA3 hash functions set,
which was developed by the NIST and first published in 2015. SHA3
is the latest memeber of the SHA family."""
    manual = f"\n{INDENT}".join(manual.split("\n"))
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

## Whirlpool.

def whirlpool(mode):
    """
    The Whirlpool function.
    """

    return get_hash("whirlpool", mode, new=True)

def whirlpool_manual():
    """
    The function, which returns the 
    Whirlpool hash function manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
WHIRLPOOL HASH FUNCTION MANUAL.
{delimiter}
The Whirlpool is a 512-bit hash function, which was designed by
Vincent Rijmen and Paulo S. L. M. Barreto. It was published in
2000. The hash was accepted by the ISO, IEC, and recommended by
the NESSIE project.
{delimiter}
Security.
The function has hashsum size of 512 bits, which is essentially
big magnitude."""
    manual = f"\n{INDENT}".join((manual.split("\n")))
    return manual

## BLAKE2b.

def blake2b(mode):
    """
    The BLAKE2b function.
    """

    return get_hash("blake2b", mode, new=True)

def blake2b_manual():
    """
    The function, which returns the 
    BLAKE2b hash function manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
BLAKE2B HASH FUNCTION MANUAL.
{delimiter}
The BLAKE2b is a 512-bit hash function, which was developed by
Jean-Philippe Aumasson, Luca Henzen, Willi Meier, and Raphael
C. W. Phan. It is a variant of the BLAKE2 algorithm. The BLAKE2b
is faster than SHA-1, SHA-2, MD5, and SHA-3 on x64 and ARM
architectures.
{delimiter}
Security.
The security level of the BLAKE2 is better than the SHA-2 and
similar to the SHA-3."""
    manual = f"\n{INDENT}".join((manual.split("\n")))
    return manual

## BLAKE2s.

def blake2s(mode):
    """
    The BLAKE2s function.
    """

    return get_hash("blake2s", mode, new=True)

def blake2s_manual():
    """
    The function, which returns the 
    BLAKE2s hash function manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
BLAKE2S HASH FUNCTION MANUAL.
{delimiter}
The BLAKE2s is a 256-bit hash function, which was developed by
Jean-Philippe Aumasson, Luca Henzen, Willi Meier, and Raphael
C. W. Phan. It is a variant of the BLAKE2 algorithm. The BLAKE2s
is optimized for architectures such as 8 to 32 bit platforms."""
    manual = f"\n{INDENT}".join((manual.split("\n")))
    return manual

## PBKDF2.

def pbkdf2_hmac(mode):
    """
    The PBKDF2 function (a special one).
    """

    output_data = dict()

    if mode == "hash_file":
        output_data["ERROR"] = "not_supported"
    elif mode == "man":
        output_data["manual"] = globals()["pbkdf2_hmac_manual"]()
    else:
        # We are assuming here that the mode is hash_str.
        # Getting all the data required to implement the PBKDF2 function.
        input_data = get_input_data(ALL_FUNCTIONS["hashing"]["functions"]["pbkdf2_hmac"][mode])

        if "ERROR" not in input_data:
            salt = random_string(64)
            output_data["text"] = input_data["text"]
            output_data["hash function"] = input_data["hash_function"]
            output_data["salt"] = salt
            output_data["number of iterations"] = input_data["number_of_iterations"]
            result = hashlib.pbkdf2_hmac(
                input_data["hash_function"],
                output_data["text"].encode("utf-8"),
                salt.encode("utf-8"),
                input_data["number_of_iterations"])
            output_data["hash sum"] = hexlify(result).decode("utf-8")
        else:
            # Handling errors.
            output_data["ERROR"] = input_data["ERROR"]
    
    return output_data

def pbkdf2_hmac_manual():
    """
    The function, which returns the 
    PBKDF2 function manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
PBKDF2 FUNCTION MANUAL.
{delimiter}
The PBKDF2 (Password-Based Key Derivation Function 2) is a key
derivation function, aimed to reduce the possibilities of
successful brute force attacks. It applies HMAC - hash-based
message authentication code."""
    manual = f"\n{INDENT}".join((manual.split("\n")))
    return manual

def get_hash(hash_function, mode, new=False):
    """
    The main function for almost all the hashing functions.
    It was defined since almost all the hashing algorithms 
    in this program have the same pattern of the code.
    """

    # We have the argument "new" since there are some functions
    # executable only by hashlib.new(name).

    output_data = dict()

    if mode == "man":
        output_data["manual"] = globals()[hash_function + "_manual"]()
        return output_data

    # Getting all the data required to implement a hash function.
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
                # The length of a salt must be equal to the digest
                # size.
                salt = output_data["salt"] = random_string(len(result.hexdigest()))
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
