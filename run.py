import gspread
from google.oauth2.service_account import Credentials
from utils import typed, program_exit
import inputs
import calc
import os
import ref_data


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open("row_assist")


def category_data(age, gender, distance, watts):
    sheet = SHEET.worksheet(f"{gender}_{distance}") 
    age_range = ref_data.ages_tuple(sheet.col_values(1), sheet.col_values(2))
    row_index = ref_data.age_index(age_range, age)
    col_index = ref_data.get_data_row(sheet, row_index, watts)
    category_data = ref_data.get_category(sheet, col_index)
    return category_data

def main():
    """
    Runs all functions
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Source - https://stackoverflow.com/a/2084628
    typed("Welcome to Row Assist, your indoor rowing assistant.\n")
    typed("You will soon be asked for your age, gender and your latest 2k test time.\n")
    typed("I will calculate your split time and watts and provide you with a ranking.")
    print("\n")
    age = inputs.get_age()
    gender = inputs.get_gender()
    distance = 2000 # Added to make sure functions will run correctly when more distances added
    row_time = inputs.get_row_time()
    split_time = calc.calculate_splits(row_time, distance)
    watts = calc.calculate_watts(split_time)
    category = category_data(age, gender, distance, watts)
    category_sheet = SHEET.worksheet("categories")
    category_description = ref_data.get_category_description(category_sheet)
    typed(f"You are: {category_description[category]}\n")
    print("\n")


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
