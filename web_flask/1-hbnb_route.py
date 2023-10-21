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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
