######################################################
##
## Data input module.
## This module defines all the functions, which are
## responsible for getting data from input.
##
######################################################

## Standard modules.
from os.path import isfile

## Modules of the projects.
from modules.config import INDENT

def input_text():
    """
    The input field for some plaintext/ciphertext.
    """

    input_data = dict()

    text = input(f"{INDENT}Enter text: ").strip()
    
    # Handling incorrect input.
    if not text:
        input_data["ERROR"] = "incorrect_input"
    else:
        input_data["data"] = text
    
    return input_data

def input_parameter(parameter_name, data_type, number_range=range(0, 0), str_matches=[], only_letters=False):
    """
    The input field for some parameter, which is usually 
    a key or number.
    """

    input_data = dict()

    parameter = input(f"{INDENT}Enter {parameter_name}: ").strip()
    
    # Handling incorrect input.
    try:
        parameter = data_type(parameter)
    except:
        input_data["ERROR"] = "incorrect_input"
    else:
        if number_range:
            # If the number range is default (0, 0), then
            # the condition will not be satisfied.
            if parameter in number_range:
                input_data["data"] = parameter
            else:
                input_data["ERROR"] = "incorrect_input"
        elif str_matches:
            # If the list called str_matches (a list
            # containing only strings) is empty, then
            # the condition will not be satisfied.
            if parameter.lower() in list(map(lambda string: string.lower(), str_matches)):
                input_data["data"] = parameter.lower()
            else:
                input_data["ERROR"] = "incorrect_input"
        elif only_letters:
            # If the boolean value only_letters is False,
            # then the condition will not be satisfied.
            if parameter.isalpha():
                input_data["data"] = parameter
            else:
                input_data["ERROR"] = "incorrect_input"
    
    return input_data

def input_path(target):
    """
    The input field for a file path.
    """

    input_data = dict()

    # We use the target argument, because we have to specify 
    # what the file actually is.
    path = input(f"{INDENT}Enter the path to {target}: ").strip()
    
    # Handling incorrect input.
    if not path:
        input_data["ERROR"] = "incorrect_input"
    else:
        if not isfile(path):
            input_data["ERROR"] = "file_not_found"
        else:
            input_data["data"] = path
    
    return input_data

def yes_or_no(question):
    """
    The input field for a YES/NO question.
    """

    input_data = dict()

    y_or_n = input(f"{INDENT}{question} [Y/n]: ").lower().strip()
    
    # Handling incorrect input.
    if not y_or_n:
        input_data["ERROR"] = "incorrect_input"
    else:
        if y_or_n not in ["y", "n"]:
            input_data["ERROR"] = "incorrect_input"
        else:
            input_data["data"] = y_or_n
    
    return input_data

def get_input_data(input_fields):
    """
    Collects input data, using an array of the required 
    input fields.
    """

    input_data = dict()

    for input_field in input_fields:
        if not input_field:
            # We are assuming here that there are no
            # functions to call.
            return input_data

        # Calling a function with some arguments and 
        # recording received data to gotten_input.
        gotten_input = globals()[input_fields[input_field]["function"]](*input_fields[input_field]["arguments"])
        
        # Handling errors.
        if "ERROR" in gotten_input:
            input_data["ERROR"] = gotten_input["ERROR"]
            break

        input_data[input_field] = gotten_input["data"]

    return input_data