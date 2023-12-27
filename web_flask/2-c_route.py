#!/usr/bin/python3
"""
a script that starts a Flask web application,
that must be listening on 0.0.0.0, port 5000
"""

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


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route function for the "/hbnb URL.

    Returns:
    str: A message "HBNB".
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Route function for the "/c/<text>" URL.

    Args:
    text (str): The value of the text variable.

    Returns:
    str: The message "C " followed by the value
    of the text variable
    """
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"


if __name__ == "__main__":
    """ Run the Flask web app """
    app.run(host='0.0.0.0', port=5000)
