# import gspread
# from google.oauth2.service_account import Credentials
from utils import typed

# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
# ]

# CREDS = Credentials.from_service_account_file("creds.json")
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# SHEET = GSPREAD_CLIENT.open("row_assist")


def ages_tuple(min, max):  # Move this into age_index()
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
    del data[0]  # Removes title cell
    for index, age in enumerate(data, 2):  # Row 0 doesn't exist and row 1 is headings
        a, b = age
        if int(value) >= int(a) and int(value) <= int(b):
            return index


def get_data_row(sheet, index, value):
    """
    Retrieves the correct row of data from the google sheet, looks up
    watts value and returns the column number for the PREVIOUS column
    """
    watts_row = sheet.row_values(index)
    watts_row = watts_row[2:]  # Removes min_age and max_age values
    for r_index, watts in enumerate(watts_row, 3):  # Cols 1&2 are age values
        if int(value) < int(sheet.cell(index, 3).value):
            return 3
        elif int(value) < int(watts):
            return r_index - 1  # Remove 1 because end point is the first category NOT achieved
        elif int(value) >= int(sheet.cell(index, 8).value):
            return 8

def get_category(sheet, value):
    """
    Uses previously generated column index to retrieve the correct
    ranking category and display it to the user
    """
    category = sheet.cell(1, int(value)).value
    typed(f"Your performance category is {category.title()}!\n")
    return category


def get_category_description(data):
    """
    Retrieves all values from the categories sheet and converts 
    them to a dictionary.
    """    
    keys = data.col_values(1)
    values = data.col_values(2)
    categories = {key: value for key, value in zip(keys, values)}
    return categories

