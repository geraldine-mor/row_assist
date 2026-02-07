"""
Performs rowing performance calculations.

Calculates user age, split times and watts from user inputs.
"""


from math import floor
from datetime import date


def calculate_splits(seconds, distance):
    """
    Calculates time per 500m and formats it to meet user expectations

    Args:
        seconds (float): total duration in seconds of the user's 2k test
        distance (int): distance rowed (currently only 2000m supported)

    Returns:
        tuple: (split_seconds (float), formatted_split (str))
            split_seconds: Split time in total seconds for further use
            formatted_split: User-friendly format mm:ss.d (eg "1:56.4")
    """
    calc_split = seconds / (distance / 500)
    split_mins = floor(calc_split / 60)
    split_secs = round(calc_split - (split_mins * 60), 1)
    # zfill(4) ensure consistent mm.d format (eg "05.2" not "5.2")
    user_split = f"{split_mins}:{str(split_secs).zfill(4)}"

    return calc_split, user_split


def calculate_watts(split):
    """
    Converts split time into watts

    Args:
        split (float): Time in seconds per 500m from user row data

    Returns:
        int: Watts (rounded to nearest int as per row erg screen feedback)
    """
    # Formula taken from https://www.concept2.com/ (full link in credits)
    calc_watts = round(2.8 / (split / 500)**3)
    return calc_watts


def calculate_age(DOB):
    """
    Calculates user's age today

    Args:
        DOB (datetime.date): User's date of birth from USER (dict)

    Returns:
        int: User's age rounded down to return whole years only
    """
    age_diff = (date.today() - DOB).days
    user_age = floor(age_diff / 365)

    return user_age
