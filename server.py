import flask
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

command = "0"
k = "0"

@app.route('/', methods=['GET', 'POST'])

def home():
    global command, k
    if flask.request.method == 'GET':
        k = command
        command = "0"
        return k
        
    else:
        print(flask.request.data.decode("utf-8"))
        command = flask.request.data.decode("utf-8")

if __name__ == '__main__':
    app.run(debug=True)