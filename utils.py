import time

def typed(string):
    """
    Creates a typed effect for the text 
    """
    for i in string:
        print(i, end="", flush=True)
        time.sleep(0.03)


def check_wr(data):
    """
    Compares entered time value to current world record and returns
    humorous message
    """
    if data < 335.8:
        typed("Greeting Barry Allen!\n")
        typed("The fastest 2k ever recorded is 5:35.8 and you smashed it!")
        print("\n")        