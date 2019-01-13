######################################################
##
## Config module.
## This module contains the entire configuration of
## Cryptopia: some constants, commands, functions,
## the general data about the project and so on.
##
######################################################

## Standard modules.
from random import choice
from itertools import chain

## Third-party modules.
from colorama import Fore

# The text for input field.
INPUT_LABEL = "[cryptopia] > "

# Identation for output strings.
INDENT = " " * len(INPUT_LABEL)

## The settings of colors.

COLOR_STYLES = {
    "REGULAR_TEXT": Fore.LIGHTGREEN_EX,
    "ERROR": Fore.LIGHTRED_EX,
    "RESULT": Fore.LIGHTYELLOW_EX,
    "DATA": Fore.LIGHTCYAN_EX,
    # All other colors from the colorama module:
    "BLACK": Fore.LIGHTBLACK_EX,
    "BLUE": Fore.LIGHTBLUE_EX,
    "MAGENTA": Fore.LIGHTMAGENTA_EX,
    "WHITE": Fore.LIGHTWHITE_EX,
}

def colorize_text(color, text):
    """
    Colorizes a text in a chosen color.
    """

    return f"{COLOR_STYLES[color]}{text}{COLOR_STYLES['REGULAR_TEXT']}"

## The main information about the project and the author's contacts.
PROJECT_NAME = "Cryptopia"
VERSION = "1.3 CLI"
AUTHOR = "atlantis"

DESCRIPTION = """Cryptopia is a cryptologic utility, which is going to help you to work
with some encryption methods, explore interesting ciphers and hash
functions, do cryptanalysis using common techniques of breaking
cryptosystems, and have fun. Cryptopia is beautiful and user-friendly 
tool made with love. So, hopefully, it will be useful for you and you
will really like it.
Good luck in use!"""

GITHUB = "https://github.com/atlanntiss"
EMAIL = "cryptofri3nd@tutanota.com"

# The text for the "info" command.
delimiter = "=" * 73
INFO_TEXT = f"""
{delimiter}
DATA ABOUT CRYPTOPIA.
{delimiter}
Release: {PROJECT_NAME} {VERSION}.
Author:  {AUTHOR}.
{delimiter}
{DESCRIPTION}
{delimiter}
CONTACTS
{delimiter}
GitHub:\t{GITHUB}
Email:\t{EMAIL}
{delimiter}
"""
INFO_TEXT = colorize_text("DATA", f"\n{INDENT}".join(INFO_TEXT.split("\n")))

## The settings of commands.

SERVICE_COMMANDS = {
    "help": {
        "command_name": "help",
        "description": "shows the help text and the list of the commands",
    },
    "info": {
        "command_name": "info",
        "description": "shows the general information about Cryptopia",
    },
    "clear": {
        "command_name": "clear",
        "description": "clears the console screen of any output",
    },
    "quit": {
        "command_name": "quit",
        "description": "quits the application",
    },
}

CIPHERS = {
    "section_name": "CIPHERS",
    "functions": {
        "caesar": {
            # Every function has its mode, so we need to specify it.
            "encrypt": {
                # These are input fields with arguments in the arrays below.
                "text": {
                    "function": "input_text",
                    "arguments": [],
                },
                "key": {
                    "function": "input_parameter",
                    "arguments": ["a key (0 < integer < 26)", int, range(1, 26)],
                },
            },
            "decrypt": {
                "text": {
                    "function": "input_text",
                    "arguments": [],
                },
                "key": {
                    "function": "input_parameter",
                    "arguments": ["a key (0 < integer < 26)", int, range(1, 26)],
                },
            },
            "crack": {
                "text": {
                    "function": "input_text",
                    "arguments": [],
                },
            },
            "man": {
                None,
            },
        },
    },
}

CRACKING = {
    "section_name": "CRACKING",
    "functions": (
        "caesar",
    )
}

