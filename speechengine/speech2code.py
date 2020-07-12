import speech_recognition as sr

import pyttsx3
engine = pyttsx3.init() # object creation
r = sr.Recognizer()

import time
import random

import requests


def sendrawtext(text):
    url = "https://alexaletscode.herokuapp.com/"

    payload = str(text)
    headers = {
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)




def getSpeech():
    text = "unknown"
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return text


flag = True
operation = 0 ##0 code commands, 1 raw text, 2 git


while flag is True:
    engine.say("Hello, welcome to speech to code. please choose your operation. Say exit or quit anytime to end the program. Say next line to directly go to the next line")
    engine.runAndWait()


    text = getSpeech()
    if "git" in text:
        operation = 2
    if "raw" in text:
        operation = 1
    if "commander" in text:
        operation = 0
    if "next" in text:
        continue
    if "exit" in text or "quit" in text:
        flag = False
        continue

    if operation == 0:

        engine.say("please choose your language. Say Sea, Sea Plus Plus, Java Script or python")
        engine.runAndWait()

        text2 = getSpeech()
        text2 = text2.lower()
        if "java" in text2:
            lang = "js"
        if "sea" in text2:
            lang = "c"
        if "sea" in text2 and "plus" in text2:
            lang = "c++"
        if "python" in text2:
            lang = "python"
        if "exit" in text2 or "quit" in text2:
            flag = False
            continue
        continue

    if operation == 1:
        engine.say("saw anything, this is raw input")
        engine.runAndWait()

        text3 = getSpeech()
        text3 = text2.lower()

        sendrawtext(text3)


        continue

    ##endpoint is called here



engine.say("goodbye")
engine.runAndWait()
engine.stop()








