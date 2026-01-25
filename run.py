import gspread
from google.oauth2.service_account import Credentials
import time

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
        time.sleep(0.05)


def user_age():
    """
    Get user age data
    Run a while loop to get valid data from the user
    """
    while True:
        typed("Please enter your age\n")
        age = input("Age: ") # Add a newline character before deployment

        if validate_age(age):
            typed(f"You entered: {age}")
            break
    
    return age
    
def validate_age(data):
    """
    Inside the try, converts age to an integer.
    Raises ValueError if string cannot be converted into int
    """
    try: 
        [int(num) for num in data]
        if int(data) < 10 | int(data) > 100:
            raise TypeError
    except ValueError:
        typed(f"Invalid age, please enter a whole number between 10 and 100")
        print("\n")
        return False
    except TypeError:
        typed("I'm sorry only ages between 10 and 100 can be accepted")
        print("\n")
        return False

    return True
    

typed("Welcome to Row Assist, your indoor rowing assistant.\n")
typed("You will soon be asked for your gender, age and your latest 2k test time.\n")
typed("I will calculate your split time and watts and provide you with a ranking.\n")
age = user_age()