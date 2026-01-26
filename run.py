import gspread
from google.oauth2.service_account import Credentials
from utils import typed
import data
import math


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open("row_assist")

def calculate_splits(data):
    """
    Calculates the time per 500m from the data provided 
    Time(s) / (distance / 500)
    Converts result into readable time format
    """
    distance = 2000
    calc_split = data / (distance / 500)
    split_mins = math.floor(calc_split / 60)
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
    typed(f"Your watts generated are: {watts}\n")

    return watts

def get_reference_min_age(data):
    """
    Retrieve min age column from google sheets
    """
    ref_sheet = SHEET.worksheet(f"{data}_2000")
    age_min = ref_sheet.col_values(1)
    
    return age_min


def get_reference_max_age(data):
    """
    Retrieve max age column from google sheets
    """
    ref_sheet = SHEET.worksheet(f"{data}_2000")
    age_max = ref_sheet.col_values(2)
    
    return age_max


def ages_tuple(min, max):
    """
    Creates a list of tuples (min, max)
    """
    reference_ages = [(x, y) for x, y in zip(min, max)]
    
    return reference_ages


def age_index(data, value):
    """
    Loops through the list comparing each tuple to the provided age
    and returns the list index of the correct range tuple
    """
    del data[0]
    for index, age in enumerate(data):
        a,b = age
        if int(value) >= int(a) and int(value) <= int(b):
            return index + 1
        

def main():
    """
    Runs all functions
    """
    typed("Welcome to Row Assist, your indoor rowing assistant.\n")
    typed("You will soon be asked for your age, gender and your latest 2k test time.\n")
    typed("I will calculate your split time and watts and provide you with a ranking.")
    print("\n")
    age = data.get_user_age()
    gender = data.get_user_gender()
    row_time = data.get_user_row_time()
    user_split = calculate_splits(row_time)
    user_watts = calculate_watts(user_split)
    min_age = get_reference_min_age(gender)
    max_age = get_reference_max_age(gender)
    age_range = ages_tuple(min_age, max_age)
    row_index = age_index(age_range, age)


main()
