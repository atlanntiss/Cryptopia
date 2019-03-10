######################################################
##
## Crypto module.
## This module defines all the cryptosystems of
## Cryptopia.
##
######################################################

# Standard library modules.
from math import ceil
from itertools import product
from string import ascii_uppercase, ascii_lowercase

## Modules of the project.
from modules.config import ALL_FUNCTIONS, INDENT, colorize_text
from modules.data_input import get_input_data, input_parameter, yes_or_no
from modules.extra_modules.detect_english import is_english, remove_non_letters

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
            elif mode == "attack":
                possible_keys = caesar_attack(input_data["text"])
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

def caesar_attack(ciphertext):
    """
    The Caesar cipher bruteforce cryptanalysis.
    """

    possible_keys = list()

    for key in range(1, len(ascii_uppercase)):
        decrypted_text = caesar_translate(ciphertext, key, "decrypt")
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
The Caesar cipher is one of the oldest and most popular ciphers in
the history of mankind. Julius Caesar used this cipher to
communicate with his generals. It is the simplest substitution
cipher. Each letter of a plaintext is shifted by some number
called a shift. This shift (key) is an integer between 0 and 26
for English, which is the length of the alphabet.
{delimiter}
We have the mathematical model of the Caesar cipher:
Cᵢ = (Pᵢ + K) mod N
Pᵢ = (Cᵢ - K) mod N
where
    C = C₀ ... Cₙ is a ciphertext;
    P = P₀ ... Pₙ is a plaintext;
    K is a shift;
    N is the length of an alphabet (26 for English).
    Subscript i (ᵢ) is the letter index in a text;
    Subscript n (ₙ) is the length of a text;
Note that we are dealing with the indexes of letters in the used
alphabet, while (en/de)crypting. So, when ABC encrypts with the
key 2, we say 0 + 2, 1 + 2, 2 + 2, since A -> 0, B -> 1, C -> 2
in English alphabet. Getting 234, convert this to the text: CDE.
{delimiter}
Cryptanalysis.
The Caesar cipher is easy to hack. You can use a frequency
cryptanalysis, but it will be faster if you use a simple
bruteforce attack. Because of the small keys range - 26 for
Enlgish - it will be really fast.
"""
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
            elif mode == "attack":
                possible_keys = transposition_attack(input_data["text"])
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

    result = list()

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

def transposition_attack(ciphertext):
    """
    The Transposition cipher bruteforce cryptanalysis.
    """

    possible_keys = list()

    for key in range(2, len(ciphertext)):
        decrypted_text = transposition_translate(ciphertext, key, "decrypt")
        if is_english(decrypted_text, word_percentage=60):
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

1. Set a key, which is greater than 1 and less than the length of
a message.
2. It is the time to build a table. Divide the length of a message
by the key and round it up to get the number of rows. The number
of columns is equal to the key.
3. Fill a plaintext in the boxes of your table from the left to
the right. If a row ends, but you still have some characters left,
go to the next row and continue.
4. When you are done, just cross out the unused boxes.
5. Write down the ciphertext, reading from the top left and going
down each column. When you get to the bottom of a column, go to
the next one to the right. Skip the boxes, which were crossed out.

The decryption process is a little bit different.
1. Knowing the key, build the table, where the number of columns
is equal to the number of rows and the number of rows is equal to
the number of columns from the encryption process in the last
instruction (use the same calculations you used when encrypting).
2. Calculate the number of the boxes, which you need to cross out:
(The number of columns * the number of rows) - the length of the
ciphertext.
3. Cross out the number of boxes you have gotten in the last step
at the bottom of the rightmost column.
4. Fill the ciphertext in the boxes of your table from the left to
the right. If a row ends, but you still have some characters left,
go to the next row and continue. Skip the boxes, which were
crossed out before.
5. Write down the plaintext, reading from the top left and going
down each column. When you get to the bottom of a column, go to
the next one to the right.

A little, but important note.
You might already notice that we add a "|" to results after
encrypting, and do not consider them while deciphering. Here is
why. We add this "|" in order for you to see space characters in a
ciphertext at the end of the string. "|" is not a part of a
ciphertext. To decrypt such a text, you MUST to leave this "|"
untouched, otherwise Cryptopia will clean all the space characters
aroung the input, and the decryption will be incorrect. The
decryption program will delete this "|" by itself, so do not
worry.
{delimiter}
Cryptanalysis.
Since the range of keys for this cipher is really small, it is not
so hard to find keys through a bruteforce attack. The number of
possible keys is the length of the message, but we do not count
the key 1 and the key, which is equal to the length of the
message, since you do not really encipher a message using those
keys. So, the number of possible keys is the length of a message
minus 2.
"""
    manual = f"\n{INDENT}".join((manual.split("\n")))
    return manual

