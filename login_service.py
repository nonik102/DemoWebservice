import database_client


def create_account(username:str, password:str) -> None:
    """ create a new user account

    Args:
        username (str): passed in username
        password (str): passed in password
    """
    database_client.create_user(username, password)    

def check_account_is_valid(username:str, password:str) -> bool:
    """check if passed in credentials are valid

    Args:
        username (str): passed in username
        password (str): passed in password

    Returns:
        bool: true if the account is valid, false if not
    """
    return database_client.check_user(username, password)

def check_if_username_exists(username:str) -> bool:
    """check if the passed username already is in use

    Args:
        username (str): username to check

    Returns:
        bool: true if in use, false if not
    """
    return database_client.find_username(username)