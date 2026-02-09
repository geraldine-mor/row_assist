"""
Utility functions for user interaction and display formatting.

Primary functions are typewriter effects, ASCII graphics,
terminal clearing and exit handling.
"""


import time
import os


def clear_terminal():
    """Clears the terminal to begin a new session."""
    # Copied code, source - https://stackoverflow.com/a/2084628
    os.system('cls' if os.name == 'nt' else 'clear')


def typed(string):
    """
    Creates a typewriter effect for the text display.

    Args:
        string (str): text to be displayed to user
    """
    # Code derived from Stack Overflow - (link in credits)
    for i in string:
        print(i, end="", flush=True)
        time.sleep(0.03)


def display_header():
    """Displays the Row Assist title banner"""
    print("""
 ██████╗  ██████╗ ██╗    ██╗    █████╗ ███████╗███████╗██╗███████╗████████╗
 ██╔══██╗██╔═══██╗██║    ██║   ██╔══██╗██╔════╝██╔════╝██║██╔════╝╚══██╔══╝
 ██████╔╝██║   ██║██║ █╗ ██║   ███████║███████╗███████╗██║███████╗   ██║
 ██╔══██╗██║   ██║██║███╗██║   ██╔══██║╚════██║╚════██║██║╚════██║   ██║
 ██║  ██║╚██████╔╝╚███╔███╔╝   ██║  ██║███████║███████║██║███████║   ██║
 ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚══════╝   ╚═╝
    """)  # Title artwork created with claude.ai


def check_wr(time):
    """
    Compares user's row time value (in seconds) to world record time.
    Displays humorous message to the user.

    Args:
        time (float): user's row time parsed into total seconds
    """
    if time < 335.8:  # Correct as of 28/1/26 (set in 2018)
        typed(" ⚡Greetings Barry Allen!⚡\n")
        typed(" The fastest 2k ever recorded is 5:35.8 and you smashed it!")
        print("\n")


def display_rowing_image():
    """Displays the rowing machine ASCII artwork as a closing graphic"""
    time.sleep(0.7)
    print("""
                   .:==:
                  .=@@@@=
                   =@@@@#.
                  .=@@@@:
                 :@@@%:              =@@:
                =@@@@@@*:.           =@@%:
               :@@@@@@@ @@%-:.       -%%=.
               *@@@@@@    *@@@%=        =%     .:@:.
              .%@@@@@=     .  *#@@@+      =%  %@@@@@%-
              :%@@@@*:-=*%@@@*:   *+===    .%@@@@@@@@@*.
              =@@@@@@@@@@@@@@@*.       *===+@@@@@@@@@@%-
              *@@@@@@@@@@+:+@@@=           =@@@@@@@@@@%-
              -%@@@@@%+:.  :*@@%:         .=@@@@@@@@@@=
            .+%%@@@@@%=.    .+@@#.  :+.:*%@@@**@@@@@=:
     .........::*@@#::........*@@%@@@%@@@%=.    =%+
    +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:        :%*
    =@=::::::::::::::::::::::::-%@@@%-           #%
    +#:                      :=**=.              +@
  .:*#=------------------------------------------+@=---:
  .-===================================================:
    """, end="")  # Created with asciiart.eu


def program_exit():
    """
    Determines whether to exit the program and gives farewell message

    Returns:
        bool: True if user enters "x" when prompted
    """
    typed(" Do you wish to exit now or restart?\n")
    exit_command = input(
        " Press 'x' to exit, press any other key to restart: ")
    if exit_command.lower() == "x":
        typed(" Exiting Row Assist, Goodbye\n")
        display_rowing_image()
        return True
