
def create_user(username:str, password:str) -> None:
    """ Create an entry in the database for a user

    Args:
        username (str): username to use
        password (str): password to use
    """
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")


def check_user(username:str, password:str) -> bool:
    """check if a username and password corresponds to an existing user

    Args:
        username (str): submitted username
        password (str): submitted password

    Returns:
        bool: True if the combination is valid, false if not
    """
    with open("users.txt", "r") as f:
        for line in f:
            if line.strip() == f"{username},{password}":
                return True
        return False

def find_username(username:str) -> bool:
    """check if a username is already in use

    Args:
        username (str): username to find

    Returns:
        bool: true if the username is in use, false if it is not
    """
    with open("users.txt", "r") as f:
        for line in f:
            user = line.strip().split(",")[0]
            if user == username:
                return True
    return False

def get_mood_data(username:str) -> list:
    """get all mood data for a user

    Args:
        username (str): username to query on

    Returns:
        list: of all dates submitted and correspoding mood data
    """
    data = []
    with open("mood_db.txt", "r") as f:
        for line in f:
            line_data = line.strip().split(",")
            user = line_data[0]
            if user == username:
                data.append((line_data[1], line_data[2]))
    return data

def post_mood_data(username:str, date:str, mood:str) -> None:
    """add mood data for a user to the database. Include date info

    Args:
        username (str): username of the user
        date (str): date to associate with the mood data
        mood (str): mood from the user
    """
    with open("mood_db.txt", "a") as f:
        formatted_line = f"{username},{date},{mood}\n"
        f.write(formatted_line)


if __name__ == "__main__":
    # create_user("a", "b")
    # print("created user a with pass b")
    # print("check user a with pass b")
    # print(check_user("a","b"))
    # print("check user a with pass c")
    # print(check_user("a", "c"))    
    # print("check if a exists as username")
    # print(find_username("a"))
    post_mood_data("a", "11/12/22", "happy")
    print(get_mood_data("a"))