## Frequency analysis.

# The order of letters' frequency in English.
ENGLISH_FREQUENCY = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def count_letters(text):
    """
    Counts every letter in a text.
    """

    # Preparing a dictionary for storing the letters and the
    # numbers of how many times they occur in a text.
    letters = dict()
    for letter in ascii_uppercase:
        letters[letter] = 0

    # Counting.
    for char in text.upper():
        if char in ascii_uppercase:
            letters[char] += 1
    
    return letters

def get_frequency_order(text):
    """
    Returns the letters arranged in order of most frequently
    occurring.
    """

    # A dictionary of each letter and its frequency.
    letters_frequency = count_letters(text)
    # A dictionary of each frequency to each letter
    # or letters with that frequency.
    frequency_letters = dict()
    for letter in ascii_uppercase:
        if letters_frequency[letter] not in frequency_letters:
            frequency_letters[letters_frequency[letter]] = [letter]
        else:
            frequency_letters[letters_frequency[letter]].append(letter)
    
    # Putting every list of letters in the reverse
    # ENGLISH_FREQUENCY order.
    for frequency in frequency_letters:
        frequency_letters[frequency].sort(key=ENGLISH_FREQUENCY.find, reverse=True)
        frequency_letters[frequency] = "".join(frequency_letters[frequency])
    
    frequency_pairs = list(frequency_letters.items())
    frequency_pairs.sort(key=lambda items: items[0], reverse=True)
    return "".join([frequency_pair[1] for frequency_pair in frequency_pairs])

def english_frequency_match_score(text):
    """
    Returns the number of matches of the frequency of a text
    with the English language frequency.
    """
    
    frequency_order = get_frequency_order(text)
    match_score = 0
    for common_letter in ENGLISH_FREQUENCY[:6]:
        if common_letter in frequency_order[:6]:
            match_score += 1
    for uncommon_letter in ENGLISH_FREQUENCY[-6:]:
        if uncommon_letter in frequency_order[-6:]:
            match_score += 1
    return match_score

## The Vigenere cipher.

# Just the initial value.
MAX_KEY_LENGTH = 0

def vigenere(mode):
    """
    The Vigenere cipher function.
    """
    
    output_data = dict()

    # Getting all the data required to implement the 
    # Vigenere cipher algorithm.
    input_data = get_input_data(ALL_FUNCTIONS["ciphers"]["functions"]["vigenere"][mode])

    if mode == "man":
        output_data["manual"] = vigenere_manual()
        return output_data
    else:
        if "ERROR" not in input_data:
            if mode in ["encrypt", "decrypt"]:
                result = vigenere_translate(input_data["text"], input_data["key"], mode)
                # For accuracy, the program shows a user whether 
                # we decrypt a ciphertext or encrypt a plaintext.
                if mode == "encrypt":
                    output_data["plaintext"] = input_data["text"]
                    output_data["ciphertext"] = result
                else:
                    output_data["ciphertext"] = input_data["text"]
                    output_data["plaintext"] = result
                output_data["key"] = input_data["key"]
            elif mode == "attack":
                global MAX_KEY_LENGTH
                MAX_KEY_LENGTH = input_data["max_key_length"]
                possible_keys = vigenere_attack(input_data["text"])
                if not possible_keys:
                    output_data["ERROR"] = "keys_not_found"
                else:
                    # We show the number of keys found (and those
                    # keys too, of course).
                    output_data[f"possible key"] = ", ".join(possible_keys)
        else:
            # Handling errors.
            output_data["ERROR"] = input_data["ERROR"]

        return output_data