HASHING = {
    "section_name": "HASHING",
    "functions": {
        "md4": {
            # Every function has its mode, so we need to specify it.
            "hash_str": {
                # These are input fields with arguments in the arrays below.
                "text": {
                    "function": "input_text",
                    "arguments": [],
                },
                "salt_y_or_n": {
                    "function": "yes_or_no",
                    "arguments": ["Do you want to use a salt (suffixed), which was randomly generated?"],
                },
            },
            "hash_file": {
                "file": {
                    "function": "input_path",
                    "arguments": ["the file whose checksum you want to find"],
                },
            },
        },
        "md5": {
            "hash_str": {
                "text": {
                    "function": "input_text",
                    "arguments": [],
                },
                "salt_y_or_n": {
                    "function": "yes_or_no",
                    "arguments": ["Do you want to use a salt (suffixed), which was randomly generated?"],
                },
            },
            "hash_file": {
                "file": {
                    "function": "input_path",
                    "arguments": ["the file whose checksum you want to find"],
                },
            },
        },
        "sha1": {
            "hash_str": {
                "text": {
                    "function": "input_text",
                    "arguments": [],
                },
                "salt_y_or_n": {
                    "function": "yes_or_no",
                    "arguments": ["Do you want to use a salt (suffixed), which was randomly generated?"],
                },
            },
            "hash_file": {
                "file": {
                    "function": "input_path",
                    "arguments": ["the file whose checksum you want to find"],
                },
            },
        },
        "sha224": {
            "hash_str": {
                "text": {
                    "function": "input_text",
                    "arguments": [],
                },
                "salt_y_or_n": {
                    "function": "yes_or_no",
                    "arguments": ["Do you want to use a salt (suffixed), which was randomly generated?"],
                },
            },
            "hash_file": {
                "file": {
                    "function": "input_path",
                    "arguments": ["the file whose checksum you want to find"],
                },
            },
        },
        "sha256": {
            "hash_str": {
                "text": {
                    "function": "input_text",
                    "arguments": [],
                },
                "salt_y_or_n": {
                    "function": "yes_or_no",
                    "arguments": ["Do you want to use a salt (suffixed), which was randomly generated?"],
                },
            },
            "hash_file": {
                "file": {
                    "function": "input_path",
                    "arguments": ["the file whose checksum you want to find"],
                },
            },
        },
        "sha384": {
            "hash_str": {
                "text": {
                    "function": "input_text",
                    "arguments": [],
                },
                "salt_y_or_n": {
                    "function": "yes_or_no",
                    "arguments": ["Do you want to use a salt (suffixed), which was randomly generated?"],
                },
            },
            "hash_file": {
                "file": {
                    "function": "input_path",
                    "arguments": ["the file whose checksum you want to find"],
                },
            },
        },
        "sha512": {
            "hash_str": {
                "text": {
                    "function": "input_text",
                    "arguments": [],
                },
                "salt_y_or_n": {
                    "function": "yes_or_no",
                    "arguments": ["Do you want to use a salt (suffixed), which was randomly generated?"],
                },
            },
            "hash_file": {
                "file": {
                    "function": "input_path",
                    "arguments": ["the file whose checksum you want to find"],
                },
            },
        },
    },
}

ALL_FUNCTIONS = {
    "ciphers": CIPHERS, 
    "cracking": CRACKING, 
    "hashing": HASHING,
}

MAIN_COMMANDS = {
    "encrypt": {
        "functions": CIPHERS["functions"],
        "description": f"works with {CIPHERS['section_name']} section (encryption)",
    },
    "decrypt": {
        "functions": CIPHERS["functions"],
        "description": f"works with {CIPHERS['section_name']} section (decryption)",
    },
    "crack": {
        "functions": CRACKING["functions"],
        "description": f"works with {CRACKING['section_name']} section (cryptanalysis)",
    },
    "hash_str": {
        "functions": HASHING["functions"],
        "description": f"works with {HASHING['section_name']} section (string hashing)",
    },
    "hash_file": {
        "functions": HASHING["functions"],
        "description": f"works with {HASHING['section_name']} section (file hashing)",
    },
    "man": {
        "functions": list(chain(*[section["functions"] for section in list(ALL_FUNCTIONS.values())])),
        "description": f"works with all the sections (manual)",
    },
}

## Setting up the help text.

# The text, which explains how to use commands.
ABOUT_SYNTAX = """The format of service commands:
    command
The format of main commands:
    command function

A correctly entered command will be accepted whether it was written
in the uppercase or lowercase style.

Examples of queries:
  info
  encrypt caesar
  clear
  crack caesar"""

# Preparing some lists of commands/functions to output.

