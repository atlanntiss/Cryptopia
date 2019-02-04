######################################################
##
## Crypto module.
## This module defines all the cryptosystems of
## Cryptopia.
##
######################################################

# Standard library modules.
from math import ceil
from string import ascii_uppercase, ascii_lowercase

## Modules of the project.
from modules.extra_modules.detect_english import *
from modules.data_input import get_input_data, input_parameter
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
    The Caesar cipher bruteforce cryptanalysis.
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

## The transposition cipher.

def transposition(mode):
    """
    The transposition cipher function.
    """
    
    output_data = dict()

    # Getting all the data required to implement the 
    # transposition cipher algorithm.
    input_data = get_input_data(ALL_FUNCTIONS["ciphers"]["functions"]["transposition"][mode])

    if mode == "man":
        output_data["manual"] = transposition_manual()
        return output_data
    else:
        if "ERROR" not in input_data:
            if mode in ["encrypt", "decrypt"]:
                # Getting a key.
                key = input_parameter(
                    f"a key (1 < integer < {len(input_data['text'])} (the length of the message))",
                    int,
                    range(1, len(input_data["text"])))
                if "ERROR" in key:
                    # Handling errors.
                    output_data["ERROR"] = key["ERROR"]
                else:
                    result = transposition_translate(input_data["text"], key["data"], mode)
                    # For accuracy, the program shows a user whether 
                    # we decrypt a ciphertext or encrypt a plaintext.
                    if mode == "encrypt":
                        output_data["plaintext"] = input_data["text"]
                        output_data["ciphertext"] = result
                    else:
                        output_data["ciphertext"] = input_data["text"]
                        output_data["plaintext"] = result
                    output_data["key"] = key["data"]
            elif mode == "crack":
                possible_keys = transposition_crack(input_data["text"])
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

def transposition_translate(text, key, mode):
    """
    The transposition cipher algorithm.
    """

    result = []

    if mode == "encrypt":
        # The number of columns equals to the length of a key.
        result = [""] * key
        for column in range(key):
            current_index = column
            while current_index < len(text):
                result[column] += text[current_index]
                current_index += key
        # We add this "|"" in order to make spaces at the end
        # of a message visible.
        result.append("|")
    elif mode == "decrypt":
        if text[len(text) - 1] == "|":
            # We do this step in order to remove the needless
            # char "|", which we add after the encryption process.
            # Now we do not need this, since the char will make
            # the decryption incorrect.
            text = text[:len(text) - 1]
        num_of_columns = int(ceil(len(text) / float(key)))
        num_of_rows = key
        num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(text)
        result = [""] * num_of_columns
        
        column = 0
        row = 0
        for char in text:
            result[column] += char
            column += 1
            if (column == num_of_columns) or ((column == (num_of_columns - 1)) and (row >= num_of_rows - num_of_shaded_boxes)):
                # If there are no more columns or we are at a
                # shaded box, switch to the first column and
                # the next row.
                column = 0
                row += 1

    return "".join(result)

def transposition_crack(text):
    """
    The Transposition cipher bruteforce cryptanalysis.
    """

    possible_keys = list()

    for key in range(2, len(text)):
        decrypted_text = transposition_translate(text, key, "decrypt")
        if is_english(decrypted_text):
            possible_keys.append(str(key))
            print(colorize_text("RESULT", f"{INDENT}Key {key: <2} >>> {decrypted_text}"))
        else:
            print(colorize_text("DATA", f"{INDENT}Key {key: <2} >>> {decrypted_text}"))
    
    return possible_keys

def transposition_manual():
    """
    The function, which returns the 
    Transposition cipher manual.
    """

    delimiter = "=" * 66
    manual = f"""
{delimiter}
TRANSPOSITION CIPHER MANUAL.
{delimiter}
The transposition cipher is a cryptosystem, which performs some
permutation of the characters of a plaintext. It simply reorders
the chars, changing their positions.
{delimiter}
Here is the process of encryption.

1. Set a key, which is greater than 1 and less than the length
of a message.
2. It is the time to build a table. Divide the length of a
message by the key and round it up to get the number of rows. The
number of columns is equal to the key.
3. Fill a plaintext in the boxes of your table from the left to
the right. If a row ends, but you still have some characters
left, go to the next row and continue.
4. When you are done, just cross out the unused boxes.
5. Write down the ciphertext, reading from the top left and going
down each column. When you get to the bottom of a column, go to
the next one to the right. Skip the boxes, which were crossed
out.

The decryption process is a little bit different.
1. Knowing the key, build the table, where the number of columns
is equal to the number of rows and the number of rows is equal
to the number of columns from the encryption process in the last
instruction (use the same calculations you used when encrypting).
2. Calculate the number of the boxes, which you need to cross
out: (The number of columns * the number of rows) - the length of
the ciphertext.
3. Cross out the number of boxes you have gotten in the last step
at the bottom of the rightmost column.
4. Fill the ciphertext in the boxes of your table from the left
to the right. If a row ends, but you still have some characters
left, go to the next row and continue. Skip the boxes, which were
crossed out before.
5. Write down the plaintext, reading from the top left and going
down each column. When you get to the bottom of a column, go to
the next one to the right.

A little, but important note.
You might already notice that we add a "|" to results after
encrypting, and do not consider them while deciphering. Here is
why. We add this "|" in order for you to see space characters in
a ciphertext at the end of the string. "|" is not a part of a
ciphertext. To decrypt such a text, you MUST to leave this "|"
untouched, otherwise Cryptopia will clean all the space
characters aroung the input, and the decryption will be
incorrect. The decryption program will delete this "|" by
itself, so do not worry.

{delimiter}
Cryptanalysis.
Since the range of keys for this cipher is really small, it is
not so hard to find keys through a bruteforce attack. The number
of possible keys is the length of the message, but we do not
count the key 1 and the key, which is equal to the length of the
message, since you do not really encipher a message using those
keys. So, the number of possible keys is the length of a message
- 2. 
"""
    manual = f"\n{INDENT}".join((manual.split("\n")))
    return manual