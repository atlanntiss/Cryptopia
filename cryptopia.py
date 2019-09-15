#!/usr/bin/env python3

###############################################
##
## Cryptopia version 2.0 CLI
## Author: atlantis
## GitHub: https://github.com/atlanntiss
## Cryptopia is a cryptologic tool, which
## is going to help you to work with ciphers
## and simple cryptanalysis.
##
###############################################

## Standard modules.
from sys import stdout
from time import sleep
from random import randint, choice
from os import system, name as os_name

## Modules of the project.
from modules.main_functions.hashing import *
from modules.main_functions.crypto import *
from modules.config import (PROJECT_NAME, VERSION, SERVICE_COMMANDS,
                            MAIN_COMMANDS, INDENT, INPUT_LABEL, HEADERS, 
                            HELP_TEXT, INFO_TEXT, ERRORS, colorize_text)

## Third-party modules.
from colorama import init as colors_init

class Interface:
    """
    The main user interface class.
    """

    def __init__(self):
        """
        The initial actions and starting the main loop of the program.
        """

        colors_init()
        self.clear()
        
        print(choice(HEADERS))
        print(f"\n{PROJECT_NAME}. Version: {VERSION}.")
        print("=" * 62)
        print(f"Enter {colorize_text('DATA', SERVICE_COMMANDS['help']['command_name'])} to get help and see the list of all the commands.")
        print(f"Enter {colorize_text('DATA', SERVICE_COMMANDS['info']['command_name'])} to get more information about Cryptopia.")
        print(f"Enter {colorize_text('DATA', SERVICE_COMMANDS['quit']['command_name'])} to exit from Cryptopia.")
        print("=" * 62)

        self.loop = True
        self.main_loop()
    
    def __del__(self):
        """
        The final output before closing the application.
        """

        print()
        for char in f"Bye and see you soon in {PROJECT_NAME}! Glory to Cryptography!":
            stdout.write(char)
            stdout.flush()
            sleep(randint(40, 100) / 3500)
        stdout.write("\n")
    
    def main_loop(self):
        """
        The main loop of the program through which you enter commands
        and get result output.
        """

        while self.loop:
            choice = input(INPUT_LABEL).strip().lower().split()
            if choice:
                if len(choice) == 1:
                    # It is assumed that a single word command is 
                    # something like "help", "quit", "info", and 
                    # so on (service commands).
                    if choice[0] in SERVICE_COMMANDS:
                        # If an entered service function exists, 
                        # we call it.
                        getattr(self, choice[0])()
                    else:
                        print(self.return_error("cmd_not_found"))
                elif (len(choice) == 2) and (choice[0] in MAIN_COMMANDS):
                    # A 2-words-command must be something from MAIN_COMMANDS.
                    if choice[1] in MAIN_COMMANDS[choice[0]]["functions"]:
                        # If the input is correct, we call the function 
                        # from globals.
                        output_data = globals()[choice[1]](choice[0])
                        # Checking for any errors.
                        if "ERROR" in output_data:
                            print(self.return_error(output_data["ERROR"]))
                        else:
                            print(self.return_result(output_data))
                    else:
                        print(self.return_error("func_not_found"))
                else:
                    print(self.return_error("cmd_not_found"))
            else:
                # The input is empty.
                pass
    
    def return_result(self, output_data):
        """
        Returns a beautiful result based on provided 
        output_data.
        """

        output = []
        # Determining the maximum word length among
        # other result titles in output_data to choose 
        # the best number of spaces way to format output.
        space_length = max(list(map(lambda string: len(string), output_data.keys())))
        for key, value in output_data.items():
            output.append(f"{INDENT}[+] {key.capitalize(): <{space_length}}: {colorize_text('RESULT', value)}")
        return "\n".join(output)
    
    def return_error(self, reason):
        """
        Returns an error message based on a specific reason.
        """

        return colorize_text("ERROR", f"{INDENT}[!] ERROR: {ERRORS[reason]}.")
    
    def quit(self):
        """
        Just closes the main loop => closes the application.
        """

        self.loop = False
    
    def help(self):
        """
        Returns the reference.
        """

        print(HELP_TEXT)
    
    def info(self):
        """
        Returns the general information about the program.
        """

        print(INFO_TEXT)
    
    def clear(self):
        """
        Clears the console window of any commands and output.
        """

        command = "clear"
        if os_name == "nt":
            command = "cls"
        system(command)

def main():
    """
    The main function with creating the main object.
    """

    try:
        cryptopia_cli = Interface()
    except KeyboardInterrupt:
        # Catching the CTRL+C hotkey.
        print("\n\nKeyboard interrupt...")
    except Exception as error:
        # Catching any other unexpected exceptions.
        print(f"\nAn unexpected error: {error}.")

if __name__ == "__main__":
    # If the app file was launched as the main file, the main 
    # function will be started.
    main()
