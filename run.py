"""Entry point and controller for the Row Assist application"""


from utils import *
import inputs
import calc
import ref_data
from datetime import date
from gspread.exceptions import GSpreadException
from google.auth.exceptions import GoogleAuthError


def get_user():
    """Returns dict of user information"""
    USER = {
        "login": "demo",
        "DOB": date(2000, 1, 14),
        "gender": "m"
    }
    return USER


def check_user(user):
    """
    Selects user mode and obtains demographic data

    Prompts user for login. If recognised, retrieves stored data.
    If empty str, proceeds as guest and prompts for age/gender inputs.

    Args:
        user (dict): persistent user information

    Returns:
        tuple: (age (int), gender (str), login (str or bool))
            age: user's age in years
            gender: "m" or "f"
            login: username string if persistent user, False if guest
    """
    while True:
        user_login = input(" Login: ")
        if user_login.lower() == user["login"]:
            user_age = calc.calculate_age(user["DOB"])
            user_gender = user["gender"]
            typed(" Welcome back!\n")
            return user_age, user_gender, user_login
        elif user_login == "":
            print("")
            typed(
                " You will soon be asked for your age, "
                "gender and your latest 2k test time.\n"
            )
            typed(
                " I will calculate your split time and watts "
                "and provide you with a ranking."
            )
            print("\n")
            age = inputs.get_age()
            gender = inputs.get_gender()
            return age, gender, False
        elif user_login.lower() != user["login"] and user_login != "":
            typed(
                " I'm sorry that login is not recognised, please try again\n"
                " or press 'Enter' to continue as a guest.\n"
            )
            continue


def main():
    """
    Controls the main program flow from user input to feedback.

    Manages calls to input collection, metric calculation and performance
    evaluating functions. Handles API/connection and data errors gracefully.
    """
    clear_terminal()
    display_header()
    print("Please avoid typing until instructed to do so.")

    typed(
        " Welcome to Row Assist, your indoor rowing assistant."
    )
    print("\n")
    typed(
        " Please enter your login or press 'Enter' to continue as a guest.\n"
    )

    USER = get_user()
    age, gender, user_login = check_user(USER)
    # Added to allow functions to run correctly if more distances added
    distance = 2000
    print("")
    row_time, display_time = inputs.get_row_time()
    typed(f" You entered: {display_time}")
    print("\n")
    check_wr(row_time)
    typed(" Calculating your scores...\n")
    split_time, display_split = calc.calculate_splits(row_time, distance)
    typed(f" Your split time is: {display_split}\n")
    watts = calc.calculate_watts(split_time)
    typed(f" Your watts generated are: {watts}")
    print("\n")
    typed(" Retrieving your ranking, please wait...\n")

    try:
        SHEET = ref_data.spreadsheet_connect()
        category = ref_data.lookup_category(
            age, gender, distance, watts, SHEET)
        category_description = ref_data.get_category_description(SHEET)
        typed(f" Your performance category is {category.title()}!\n")
        description = category_description[category]
        typed(
            f" You are: {description[0]}\n {description[1]}\n {description[2]}"
        )
        print("\n")
        ref_data.save_row_data(row_time, watts, user_login, SHEET)
    except (GSpreadException, GoogleAuthError):
        typed(
            " Apologies, the database is not available at this time.\n"
            " Please check your connection and try again later.\n"
            " If the problem persists, please contact customer support.\n"
        )
        print("")
    except Exception:
        typed(
            " I'm sorry, the program has encountered a problem and needs"
            " to close.\n If the problem persists, please contact customer"
            " support."
        )
        print("\n")


def run():
    """Handles main program run loop, allowing restart or clean exit."""
    while True:
        main()
        if program_exit():
            break


run()
