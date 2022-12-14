from flask import Flask, request, abort
from markupsafe import escape

import mood_service
import login_service

app = Flask(__name__)

special_characters = "!@#$%^&*()-=+/.,<>?\"';:[]{}\|`~"

@app.post("/signup")
def create_account():
    # get params from form body
    username = request.form["username"]
    password = request.form["password"]
    # input validation
    if check_special_characters(username) or check_special_characters(password):
        abort(422)
    # check if the account already exists
    if login_service.check_account_is_valid(username, password):
        abort(400)
    # call the login service to create the account
    login_service.create_account(username, password)
    return "account created"

@app.get("/")
def get_mood():
    pass

@app.post("/")
def set_mood():
    pass


def check_special_characters(s:str) -> bool:
    """check if a string contains special characters

    Args:
        s (str): string coming from an external user

    Returns:
        bool: true if the string contains special characters, false if not
    """

    return any((c in special_characters for c in s))