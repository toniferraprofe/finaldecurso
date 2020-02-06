"""
COPYRIGHT MADE BY @JAVIER
BEST OF THE BEST

"""
from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Roberto !!'


if __name__ == '__main__':
    app.run()