def vigenere_translate(text, key, mode):
    """
    The Vigenere cipher algorithm.
    """

    result = list()

    key_index = 0
    for char in text:
        if char.upper() in ascii_uppercase:
            shift = ascii_uppercase.find(key[key_index].upper())
            if mode == "encrypt":
                char = caesar_translate(char, shift, "encrypt")
            else:
                char = caesar_translate(char, shift, "decrypt")
            result.append(char)

            key_index += 1
            if key_index == len(key):
                key_index = 0
        else:
            result.append(char)

    return "".join(result)

def find_repeated_sequences(ciphertext):
    """
    Finds any 3 to 5 letter sequences, which are repeated, in a
    ciphertext. Returns a dictionary with these sequences and the
    distances between them.
    """

    ciphertext = remove_non_letters(ciphertext.upper(), delete_spaces="yes")
    
    repeated_sequences = dict()
    for sequence_length in range(3, 6):
        for sequence_start in range(len(ciphertext) - sequence_length):
            # Determining a sequence.
            sequence = ciphertext[sequence_start:sequence_start + sequence_length]
            for index in range(sequence_start + sequence_length, len(ciphertext) - sequence_length):
                # Finding a stored sequence in the rest of a ciphertext.
                if ciphertext[index:index + sequence_length] == sequence:
                    if sequence not in repeated_sequences:
                        repeated_sequences[sequence] = list()
                    repeated_sequences[sequence].append(index - sequence_start)

    return repeated_sequences

def get_useful_factors(number):
    """
    Returns factors of a number, which are less than (MAX_KEY_LENGTH
    + 1) and not 1.
    """

    if number < 2:
        return []

    factors = list()
    for factor in range(2, MAX_KEY_LENGTH + 1):
        if number % factor == 0:
            factors.append(factor)
            other_factor = int(number / factor)
            if ((other_factor < MAX_KEY_LENGTH + 1) and (other_factor != 1)):
                factors.append(other_factor)
    
    return list(set(factors))

def get_most_common_factors(distance_factors):
    """
    Returns the most common factors from given distances' factors.
    """

    # Calculating of how many times different factors occur.
    factors_frequency = dict()
    for sequence in distance_factors:
        factor_list = distance_factors[sequence]
        for factor in factor_list:
            if factor not in factors_frequency:
                factors_frequency[factor] = 0
            factors_frequency[factor] += 1
    
    most_common_factors = list()
    for factor in factors_frequency:
        if factor <= MAX_KEY_LENGTH:
            most_common_factors.append((factor, factors_frequency[factor]))
    most_common_factors.sort(key=lambda items: items[1], reverse=True)
    
    return most_common_factors

def kasiski_examination(ciphertext):
    """
    Implements a Kasiski examination, which attacks a ciphertext
    in order to figure out the proper key length.
    """

    # The repeated_sequences is a dictionary of the following form:
    # {<SEQUENCE>: [<DISTANCE_1>, <DISTANCE_2>, ...], ...}.
    repeated_sequences = find_repeated_sequences(ciphertext)
    
    # Getting the factors of numbers, which were gotten above and
    # called distances.
    distance_factors = dict()
    for sequence in repeated_sequences:
        distance_factors[sequence] = list()
        for distance in repeated_sequences[sequence]:
            distance_factors[sequence].extend(get_useful_factors(distance))
    
    most_common_factors = get_most_common_factors(distance_factors)
    # Returning the possiblest key lengths.
    return [factor[0] for factor in most_common_factors]

