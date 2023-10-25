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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ Route function for /states and /states/<id> """
    state_not_found = False
    if id is not None:
        states = storage.all(State, id)
        id_exists = True
        if len(states) == 0:
            state_not_found = True
    else:
        states = storage.all(State)
        id_exists = False
    return render_template('9-states.html', states=states,
                           id_exists=id_exists,
                           state_not_found=state_not_found)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