main_commands_output = list()
for key, value in MAIN_COMMANDS.items():
    main_commands_output.append(f"  {key: <10} - {value['description']}.")
MAIN_COMMANDS_OUTPUT = "\n".join(main_commands_output)

functions_output = list()
for section in list(ALL_FUNCTIONS.values()):
    functions_output.append(f"\n{section['section_name']}:")
    for function in section["functions"]:
        functions_output.append(f"  {function}")
FUNCTIONS_OUTPUT = "\n".join(functions_output)

service_commands_output = list()
for key, value in SERVICE_COMMANDS.items():
    service_commands_output.append(f"  {key: <5} - {value['description']}.")
SERVICE_COMMANDS_OUTPUT = "\n".join(service_commands_output)

# The help text. Here it is!
delimiter = "=" * 69
HELP_TEXT = f"""
{delimiter}
CRYPTOPIA MANUAL.
{delimiter}
SYNTAX.
{delimiter}
{ABOUT_SYNTAX}
{delimiter}
MAIN COMMANDS.
{delimiter}
{MAIN_COMMANDS_OUTPUT}
{delimiter}
FUNCTIONS.
{delimiter}{FUNCTIONS_OUTPUT}
{delimiter}
SERVICE COMMANDS.
{delimiter}
{SERVICE_COMMANDS_OUTPUT}
{delimiter}
"""
HELP_TEXT = colorize_text("DATA", f"\n{INDENT}".join(HELP_TEXT.split("\n")))

## Headers.

BIG = """   _____                  _              _       
  / ____|                | |            (_)      
 | |     _ __ _   _ _ __ | |_ ___  _ __  _  __ _ 
 | |    | '__| | | | '_ \| __/ _ \| '_ \| |/ _` |
 | |____| |  | |_| | |_) | || (_) | |_) | | (_| |
  \_____|_|   \__, | .__/ \__\___/| .__/|_|\__,_|
               __/ | |            | |            
              |___/|_|            |_|            """

BIG_MONEY = """  /$$$$$$                                  /$$                         /$$          
 /$$__  $$                                | $$                        |__/          
| $$  \__/  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$  /$$  /$$$$$$ 
| $$       /$$__  $$| $$  | $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$| $$ |____  $$
| $$      | $$  \__/| $$  | $$| $$  \ $$  | $$    | $$  \ $$| $$  \ $$| $$  /$$$$$$$
| $$    $$| $$      | $$  | $$| $$  | $$  | $$ /$$| $$  | $$| $$  | $$| $$ /$$__  $$
|  $$$$$$/| $$      |  $$$$$$$| $$$$$$$/  |  $$$$/|  $$$$$$/| $$$$$$$/| $$|  $$$$$$$
 \______/ |__/       \____  $$| $$____/    \___/   \______/ | $$____/ |__/ \_______/
                     /$$  | $$| $$                          | $$                    
                    |  $$$$$$/| $$                          | $$                    
                     \______/ |__/                          |__/                    """

EPIC = """ _______  _______           _______ _________ _______  _______ _________ _______ 
(  ____ \(  ____ )|\     /|(  ____ )\__   __/(  ___  )(  ____ )\__   __/(  ___  )
| (    \/| (    )|( \   / )| (    )|   ) (   | (   ) || (    )|   ) (   | (   ) |
| |      | (____)| \ (_) / | (____)|   | |   | |   | || (____)|   | |   | (___) |
| |      |     __)  \   /  |  _____)   | |   | |   | ||  _____)   | |   |  ___  |
| |      | (\ (      ) (   | (         | |   | |   | || (         | |   | (   ) |
| (____/\| ) \ \__   | |   | )         | |   | (___) || )      ___) (___| )   ( |
(_______/|/   \__/   \_/   |/          )_(   (_______)|/       \_______/|/     \|
                                                                                 """

FIRE_FONT = """                                                    
   (                         )                      
   )\   (    (            ( /(            (      )  
 (((_)  )(   )\ )  `  )   )\()) (   `  )  )\  ( /(  
 )\___ (()\ (()/(  /(/(  (_))/  )\  /(/( ((_) )(_)) 
((/ __| ((_) )(_))((_)_\ | |_  ((_)((_)_\ (_)((_)_  
 | (__ | '_|| || || '_ \)|  _|/ _ \| '_ \)| |/ _` | 
  \___||_|   \_, || .__/  \__|\___/| .__/ |_|\__,_| 
             |__/ |_|              |_|              """

