#TEXT = "function square arguments n new line print n * n new line back tab new line call square arguments 4"
import git
import sys
from PyQt5.Qt import QApplication
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit, QLabel, QPushButton
from PyQt5.QtCore import QSize
import keyboard
from convert import get_python_code
import speech_recognition as sr 
import pyttsx3  

r = sr.Recognizer()  
def SpeakText(command): 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 

appctxt = QApplication([])
w = QWidget()  
w.setWindowTitle("Alexa Lets Code")
w.resize(512, 512) 

def write():
    
    while(1):     
        try: 
            with sr.Microphone() as source2: 
                r.adjust_for_ambient_noise(source2, duration=0.2) 
                audio2 = r.listen(source2) 
                MyText = r.recognize_google(audio2) 
                MyText = MyText.lower() 
  
                print(MyText)
                keyboard.write(get_python_code(MyText))
                keyboard.write("\n")
            
              
        except sr.RequestError as e: 
            print("Could not request results; {0}".format(e)) 
             
        except sr.UnknownValueError: 
            continue
    
submit = QPushButton("start", w)
submit.move(5, 50)
submit.clicked.connect(write)
w.show()
sys.exit(appctxt.exec_())

"""
g = git.cmd.Git("C:/Users/Nand/Alexa-Lets-Code")

g.add(".")
g.commit("-m \"init\"")
g.push()
"""
