from utils import *
import inputs
import calc
import os
import ref_data
from datetime import date


USER = {
    "login": "demo",
    "DOB": date(2000, 1, 14),
    "gender": "m"
}


def check_user():
    """
    Requests and verifies user login, if verified, retrieves stored
    age and gender data. Alternatively offers the option to proceed
    as a guest user requesting the age and gender data.
    Function returns user age, gender and login
    """
    while True:
        user_login = input(" Login: ")
        if user_login.lower() == USER["login"]:
            user_age = calc.calculate_age(USER["DOB"])
            user_gender = USER["gender"]
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
        elif user_login.lower() != USER["login"] and user_login != "":
            typed(
            " I'm sorry that login is not recognised, please try again\n"
            " or press 'Enter' to continue as a guest.\n"
            )
            continue


def main():
    """
    Runs all functions
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    # Source - https://stackoverflow.com/a/2084628

    display_header()

    typed(
        " Welcome to Row Assist, your indoor rowing assistant."
    )
    print("\n")
    typed(
        " Please enter your login or press 'Enter' to continue as a guest.\n"
    )
    age, gender, user_login = check_user()
    distance = 2000
    # Added to make sure functions will run correctly when more distances added
    row_time = inputs.get_row_time()
    split_time, display_split = calc.calculate_splits(row_time, distance)
    typed(f" Your split time is: {display_split}\n")
    watts = calc.calculate_watts(split_time)
    typed(f" Your watts generated are: {watts}")
    print("\n")
    typed(" Retrieving your ranking, please wait...\n")
    try:
        SHEET = ref_data.spreadsheet_connect()
        category = ref_data.lookup_category(age, gender, distance, watts, SHEET)
        category_description = ref_data.get_category_description(SHEET)
        typed(f" Your performance category is {category.title()}!\n")
        description = category_description[category]
        typed(f" You are: {description[0]}\n {description[1]}\n {description[2]}")
        print("\n")
        ref_data.save_row_data(date.today(), row_time, watts, user_login, SHEET)
    except Exception:
        # print(traceback.format_exc())
        typed(
            " Apologies the database is not available at this time.\n"
            " Please check your connection and try again later\n"
            " If the problem persists, please contact customer support\n"
        )
        

def run():
    """
    Restart main if any other key is pressed in program_exit
    Exits the program cleanly if user chooses exit option
    """
    while True:
        main()
        if program_exit():
            break


run()
