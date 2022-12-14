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
def set_mood():
    return f"<p>Hello {escape(name)}!</p>"

@app.post("/")
def my_name_is():
    name = request.form["name"]
    return {
        "status": "OK"
    }
