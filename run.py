import gspread
from google.oauth2.service_account import Credentials
import time
import datetime 

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open("row_assist")


def typed(string):
    """
    Creates a typed effect for the text 
    """
    for i in string:
        print(i, end="", flush=True)
        time.sleep(0.03)


def get_user_age():
    """
    Get user age data
    Run a while loop to get valid data from the user
    """
    while True:
        typed("Please enter your age\n")
        user_age = input("Age: ") # Add a newline character before deployment

        if validate_age(user_age):
            typed(f"You entered: {user_age}")
            print("\n")
            break
    
    return user_age
    
def validate_age(data):
    """
    Inside the try, converts age to an integer.
    Raises ValueError if string cannot be converted into int
    Raises TypeError if age falls outside the range 10-100
    """
    try: 
        a = int(data)
        if a < 10 or a > 100:
            raise TypeError
    except ValueError:
        typed("Invalid age, please enter a whole number between 10 and 100")
        print("\n")
        return False
    except TypeError:
        typed("I'm sorry only ages between 10 and 100 can be accepted")
        print("\n")
        return False

    return True
    

def get_user_gender():
    """
    Get user gender data
    Run a while loop to get valid data from the user
    """
    while True:
        typed("Please enter your gender: m/f\n")
        user_gender = input("Gender: ") # Add a newline character before deployment

        if validate_gender(user_gender):
            typed(f"You entered: {user_gender}")
            print("\n")
            break
    
    return user_gender


def validate_gender(data):
    """
    Inside the try, checks for m or f character.
    Raises ValueError if any other character is entered
    """
    try: 
        if data.lower() != "f" and data.lower() != "m":
            raise ValueError
    except ValueError:
        typed("Invalid entry, please enter either m or f")
        print("\n")
        return False

    return True

def get_user_row_time():
    """
    Get time for latest row
    Run a while loop to get valid data from the user
    Convert inputs into a readable string and and a computable integer
    """
    typed("Please enter your latest 2k test time. Minutes, then seconds, then tenths\n")
    while True:
        user_row_minutes = input("Minutes: ") # Add a newline character before deployment
        if validate_minutes(user_row_minutes):
            user_row_seconds = input("Seconds: ") # Add a newline character before deployment
            if validate_seconds(user_row_seconds):
                user_row_tenths = input("Tenths: ") # Add a newline character before deployment
                user_row_time = f"{user_row_minutes}:{user_row_seconds.zfill(2)}.{user_row_tenths}"
                if validate_tenths(user_row_tenths):
                    typed(f"You entered: {user_row_time}")
                    print("\n")
                    break
 
    actual_time = (int(user_row_minutes) * 60) + int(user_row_seconds) + (int(user_row_tenths) / 10)

    return actual_time       

def validate_minutes(data):
    """
    Inside the try, converts time to integer
    Raises ValueError if the string can't be converted or if minutes 
    fall ouside the range 1-59
    """
    try:
        m = int(data)
        if m < 1 or m > 59:
            raise ValueError
    except ValueError:
        typed("Invalid entry, please enter a minutes value between 1 and 59")
        print("\n")
        return False
    
    return True


def validate_seconds(data):
    """
    Inside the try, converts time to integer
    Raises ValueError if the string can't be converted or if seconds 
    fall ouside the range 0-59
    """
    try:
        m = int(data)
        if m < 0 or m > 59:
            raise ValueError
    except ValueError:
        typed("Invalid entry, please enter a seconds value between 0 and 59")
        print("\n")
        return False
    
    return True

def validate_tenths(data):
    """
    Inside the try, converts time to integer
    Raises ValueError if the string can't be converted or if tenths 
    fall ouside the range 0-9
    """
    try:
        m = int(data)
        if m < 0 or m > 9:
            raise ValueError
    except ValueError:
        typed("Invalid entry, please enter a tenths value between 0 and 9")
        print("\n")
        return False
    
    return True

def main():
    """
    Runs all functions
    """
    # typed("Welcome to Row Assist, your indoor rowing assistant.\n")
    # typed("You will soon be asked for your gender, age and your latest 2k test time.\n")
    # typed("I will calculate your split time and watts and provide you with a ranking.\n")
    # print("\n")
    # age = get_user_age()
    # gender = get_user_gender()
    row_time = get_user_row_time()
    print(row_time)

main()
