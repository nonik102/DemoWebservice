from flask import Flask, request, abort
from markupsafe import escape

import mood_service
import login_service

app = Flask(__name__)

special_characters = "!@#$%^&*()-=+/.,<>?\"';:[]{}\|`~"

@app.post("/signup")
def create_account():
    pass

@app.get("/")
def get_mood():
    pass

@app.post("/")
def set_mood():
    pass