MODULAR = """ _______  ______    __   __  _______  _______  _______  _______  ___   _______ 
|       ||    _ |  |  | |  ||       ||       ||       ||       ||   | |   _   |
|       ||   | ||  |  |_|  ||    _  ||_     _||   _   ||    _  ||   | |  |_|  |
|       ||   |_||_ |       ||   |_| |  |   |  |  | |  ||   |_| ||   | |       |
|      _||    __  ||_     _||    ___|  |   |  |  |_|  ||    ___||   | |       |
|     |_ |   |  | |  |   |  |   |      |   |  |       ||   |    |   | |   _   |
|_______||___|  |_|  |___|  |___|      |___|  |_______||___|    |___| |__| |__|"""


SOFT = """                                                                 
 ,-----.                        ,--.                ,--.         
'  .--./,--.--.,--. ,--.,---. ,-'  '-. ,---.  ,---. `--' ,--,--. 
|  |    |  .--' \  '  /| .-. |'-.  .-'| .-. || .-. |,--.' ,-.  | 
'  '--'\|  |     \   ' | '-' '  |  |  ' '-' '| '-' '|  |\ '-'  | 
 `-----'`--'   .-'  /  |  |-'   `--'   `---' |  |-' `--' `--`--' 
               `---'   `--'                  `--'                """

STAR_WARS = """  ______ .______     ____    ____ .______   .___________.  ______   .______    __       ___      
 /      ||   _  \    \   \  /   / |   _  \  |           | /  __  \  |   _  \  |  |     /   \     
|  ,----'|  |_)  |    \   \/   /  |  |_)  | `---|  |----`|  |  |  | |  |_)  | |  |    /  ^  \    
|  |     |      /      \_    _/   |   ___/      |  |     |  |  |  | |   ___/  |  |   /  /_\  \   
|  `----.|  |\  \----.   |  |     |  |          |  |     |  `--'  | |  |      |  |  /  _____  \  
 \______|| _| `._____|   |__|     | _|          |__|      \______/  | _|      |__| /__/     \__\ 
                                                                                                 """

ANSI_SHADOW = """ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ██████╗ ██╗ █████╗ 
██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗
██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║██████╔╝██║███████║
██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║██╔═══╝ ██║██╔══██║
╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝██║     ██║██║  ██║
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝
                                                                      """

O8 = """  oooooooo8                                     o8                       o88              
o888     88 oo oooooo  oooo   oooo ooooooooo  o888oo ooooooo  ooooooooo  oooo   ooooooo   
888          888    888 888   888   888    888 888 888     888 888    888 888   ooooo888  
888o     oo  888         888 888    888    888 888 888     888 888    888 888 888    888  
 888oooo88  o888o          8888     888ooo88    888o 88ooo88   888ooo88  o888o 88ooo88 8o 
                        o8o888     o888                       o888                        """

NANCYJ_UNDERLINED = """ a88888b.                               dP                      oo          
d8'   `88                               88                                  
88        88d888b. dP    dP  88d888b. d8888P .d8888b.  88d888b. dP .d8888b. 
88        88'  `88 88    88  88'  `88   88   88'  `88  88'  `88 88 88'  `88 
Y8.   .88 88       88.  .88  88.  .88   88   88.  .88  88.  .88 88 88.  .88 
 Y88888P' dP       `8888P88  88Y888P'   dP   `88888P'  88Y888P' dP `88888P8 
oooooooooooooooooooo~~~~.88~~88~oooooooooooooooooooooo~88~oooooooooooooooooo
                    d8888P   dP                        dP                   """

HEADERS = [
    O8,
    BIG,
    SOFT,
    EPIC,
    MODULAR,
    STAR_WARS,
    BIG_MONEY,
    FIRE_FONT,
    ANSI_SHADOW,
    NANCYJ_UNDERLINED
]

# Colorizing the headers.
for header_number, header in enumerate(HEADERS):
    header_chars = list(header)
    for char_number, char in enumerate(header_chars):
        header_chars[char_number] = colorize_text(choice(list(COLOR_STYLES.keys())), char)
    HEADERS[header_number] = "".join(header_chars)