#!/usr/bin/python3
"""Module that initiates flask"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """returns string html"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """returns c and name of route"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text="is cool"):
    """returns python and name of route"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number', strict_slashes=False)
@app.route('/number/<n>', strict_slashes=False)
def pythoniscool(num):
    """returns python and name of route"""
    if num is int:
        return num + " is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
