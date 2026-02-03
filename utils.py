import time


def typed(string):
    """
    Creates a typewriter effect for the text
    Iterates through the string printing one letter at a time,
    horizontally and immediately with a 0.03s time delay
    """
    for i in string:
        print(i, end="", flush=True)
        time.sleep(0.03)


def display_header():
    """
    Display the Row Assist title banner
    """
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
    Compares entered time value (in seconds) to world record and
    returns humorous message if the user enters a time faster than
    the world record
    """
    if time < 335.8:  # Correct as of 28/1/26 (set in 2018)
        typed(" Greetings Barry Allen!\n")
        typed(" The fastest 2k ever recorded is 5:35.8 and you smashed it!")
        print("\n")


def display_rowing_image():
    """
    Display the rowing machine ASCII artwork as a closing graphic
    """
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
    Asks user if they would like to exit or restart
    Exit commands triggers exit, restart triggers main()
    """
    typed(" Do you wish to exit now or restart?\n")
    exit_command = input(
        " Press 'x' to exit, press any other key to restart: ")
    if exit_command.lower() == "x":
        typed(" Exiting Row Assist, Goodbye\n")
        display_rowing_image()
        return True
