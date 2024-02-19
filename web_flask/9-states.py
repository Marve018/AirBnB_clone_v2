#!/usr/bin/python3
""" The module Starts flask web application must be listening
    on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states/<state_id>", strict_slashes=False)
@app.route("/states", strict_slashes=False)
def states_by_id(state_id=None):
    """Return an HTML Page that displays the list of states
    and cities as text"""
    states = storage.all(State)
    if state_id is not None:
        state_id = f'State.{state_id}'
    return render_template("9-states.html", states=states, state_id=state_id)


@app.teardown_appcontext
def teardown(excep):
    """Call Storage.close method"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
