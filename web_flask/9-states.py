#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Teardown method to close the SQLAlchemy Session after each request
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def display_states():
    """
    Display a list of all states
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def display_cities_by_state(id):
    """
    display cities of a specific state.
    """
    state = storage.get("State", id)
    if state:
        cities = sorted(state.cities, key=lambda x: x.name)
        if hasattr(state, 'cities') else state.cities
        return render_template('9-state.html', state=state, cities=cities)
    else:
        return render_template('9-state.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
