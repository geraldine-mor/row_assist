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


def check_wr(time):
    """
    Compares entered time value (in seconds) to world record and
    returns humorous message if the user enters a time faster than
    the world record
    """
    if time < 335.8:  # Correct as of 28/1/26 (set in 2018)
        typed("Greeting Barry Allen!\n")
        typed("The fastest 2k ever recorded is 5:35.8 and you smashed it!")
        print("\n")
        