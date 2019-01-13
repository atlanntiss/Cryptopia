######################################################
##
## Crypto module.
## This module defines all the cryptosystems of
## Cryptopia.
##
######################################################

# Standard library modules.
from string import ascii_uppercase, ascii_lowercase

## Modules of the project.
from modules.data_input import get_input_data
from modules.extra_modules.detect_english import *
from modules.config import ALL_FUNCTIONS, INDENT, colorize_text

## The Caesar cipher.

def caesar(mode):
    """
    The Caesar cipher function.
    """
    
    output_data = dict()

    # Getting all the data required to implement the 
    # Caesar cipher algorithm.
    input_data = get_input_data(ALL_FUNCTIONS["ciphers"]["functions"]["caesar"][mode])

    if mode == "man":
        output_data["manual"] = caesar_manual()
        return output_data
    else:
        if "ERROR" not in input_data:
            if mode in ["encrypt", "decrypt"]:
                result = caesar_translate(input_data["text"], input_data["key"], mode)
                # For accuracy, the program shows a user whether 
                # we decrypt a ciphertext or encrypt a plaintext.
                if mode == "encrypt":
                    output_data["plaintext"] = input_data["text"]
                    output_data["ciphertext"] = result
                else:
                    output_data["ciphertext"] = input_data["text"]
                    output_data["plaintext"] = result
                output_data["key"] = input_data["key"]
            elif mode == "crack":
                possible_keys = caesar_crack(input_data["text"])
                if not possible_keys:
                    output_data["ERROR"] = "keys_not_found"
                else:
                    # We show the number of keys found (and those
                    # keys too, of course).
                    output_data[f"possible keys ({len(possible_keys)})"] = ", ".join(possible_keys)
        else:
            # Handling errors.
            output_data["ERROR"] = input_data["ERROR"]

        return output_data

def caesar_translate(text, key, mode):
    """
    The Caesar cipher algorithm.
    """

    result = []

    for char in text:
        char_index = ascii_uppercase.find(char.upper())
        if char_index != -1:
            # (En)/(de)cryption process.
            if mode == "encrypt":
                char_index += key
            elif mode == "decrypt":
                char_index -= key
            char_index %= len(ascii_uppercase)
            
            # We need to indetify whether a char was in uppercase 
            # or lowercase to output the result correctly.
            if char.isupper():
                result.append(ascii_uppercase[char_index])
            else:
                result.append(ascii_lowercase[char_index])
        else:
            result.append(char)

    return "".join(result)

def caesar_crack(text):
    """
    The Caesar cipher cryptanalysis.
    """

    possible_keys = list()

    for key in range(1, len(ascii_uppercase)):
        decrypted_text = caesar_translate(text, key, "decrypt")
        if is_english(decrypted_text):
            possible_keys.append(str(key))
            print(colorize_text("RESULT", f"{INDENT}Shift {key: <2} >>> {decrypted_text}"))
        else:
            print(colorize_text("DATA", f"{INDENT}Shift {key: <2} >>> {decrypted_text}"))
    
    return possible_keys

def caesar_manual():
    """
    The function, which returns the 
    Caesar cipher manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
CAESAR CIPHER MANUAL.
{delimiter}
The Caesar cipher is one of the oldest and most popular ciphers 
in the history of mankind. Julius Caesar used this cipher to
communicate with his generals. It is the simplest substitution 
cipher. Each letter of a plaintext is shifted by some number
called a shift. This shift (key) is an integer between 0 and 26
for English, which is the length of the alphabet.
{delimiter}
We have the mathematical model of the Caesar cipher:
C = (P + K) mod N
P = (C - K) mod N
where
    C is a ciphertext;
    P is a plaintext;
    K is a shift;
    N is the length of an alphabet (26 for English).
This operation must be applied to each letter of a message.
{delimiter}
Cryptanalysis.
The Caesar cipher is easy to hack. You can use a frequency 
cryptanalysis, but it will be faster if you use a simple
bruteforce attack. Because of the small keys range - 26 for 
Enlgish - it will be really fast."""
    manual = f"\n{INDENT}".join((manual.split("\n")))
    return manual