def get_subkeys_letters(start_index, key_length, ciphertext):
    """
    Extracts a group of letters from a ciphertext, which is
    a text, enciphered by the single Caesar encryption.
    """

    ciphertext = remove_non_letters(ciphertext, delete_spaces="yes")
    index = start_index - 1
    group_of_letters = list()
    while index < len(ciphertext):
        group_of_letters.append(ciphertext[index])
        index += key_length
    return "".join(group_of_letters)

def vigenere_attempt_attack(ciphertext, key_length):
    """
    A part of the Vigenere cipher cryptanalysis process.
    Attempts an attack with a chosen key length.
    """

    # The list of key_length number of lists. The inner
    # lists are the frequency_score lists.
    all_frequency_scores = list()
    
    for start_index in range(1, key_length + 1):
        # Getting subgroups of a ciphertext.
        letters = get_subkeys_letters(start_index, key_length, ciphertext.upper())
        
        # The list below has the following format:
        # [(<a letter>, <its english frequency match score>), ...].
        frequency_scores = list()
        for possible_key in ascii_uppercase:
            decrypted_text = vigenere_translate(letters, possible_key, "decrypt")
            key_and_frequency_match = (possible_key, english_frequency_match_score(decrypted_text))
            frequency_scores.append(key_and_frequency_match)
        frequency_scores.sort(key=lambda items: items[1], reverse=True)
        
        all_frequency_scores.append(frequency_scores[:4])

    for frequency_score_index in range(len(all_frequency_scores)):
        # We use the (frequency_score_index + 1) expression in order
        # to index the first letter as 1 instead of 0.
        print(f"{INDENT}Possible letters for letter {frequency_score_index + 1} of the key: ", end="")
        print(f"{colorize_text('DATA', ' '.join([frequency_score[0] for frequency_score in all_frequency_scores[frequency_score_index]]))}.")
    input(f"{INDENT}[ENTER to continue]")
    
    # Trying every combination of the possiblest letters for a position
    # in a key.
    for indexes in product(range(4), repeat=key_length):
        possible_key = str()
        for key_index in range(key_length):
            possible_key += all_frequency_scores[key_index][indexes[key_index]][0]
        print(f"{INDENT}Attempting with the key of {colorize_text('DATA', possible_key)}.")
        
        decrypted_text = vigenere_translate(ciphertext.upper(), possible_key, "decrypt")
        if is_english(decrypted_text):
            # Setting a ciphertext to the original casing in the sake
            # of the printing the text for a user in the right casing.
            original_case = list()
            for index in range(len(ciphertext)):
                if ciphertext[index].isupper():
                    original_case.append(decrypted_text[index].upper())
                else:
                    original_case.append(decrypted_text[index].lower())
            possible_plaintext = "".join(original_case)

            print(f"{INDENT}A possible encryption hack with key {colorize_text('DATA', possible_key)}:")
            if len(possible_plaintext) > 100:
                possible_plaintext = f"{possible_plaintext[:100]}..."
            print(f"{INDENT}{colorize_text('DATA', possible_plaintext)}")
            
            # Asking whether we need to continue cracking or we do not.
            continue_cryptanalysis = "ERROR"
            while "ERROR" in continue_cryptanalysis:
                continue_cryptanalysis = yes_or_no("Do you want to continue cryptanalysis?")
            if continue_cryptanalysis["data"] == "n":
                return possible_key

    # If an attempt is failed, we return a None value.
    return None

