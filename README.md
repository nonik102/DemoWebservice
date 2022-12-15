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

## Notes

If I was making this for production, I would change a lot of things. For one, I would need to know the scale of this application. If this needed to be highly scalable, I think that python might not be the way to go, since it is interpreted instead of compiled. This means less speed and efficiency.

Also, I would use a database service. I used files as my "database" since I did not want to have to set up an entire database framework, but this is very inefficient since reading and writing to files is slow, and this is also not secure.

Another thing I would change would probably be the return value. Instead of  returning a variable size dictionary of dates from the GET endpoint, I would return a list of date objects. This would keep the API spec more constant and cleaner.

Another thing I would change would be the security. Basic HTTP auth is not very secure since it sends the data with only mild encryption. I would probably go with OAuth and Session management for security if this needed to be in prod.

Finally, if this needed to be in prod I would write unit tests, integration tests, validation tets, and security tests for all pieces of the webservice. Not only is this important for validating functionality, but it also ensures that when others make changes, they do not break existing functionality.

These are a few of the changes I would make if I was creating this for prod.