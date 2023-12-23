#!/usr/bin/python3
""" a script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route function for the root URL("/")

    Returns:
    str: A greeting message "Hello HBNB!"
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    """ Run the Flask web app """
    app.run(host='0.0.0.0', port=5000)
