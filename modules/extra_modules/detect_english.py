##################################################
##
## Detect_english module
## This module defines the functions, which are
## responsible for detecting english words in a
## string.
##
##################################################

## Standard modules.
from string import ascii_letters

def load_dictionary():
    """
    Loads the dictionary with English words, which 
    we will use to detect English text in a string.
    """

    with open("modules/data/english_dictionary.txt") as file:
        english_words = []
        for word in file.read().split("\n"):
            english_words.append(word.upper())
    return english_words

ENGLISH_WORDS = load_dictionary()

def remove_non_letters(text, delete_spaces="no"):
    """
    Removes all the chars from a string, which are
    not letters (or spaces).
    """
    
    letters_and_space = ascii_letters + " \t\n"
    
    letters = []
    for char in text:
        if delete_spaces == "no":
            if char in letters_and_space:
                letters.append(char)
        else:
            if char in ascii_letters:
                letters.append(char)
    return "".join(letters)

def english_word_probability(text):
    """
    Calculates the probability of an English word
    in text.
    """

    possible_words = remove_non_letters(text.upper()).split()
    if not possible_words:
        return 0.0
    matches = 0
    for word in possible_words:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possible_words)

def is_english(text, word_percentage=20, letter_percentage=85):
    """
    Usually, 20% of the words in a string exists
    in our dictionary. Also, by default, 85% of
    the characters in a string must be letters or
    spaces.
    """

    words_match = (english_word_probability(text) * 100) >= word_percentage
    message_letters_percentage = float(len(remove_non_letters(text))) / len(text) * 100
    letters_match = message_letters_percentage >= letter_percentage
    return (words_match and letters_match)