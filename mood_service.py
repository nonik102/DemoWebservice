import database_client

def set_mood(mood:str) -> None:
    """set the client's mood to a specific value for today

    Args:
        mood (str): the mood passed by the user
    """
    pass

def get_mood() -> dict:
    """get the client's previous mood history along with streak info

    Returns:
        dict: dictionary containing the moods and the current streak
    """
    pass

def get_streak(today:str) -> int:
    """get the number of days the user has successfully submitted moods

    Args:
        today (str): current day

    Returns:
        int: number of days the mood has been submitted in a row
    """
    pass