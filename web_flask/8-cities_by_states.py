#!/usr/bin/python3
"""
a script that starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Closes the database again at the end of the request
    """
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display a HTML page with a list of states and their cities.
    """
    states = storage.all("State").values()
    states_sorted = sorted(states, key=lambda x: x.name)

    return render_template('cities_by_states.html', states=states_sorted)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
