#TEXT = "function square arguments n new line print n * n new line back tab new line call square arguments 4"

import sys
from PyQt5.Qt import QApplication
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit, QLabel, QPushButton
from PyQt5.QtCore import QSize
import keyboard
from convert import get_python_code

appctxt = QApplication([])
w = QWidget()  
w.setWindowTitle("Alexa Lets Code")
w.resize(512, 512) 

title = QPlainTextEdit(w)
title.setPlaceholderText("Enter raw text")
title.move(5, 5)
title.resize(502, 40)

def write():
    k = get_python_code(title.toPlainText())
    keyboard.wait('\n')
    keyboard.write(k)

submit = QPushButton("submit", w)
submit.move(5, 50)
submit.clicked.connect(write)
w.show()
sys.exit(appctxt.exec_())

