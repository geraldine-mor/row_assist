import gspread
from google.oauth2.service_account import Credentials
from utils import typed
import data
import calc


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open("row_assist")


def ages_tuple(min, max): # Move this into age_index()
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
    del data[0] # Removes title cell
    for index, age in enumerate(data, 2): # Row 0 doesn't exist and row 1 is headings
        a,b = age
        if int(value) >= int(a) and int(value) <= int(b):
            return index 
        

def get_data_row(sheet, index, value):
    """
    Retrieves the correct row of data from the google sheet, looks up 
    watts value and returns the column number for the PREVIOUS column
    """
    watts_row = sheet.row_values(index)
    watts_row = watts_row[2:] # Removes min_age and max_age values
    for r_index, watts in enumerate(watts_row, 3): # Cols 1&2 are age values
        if int(value) < int(watts):
            return r_index - 1 # Remove 1 because end point is the first category NOT achieved
        

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
    distance = 2000 # Added to make sure functions will run correctly when more distances added
    row_time = data.get_user_row_time()
    user_split = calc.calculate_splits(row_time)
    user_watts = calc.calculate_watts(user_split)
    # The following vars should be moved 
    sheet = SHEET.worksheet(f"{gender}_{distance}") 
    min_age = sheet.col_values(1)
    max_age = sheet.col_values(2)
    age_range = ages_tuple(min_age, max_age)
    row_index = age_index(age_range, age)
    col_index = get_data_row(sheet, row_index, user_watts)
    

main()
