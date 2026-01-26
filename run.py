import gspread
from google.oauth2.service_account import Credentials
from utils import typed
import data

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open("row_assist")



def main():
    """
    Runs all functions
    """
    typed("Welcome to Row Assist, your indoor rowing assistant.\n")
    typed("You will soon be asked for your gender, age and your latest 2k test time.\n")
    typed("I will calculate your split time and watts and provide you with a ranking.")
    print("\n")
    age = data.get_user_age()
    gender = data.get_user_gender()
    row_time = data.get_user_row_time()
    

main()
