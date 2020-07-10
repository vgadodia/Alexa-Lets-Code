from pynput.keyboard import Key, Controller
from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import unidecode
import time

keyboard = Controller()

app = Flask(__name__)
ask = Ask(app, "/reddit_reader")

def get_headlines():
    user_pass_dict = {'user':'vgadodia',
                      'password': 'tennis24',
                      'api_type': 'JSON'}
    sess = requests.Session()
    sess.headers.update({"User-Agent": 'I am testing Alexa: Veer'})
    sess.post("https://reddit.com/api/login", data = user_pass_dict)
    time.sleep(1)
    url = "https://reddit.com/r/worldnews/.json?limit=10"
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = [unidecode.unidecode(listing['data']['title']) for listing in data['data']['children']]
    titles = "... ".join([i for i in titles])
    return titles

@app.route('/')
def homepage():
    # keyboard.press(Key.cmd)
    # keyboard.press(Key.tab)
    # keyboard.release(Key.tab)
    # keyboard.release(Key.cmd)

    # time.sleep(1)

    # keyboard.press(Key.cmd)
    # keyboard.press('n')
    # keyboard.release(Key.cmd)
    # keyboard.release('n')
    # keyboard.type('This is one line.\nAnd this is the next line.\n\tThis line has been tabbed in.')
    
    return "Hi there, how ya doin?"

@ask.launch
def start_skill():
    welcome_message = "Hello there, would you like the news?"
    return question(welcome_message)

@ask.intent("YesIntent")
def share_headlines():
    headlines = get_headlines()
    headline_msg = "The current world news headlines are {}".format(headlines)
    return statement(headline_msg)

@ask.intent("NoIntent")
def no_intent():
    bye_text = "Ok bye then"
    return statement(bye_text)

if __name__ == '__main__':
    app.run(debug=True)