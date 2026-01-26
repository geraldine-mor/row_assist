import time

def typed(string):
    """
    Creates a typed effect for the text 
    """
    for i in string:
        print(i, end="", flush=True)
        time.sleep(0.03)