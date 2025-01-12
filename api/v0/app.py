#!/usr/bin/python3
"""flask REST api handler"""

from flask import Flask
from .views import app_view

app = Flask(__name__)
app.register_blueprint(app_view)


@app.route('/')
def confront():

    return "hello"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
