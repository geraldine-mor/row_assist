import gspread
from google.oauth2.service_account import Credentials
from utils import typed


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open("row_assist")


def get_row_number(col1, col2, age):
    """
    Creates a list of tuples from the 2 age columns
    Loops through the list comparing each tuple to the provided age
    and returns the list index of the correct range tuple
    """
    age_range = [(x, y) for x, y in zip(col1, col2)]
    del age_range[0]  # Removes title cell
    for row_index, age_tuple in enumerate(age_range, 2):
        # Row 0 doesn't exist and row 1 is headings
        min_age, max_age = age_tuple
        if int(age) >= int(min_age) and int(age) <= int(max_age):
            return row_index


def get_col_number(sheet, index, watts):
    """
    Retrieves the reference row of data from the google sheet, loops
    through the watts values to find the right one and returns
    the column number for the PREVIOUS column
    """
    watts_row = sheet.row_values(index)
    watts_row = watts_row[2:]  # Removes min_age and max_age values
    for col_index, ref_watts in enumerate(watts_row, 3):
        # Cols 1&2 are age values so enumerate starts at 3
        if int(watts) < int(sheet.cell(index, 3).value):
            return 3
        elif int(watts) < int(ref_watts):
            return col_index - 1
        # Remove 1 because end point is the first category NOT achieved
        elif int(watts) >= int(sheet.cell(index, 8).value):
            return 8


def get_category(sheet, index):
    """
    Uses column index to retrieve the correct category
    """
    user_category = sheet.cell(1, int(index)).value

    return user_category


def get_category_description():
    """
    Retrieves all values from the categories sheet and converts
    them to a dictionary.
    """
    keys = SHEET.worksheet("categories").col_values(1)
    col2 = SHEET.worksheet("categories").col_values(2)
    col3 = SHEET.worksheet("categories").col_values(3)
    col4 = SHEET.worksheet("categories").col_values(4)
    categories = {
        key: [a, b, c] for key, a, b, c in zip(keys, col2, col3, col4)}
    return categories


def lookup_category(age, gender, distance, watts):
    """
    Determines user's performance category by looking up their age
    and watts against the relevant reference sheet
    """
    sheet = SHEET.worksheet(f"{gender}_{distance}")
    row_index = get_row_number(sheet.col_values(1), sheet.col_values(2), age)
    col_index = get_col_number(sheet, row_index, watts)
    category = get_category(sheet, col_index)
    return category


def save_row_data(date, time, watts, user_login):
    """
    Provides option to save user data if the user is "logged in" and
    stores the data in the Google sheet
    """
    if user_login:
        while True:
            save = input(" Do you wish to save this test data? Y/N:")
            user_sheet = SHEET.worksheet(user_login)
            if save.lower() == "y":
                save_data = [str(date), time, watts]
                user_sheet.append_row(save_data)
                typed(" Your test data has been saved")
                print("\n")
                break
            elif save.lower() == "n":
                typed(" Your test data has been deleted")
                print("\n")
                break
            else:
                typed(" Invalid enrty.")
                continue
