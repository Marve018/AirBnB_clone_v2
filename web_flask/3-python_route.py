#!/usr/bin/python3
""" script that starts a Flask web application:"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Routing to root """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Routing to /hbnb page"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Routing to C using Variables"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """Routing to python with defult option using Variables"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
