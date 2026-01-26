from utils import typed

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
    user_minutes = get_time("minutes")
    user_seconds = get_time("seconds")
    user_tenths = get_time_tenths()            
    user_row_time = f"{user_minutes}:{user_seconds.zfill(2)}.{user_tenths}"
                
    typed(f"You entered: {user_row_time}")
    print("\n")               
    actual_time = (int(user_minutes) * 60) + int(user_seconds) + (int(user_tenths) / 10)
    check_wr(actual_time)
    
    return actual_time   


def get_time(data):
    """
    Get time values for latest row
    Run a while loop to get valid data from the user
    """
    while True:
        user_input = input(f"{data.capitalize()}: ") # Add a newline character before deployment
        if validate_time(user_input):
            return user_input


def get_time_tenths():
    """
    Get tenths value for latest row
    Run a while loop to get valid data from the user
    """
    while True:
        tenths = input("Tenths: ") # Add a newline character before deployment
        if validate_tenths(tenths):
            break

    return tenths


def validate_time(data):
    """
    Inside the try, converts time to integer
    Raises ValueError if the string can't be converted or if minutes 
    fall ouside the range 0-59
    """
    try:
        m = int(data)
        if m < 0 or m > 59:
            raise ValueError
    except ValueError:
        typed("Invalid entry, please enter a minutes value between 0 and 59")
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

def check_wr(data):
    if data < 335.8:
        typed("Greeting Barry Allen!\n")
        typed("The fastest 2k ever recorded is 5:35.8 and you smashed it!")
        print("\n")
