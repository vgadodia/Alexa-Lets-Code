import keyboard
from convert import get_python_code
TEXT = "function square arguments n new line print n * n new line back tab new line call square arguments 4"
k = get_python_code(TEXT)

keyboard.wait('esc')
keyboard.write(k)