"""
COPYRIGHT MADE BY @JAVIER
BEST OF THE BEST

"""
from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()

