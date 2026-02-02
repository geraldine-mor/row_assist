import utils


def validate_age(age):
    """
    Inside the try, converts age to an integer.
    Raises ValueError if string cannot be converted into int
    Raises TypeError if age falls outside the range 10-90
    """
    try:
        if int(age) < 10 or int(age) > 90:
            raise TypeError
    except ValueError:
        utils.typed("Invalid age, please enter a number between 10 and 90")
        print("\n")
        return False
    except TypeError:
        utils.typed("I'm sorry only ages between 10 and 90 can be accepted")
        print("\n")
        return False

    return True


def validate_gender(gender):
    """
    Inside the try, checks for m or f character.
    Raises ValueError if any other character is entered
    """
    try:
        if gender.lower() != "f" and gender.lower() != "m":
            raise ValueError
    except ValueError:
        utils.typed("Invalid entry, please enter either m or f")
        print("\n")
        return False

    return True


def validate_time(time, string):
    """
    Inside the try, converts time to integer
    Raises ValueError if the string can't be converted or if minutes
    fall ouside the range 0-59
    """
    try:
        if int(time) < 0 or int(time) > 59:
            raise ValueError
    except ValueError:
        utils.typed(
            f"Invalid entry, please enter a {string} value between 0 and 59")
        print("\n")
        return False

    return True


def validate_tenths(tenths):
    """
    Inside the try, converts time to integer
    Raises ValueError if the string can't be converted or if tenths
    fall ouside the range 0-9
    """
    try:
        if int(tenths) < 0 or int(tenths) > 9:
            raise ValueError
    except ValueError:
        utils.typed(
            "Invalid entry, please enter a tenths value between 0 and 9")
        print("\n")
        return False

    return True
