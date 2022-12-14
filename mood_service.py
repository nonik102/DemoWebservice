import database_client
from datetime import datetime, timedelta

def set_mood(mood:str) -> None:
    """set the client's mood to a specific value for today

    Args:
        mood (str): the mood passed by the user
    """
    pass

def get_mood(user:str) -> dict:
    """get the client's previous mood history along with streak info
    
    Args:
        user (str): the user to get mood data for

    Returns:
        dict: dictionary containing the moods and the current streak
    """
    # get the mood data for this user from the db
    data = database_client.get_mood_data(user)
    # check the streak
    dates = [date for date,mood in data]
    streak = get_streak(dates)
    mood_dict = {}
    for date,mood in data:
        mood_dict[date]=mood
    return {
        "mood_data": mood_dict,
        "streak": streak
    }

def get_streak(dates: list) -> int:
    """get the current streak length

    Args:
        data (list): list of dates

    Returns:
        int: the current streak length
    """
    # remove duplicates
    unique_dates = []
    [unique_dates.append(date) for date in dates if date not in unique_dates]
    # transform into datetime objects
    dates = [datetime.strptime(date, "%m/%d/%y") for date in unique_dates]
    # sort the dates list
    dates.sort()
    # 
    streak = 0
    last_date = datetime.today()
    for date in dates:
        if last_date + timedelta(days=1) == date:
            streak += 1
        else:
            streak = 1
        last_date = date
    return streak


if __name__ == "__main__":
    print(get_streak(["12/22/22", "12/23/22", "12/24/22", "12/31/22", "1/1/23"]))
    print(get_mood("a"))