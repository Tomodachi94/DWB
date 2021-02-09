from flask import Flask
from threading import Thread
import random
import bot

config = bot.prepConfig()

app = Flask('')


@app.route('/')
def home():
    return f"Dash {version}"


def run():
    app.run(
        host='0.0.0.0',
        port=random.randint(2000, 9000)
    )


def keepalive():
    '''
    Creates and starts new thread that runs the function run.
    '''
    t = Thread(target=run)
    t.start()
