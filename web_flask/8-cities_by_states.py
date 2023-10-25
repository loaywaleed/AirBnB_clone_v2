#!/usr/bin/python3
"""intiating flask web app"""

from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """displays states"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
