from utils import typed, program_exit, display_header
import inputs
import calc
import os
import ref_data


def main():
    """
    Runs all functions
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    # Source - https://stackoverflow.com/a/2084628

    display_header()
   
    typed(
        " Welcome to Row Assist, your indoor rowing assistant.\n"
    )
    typed(
        " You will soon be asked for your age, "
        "gender and your latest 2k test time.\n"
    )
    typed(
        " I will calculate your split time and watts "
        "and provide you with a ranking."
    )
    print("\n")
    age = inputs.get_age()
    gender = inputs.get_gender()
    distance = 2000
    # Added to make sure functions will run correctly when more distances added
    row_time = inputs.get_row_time()
    split_time, display_split = calc.calculate_splits(row_time, distance)
    typed(f" Your split time is: {display_split}\n")
    watts = calc.calculate_watts(split_time)
    typed(f" Your watts generated are: {watts}")
    print("\n")
    typed(" Retrieving your ranking, please wait...\n")
    category = ref_data.lookup_category(age, gender, distance, watts)
    category_description = ref_data.get_category_description()
    typed(f" Your performance category is {category.title()}!\n")
    description = category_description[category]
    typed(f" You are: {description[0]}\n {description[1]}\n {description[2]}")
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
