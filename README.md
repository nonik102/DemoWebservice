# DemoWebservice

Demo backend webservice with a REST API

## Overview

The webservice has the following features:

### Login functionality: 

use the `/signup` endpoint with username and password passed in to create an account. The username and password are stored in a database. In all future calls, the username and password must be provided to log in.    

**Examples:**

create an account: `curl --data "username=my_username&password=my_password" server_address`

make a call using account details: `curl --user my_username:my_password server_address`

### Mood Functionality:
use the `/mood` endpoint to create and get mood data, as well as streak information. Mood data is persisted in a database which can be queried later. A client is only able to view their mood data. Mood data is returned in the following format:

```json
{
    "mood_data": {
        "date1": ["mood1", "mood2", ...],
        "date2": ["mood1", "mood2", ...],
        ...
        "daten": ["mood1", "mood2", ...]
    },
    "streak": 10
}
```

Each date has a list of moods corresponding to all moods submitted that day. No promises are made about the order of the moods or the dates in the response.

**Examples:**

POST mood data: `curl --user my_username:my_password --data "mood=my_mood" server_address/mood`

GET mood data: `curl -- user my_username:my_password server_address/mood`

## Dependencies

This server has the following dependencies:

- flask
- flask_httpauth

These can be installed by running the following: `pip install < requirements.txt`

## Usage

To run the server using defaults, use `make run`

To run the server directly, use `flask --app controller.py run` or `python -m flask --app controller.py run`