def vigenere_attack(ciphertext):
    """
    The Vigenere cipher cryptanalysis, using Kasiski examination.
    """

    possible_keys = list()

    # The first step of cryptanalysis: getting all possible key lengths.
    possible_key_lengths = kasiski_examination(ciphertext)
    if possible_key_lengths:
        print(f"{INDENT}According to Kasiski examination, the most possible key lengths: {colorize_text('DATA', ', '.join(list(map(lambda number: str(number), possible_key_lengths))))}.")
    else:
        print(f"{INDENT}According to Kasiski examination, there are no possible key lengths.")
    # Starting to attempt an attack, using one of the derived key lengths.
    for counter, key_length in enumerate(possible_key_lengths):
        print(f"{INDENT}Attempt #{counter}: an attack using the key length of {colorize_text('DATA', key_length)}.")
        key = vigenere_attempt_attack(ciphertext, key_length)
        # If function returns a true value, then we probably have succeeded.
        if key:
            possible_keys.append(key)
            return possible_keys
    # If no keys are found, then we ask for starting a bruteforce attack.
    if not possible_keys:
        while True:
            start_bruteforce = yes_or_no("Unable to hack using the most possible key lengths. Do you want to start bruteforce?")
            if "ERROR" in start_bruteforce:
                continue
            elif start_bruteforce["data"] == "y":
                for counter, key_length in enumerate(range(2, MAX_KEY_LENGTH + 1)):
                    if key_length not in possible_key_lengths:
                        print(f"{INDENT}Attempt #{counter}: an attack using the key length of {colorize_text('DATA', key_length)}.")
                        key = vigenere_attempt_attack(ciphertext, key_length)
                        if key:
                            possible_keys.append(key)
                            return possible_keys
                break
            elif start_bruteforce["data"] == "n":
                break

    return possible_keys

def vigenere_manual():
    """
    The function, which returns the 
    Vigenere cipher manual.
    """

    delimiter = "=" * 66
    manual = f"""

{delimiter}
VIGENERE CIPHER MANUAL.
{delimiter}
Vigenere cipher is a polyalphabetic cryptosystem. The cipher uses
a series of Caesar ciphers, which is obtained from a chosen key.
Although Vigenere cipher was firstly invented by Giovan Battista
Bellaso in 1553, the cipher was misattributed to Blaise de
Vigenere in the 19th century.
{delimiter}
The mathematical model of this cipher is as the same as one of the
Caesar cipher, since, as noticed earlier, Vigenere cipher uses a
series of Caesar ciphers, according to a chosen key.
So, here is what we have:
Cᵢ = (Pᵢ + Kᵢ) mod N
Pᵢ = (Cᵢ - Kᵢ) mod N
where
    C = C₀ ... Cₙ is a ciphertext;
    P = P₀ ... Pₙ is a plaintext;
    K = K₀ ... Kₙ is a key;
    N is the length of an alphabet (26 for English).
    Subscript i (ᵢ) is the letter index in a text;
    Subscript n (ₙ) is the length of a text;
A keyword, chosen by a user, must be a string, consisting only of
letters. Then that string is going to be repeated (n / m) times,
making the final key, where n is the message length, and m is the
keyword length.
{delimiter}
Cryptanalysis.
You probably already know that this is impossible to apply only
frequency cryptanalysis to attack the cipher, because it uses
different monoalphabetic ciphers. But there is a vulnerability.
Since Cryptopia uses Kasiski Examination in order to perform a
cryptanalysis to this cipher, we will discuss this particular
technique. The method was first published by Friedrich Kasiski, a
German officer, in 1863. In fact, the method was discovered, but
not published, by Charles Babbage in 1846.

So, here are the steps of cryptanalysis.
1. Find the key length (Kasiski Examination).
2. Divide the ciphertext into groups of different Caesar ciphers,
(the number of Caesar ciphers = the key length), and use the
frequency cryptanalysis techniques to derive the plaintext.
3. Join the groups of text, which were decrypted at the second
step.

Kasiski Examination. Finding the key length.
1. Find repeated sequences of 3/more characters in a ciphertext.
2. Find the distances between every of the consecutive sequences.
3. Take the GCF (the greatest common factor) of all the distances.
Why does it work? We can have repeated sequences, since the key
letters can line up in the same way with the same words, and that
means that the distance between the words must be a multiple of
the keyword length, unless it is a coincidence.
"""
    manual = f"\n{INDENT}".join((manual.split("\n")))
    return manual