from math import floor


def calculate_splits(seconds, distance):
    """
    Calculates the time per 500m from the data provided
    Time(s) / (distance / 500)
    Converts result into readable time format
    """
    calc_split = seconds / (distance / 500)
    split_mins = floor(calc_split / 60)
    split_secs = round(calc_split - (split_mins * 60), 1)
    user_split = f"{split_mins}:{str(split_secs).zfill(4)}"
    # z-fill(4) was used because split_secs was always in the format
    # 0.0 so min 4 characters was required to always achieve 00.0

    return calc_split, user_split


def calculate_watts(split):
    """
    Converts split times into watts
    2.8 / (split(s) / 500)^3
    Rounds to nearest int as per row erg monitors
    """
    calc_watts = round(2.8 / (split / 500)**3)

    return calc_watts
