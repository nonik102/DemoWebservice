
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
        valid = False
        for line in f:
            if line.strip() == f"{username},{password}":
                valid = True
                break
        return valid


if __name__ == "__main__":
    create_user("a", "b")
    print("created user a with pass b")
    print("check user a with pass b")
    print(check_user("a","b"))
    print("check user a with pass c")
    print(check_user("a", "c"))    