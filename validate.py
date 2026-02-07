"""Handles all validation logic for user inputs."""


import utils


def validate_age(age):
    """
    Validates user's age input for type and range

    Args:
        age (str): User's age input to be tested

    Returns:
        bool: True if age input is an integer in range 10-90, otherwise False
    """
    try:
        if int(age) < 10 or int(age) > 90:
            utils.typed(
                " I'm sorry only ages between 10 and 90 can be accepted")
            print("\n")
            return False
    except ValueError:
        utils.typed(" Invalid age, please enter a number between 10 and 90")
        print("\n")
        return False

    return True


def validate_gender(gender):
    """
    Validates user's gender input for type and valid values

    Args:
        gender (str): User's gender input to be tested

    Returns:
        bool: True if gender input is "m", "M", "f" or "F",
            otherwise False
    """
    try:
        if gender.lower() != "f" and gender.lower() != "m":
            raise ValueError
    except ValueError:
        utils.typed(" Invalid entry, please enter either m or f")
        print("\n")
        return False

    return True


def validate_time(time, time_unit):
    """
    Validates user's time inputs for type and range

    Args:
        time (str): User's time input to be tested
        time_unit (str): Unit of time to be displayed in the error message,
            minutes or seconds

    Returns:
        bool: True if time input is an integer in range 0-59, otherwise False
    """
    try:
        if int(time) < 0 or int(time) > 59:
            raise ValueError
    except ValueError:
        utils.typed(
            f" Invalid entry, please enter a {time_unit}"
            " value between 0 and 59"
        )
        print("\n")
        return False

    return True


def validate_tenths(tenths):
    """
    Validates user's tenths input for type and range

    Args:
        tenths (str): User's tenths input to be tested

    Returns:
        bool: True if time input is an integer in range 0-9, otherwise False
    """
    try:
        if int(tenths) < 0 or int(tenths) > 9:
            raise ValueError
    except ValueError:
        utils.typed(
            " Invalid entry, please enter a tenths value between 0 and 9")
        print("\n")
        return False

    return True
