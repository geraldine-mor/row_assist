"""
Manages Google Sheets API interactions for rowing performance data

Retrieves user performance rankings and facilitates saving workout data
to persistent user worksheets.
"""


import gspread
from google.oauth2.service_account import Credentials
from utils import typed
from datetime import date


def spreadsheet_connect():
    """
    Opens the row_assist reference data worksheet

    Returns:
        gspread.spreadsheet.Spreadsheet: spreadsheet for further use
    """
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

    CREDS = Credentials.from_service_account_file("creds.json")
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    GSPREAD_CLIENT.set_timeout(10)
    SHEET = GSPREAD_CLIENT.open("row_assist")

    return SHEET


def get_row_number(col1, col2, age):
    """
    Finds the spreadsheet row number matching the user's age range.

    Creates age range tuples from min/max age columns, then searches
    for the range containing the user's age.

    Args:
        col1 (list): Minimum age values from spreadsheet column
        col2 (list): Maximum age values from spreadsheet column
        age (int): User's age to compare to ranges

    Returns:
        int: Spreadsheet row number (1-indexed) of matching age range
    """
    age_range = [(x, y) for x, y in zip(col1, col2)]
    # Remove title cell
    # Use of del keyword suggested by Geeks for Geeks (link in credits)
    del age_range[0]

    # Start enumerate at 2 (row 1 is title, row 0 doesn't exist)
    # Use of enumerate() explained by w3 schools (link in credits)
    for row_index, age_tuple in enumerate(age_range, 2):
        min_age, max_age = age_tuple
        if age >= int(min_age) and age <= int(max_age):
            return row_index


def get_col_number(sheet, index, watts):
    """
    Finds the column number matching the user's ranking category

    Args:
        sheet (gspread.spreadsheet.Spreadsheet):
            row_assist Google Sheet reference data
        index (int): index of the required reference row
        watts (int): user's watts value

    Returns:
        int: Spreadsheet column number of user's performance ranking
    """
    watts_row = sheet.row_values(index)
    # Remove min_age and max_age values
    watts_row = watts_row[2:]

    # Cols 1&2 are age values so start enumerating at 3
    for col_index, ref_watts in enumerate(watts_row, 3):
        # Use of cell(row, column).value derived from gspread docs
        if watts < int(sheet.cell(index, 3).value):
            return 3
        elif watts < int(ref_watts):
            # Remove 1 because end point is the first category NOT achieved
            return col_index - 1
        elif watts >= int(sheet.cell(index, 8).value):
            return 8


def get_category(sheet, index):
    """
    Retrieves the performance ranking from the the spreadsheet cell

    Args:
        sheet (gspread.spreadsheet.Spreadsheet):
            row_assist Google Sheet reference data
        index (int): column number of user's performance ranking

    Returns:
        str: User's performance ranking
    """
    user_category = sheet.cell(1, index).value

    return user_category


def get_category_description(sheet):
    """
    Creates a dictionary from the ranking categories and their respective
    descriptions

    Args:
        sheet (gspread.spreadsheet.Spreadsheet):
            row_assist Google Sheet reference data

    Returns:
        dict: Category: Description pairs
    """
    keys = sheet.worksheet("categories").col_values(1)
    col2 = sheet.worksheet("categories").col_values(2)
    col3 = sheet.worksheet("categories").col_values(3)
    col4 = sheet.worksheet("categories").col_values(4)
    categories = {
        key: [a, b, c] for key, a, b, c in zip(keys, col2, col3, col4)}
    return categories


def lookup_category(age, gender, distance, watts, sheet):
    """
    Orchestrates the retrieval of the user's ranking category

    Args:
        age (int): user's age in years
        gender (str): user's gender "f" or "m"
        distance (int): distance rowed
        watts (int): user's watts
        sheet (gspread.spreadsheet.Spreadsheet):
            row_assist Google Sheet reference data

    Returns:
        str: User's performance ranking
    """
    sheet = sheet.worksheet(f"{gender}_{distance}")
    row_index = get_row_number(sheet.col_values(1), sheet.col_values(2), age)
    col_index = get_col_number(sheet, row_index, watts)
    category = get_category(sheet, col_index)
    return category


def save_row_data(time, watts, user_login, sheet):
    """
    Saves rowing metrics to the google sheet for persistent user

    Args:
        time (float): user's row time in total seconds
        watts (int): user's watts value
        user_login (str or bool): Username if persistent user, False if guest
        sheet (gspread.spreadsheet.Spreadsheet):
            row_assist Google Sheet reference data
    """
    today = date.today()
    if user_login:
        while True:
            save = input(" Do you wish to save this test data? Y/N:")
            user_sheet = sheet.worksheet(user_login)
            if save.lower() == "y":
                save_data = [str(today), time, watts]
                user_sheet.append_row(save_data)
                typed(" Your test data has been saved")
                print("\n")
                break
            elif save.lower() == "n":
                typed(" Your test data has been deleted")
                print("\n")
                break
            else:
                typed(" Invalid entry.")
                continue
