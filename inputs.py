import utils
import validate


def get_age():
    """
    Get user age data
    Run a while loop to get valid data from the user
    """
    while True:
        utils.typed("Please enter your age\n")
        user_age = input("Age: ")
        print("")  # Create a single line space, print("\n") was causing 2
        if validate.validate_age(user_age):
            break

    return user_age


def get_gender():
    """
    Get user gender data
    Run a while loop to get valid data from the user
    """
    while True:
        utils.typed("Please enter your gender: m/f\n")
        user_gender = input("Gender: ")
        print("")
        if validate.validate_gender(user_gender):
            break

    return user_gender


def get_row_time():
    """
    Compile valid input times
    Convert inputs into a readable string and and a computable float
    """
    utils.typed(
        "Please enter your latest 2k test time. Minutes, seconds, tenths\n"
        )
    minutes = get_time("minutes")
    seconds = get_time("seconds")
    tenths = get_tenths()
    display_time = f"{minutes}:{seconds.zfill(2)}.{tenths}"

    utils.typed(f"You entered: {display_time}")
    print("\n")
    time_as_seconds = (int(minutes) * 60) + int(seconds) + (int(tenths) / 10)
    utils.check_wr(time_as_seconds)
    utils.typed("Calculating your scores...\n")

    return time_as_seconds


def get_time(string):
    """
    Get time values from user for latest row
    Run a while loop to get valid data from the user
    """
    while True:
        user_time = input(f"{string.capitalize()}: ")
        if validate.validate_time(user_time):
            return user_time


def get_tenths():
    """
    Get tenths value for latest row
    Run a while loop to get valid data from the user
    """
    while True:
        user_tenths = input("Tenths: ")
        if validate.validate_tenths(user_tenths):
            break

    return user_tenths
