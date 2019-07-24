#!/usr/bin/env python

import uuid

from flask import Flask, redirect, url_for
from flask_uuid import FlaskUUID

app = Flask(__name__)
FlaskUUID(app)


@app.route('/')
def index():
    return redirect(url_for('example1', id=uuid.uuid4()))


@app.route('/example1/<uuid:id>/')
def example1(id):
    return repr(id)


@app.route('/example2/<uuid(strict=False):id>/')
def example2(id):
    return repr(id)


if __name__ == '__main__':
    app.run(debug=True)
