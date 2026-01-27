from math import floor
from utils import typed


def calculate_splits(data):
    """
    Calculates the time per 500m from the data provided 
    Time(s) / (distance / 500)
    Converts result into readable time format
    """
    distance = 2000 # If more distances allowed in future, this will become a user input on data.py so will need importing
    calc_split = data / (distance / 500)
    split_mins = floor(calc_split / 60)
    split_secs = round(calc_split - (split_mins * 60), 1)
    user_split = f"Your split time is: {split_mins}:{str(split_secs).zfill(4)}\n"
    typed(user_split)

    return calc_split


def calculate_watts(data):
    """
    Converts split times into watts
    2.8 / (split(s) / 500)^3
    Rounds to nearest int as per 
    """
    watts = round(2.8 / (data / 500)**3)
    typed(f"Your watts generated are: {watts}")
    print("\n")
    typed("Retrieving your ranking...\n")
    
    return watts