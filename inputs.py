"""
Collects user demographic and row performance inputs

All values are validated before being returned
"""


import utils
import validate


def get_age():
    """
    Collects user age data

    Returns:
        int: User age validated to be in the range 10-90
    """
    while True:
        utils.typed(" Please enter your age\n")
        user_age = input(" Age: ")
        print("")
        if validate.validate_age(user_age):
            break

    return int(user_age)


def get_gender():
    """
    Collects user gender data

    Returns:
        str: User gender validated to be either "f" or "m"
    """
    while True:
        utils.typed(" Please enter your gender: m/f\n")
        user_gender = input(" Gender: ")
        if validate.validate_gender(user_gender):
            break

    return user_gender


def get_row_time():
    """
    Collates user's inputted row times. Converts inputs into a
    readable string and and a float.

    Returns:
        tuple: (time_seconds (float), time_display (str))
            time_seconds: Row time in total seconds for further use
            time_display: User-friendly format mm:ss.d (eg 7:45.6)
    """
    utils.typed(
        " Please enter your latest 2k test time. Minutes, seconds, tenths\n"
        )
    minutes = get_time("minutes")
    seconds = get_time("seconds")
    tenths = get_tenths()
    # Use of zfill() inspired by reddit answer (link in credits)
    display_time = f"{minutes}:{seconds.zfill(2)}.{tenths}"
    time_as_seconds = (int(minutes) * 60) + int(seconds) + (int(tenths) / 10)

    return time_as_seconds, display_time


def get_time(time_unit):
    """
    Collects row duration time information from user

    Args:
        time_unit (str): unit of time to be collected

    Return:
        str: User's time input validated to be in the range 0-59
    """
    while True:
        user_time = input(f" {time_unit.capitalize()}: ")
        if validate.validate_time(user_time, time_unit):
            return user_time


def get_tenths():
    """
    Collects tenths portion of row time duration

    Returns:
        str: User's tenths input validated to be in the range 0-9
    """
    while True:
        user_tenths = input(" Tenths: ")
        if validate.validate_tenths(user_tenths):
            break

    return user_tenths
