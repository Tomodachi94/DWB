"""
    login.py

    MediaWiki API Demos
    Demo of `Login` module: Sending post request to login
    MIT license
"""

import requests
import bot

S = requests.Session()

config = bot.prepConfig()

URL = config["mediawikiEndpoint"]

# Retrieve login token first
PARAMS_0 = {
    'action':"query",
    'meta':"tokens",
    'type':"login",
    'format':"json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# Send a post request to login. Using the main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword

PARAMS_1 = {
    'action':"login",
    'lgname':config["mediawikiUsernane"],
    'lgpassword':config["mediawikiPassword"],
    'lgtoken':LOGIN_TOKEN,
    'format':"json"
}

R = S.post(URL, data=PARAMS_1)
DATA = R.json()

print(DATA)