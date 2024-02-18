#!/usr/bin/python3
""" script that starts a Flask web application:"""

from flask import Flask, render_template


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

@app.route('/number/<int:n>', strict_slashes=False)
def is_a_numbet(n):
    """Routing to n for intergers"""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def a_number_template(n):
    """Routing to n for intergers with templates"""
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
