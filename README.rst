==========
Flask-UUID
==========

*Flask-UUID* is a simple Flask_ extension that registers a UUID converter for
urls on a Flask application. It uses the standard library's ``uuid`` module to
convert UUIDs to and from strings.

This extension allows you to easily route and generate urls containing UUID parts,
e.g. ``/page/fe4a3e33-cb4b-42ac-a29b-a8160a85af7e``.

.. _Flask: http://flask.pocoo.org


Installation
============

Installation is trivial::

    $ pip install Flask-UUID


Usage
=====

Flask-UUID is a well-behaved Flask extension, so you can either initialise it
directly upon instantiation::

    from flask import Flask
    from flask_uuid import FlaskUUID

    app = Flask(__name__)
    FlaskUUID(app)

Or initialise it like this::

    from flask import Flask
    from flask_uuid import FlaskUUID

    app = Flask(__main__)

    flask_uuid = FlaskUUID()
    flask_uuid.init_app(app)

Now you can use it in your routes like any other converter::

    @app.route('/<uuid:id>')
    def mypage(id):
        return id  # 'id' is a uuid.UUID instance

You can also use UUID instances to generate urls::

    random_uuid = uuid.uuid4()
    url = url_for('mypage', id=random_uuid)

Note that, by default, the converter only accepts and generates lowercase
hexadecimal UUIDs with dashes at the proper places, in order to keep urls
unique. If you want to accept any UUID string accepted by the ``uuid.UUID()``
constructor, simply set the `strict` flag to `False`::

    @app.route('/<uuid(strict=False):id>'>
    def mypage(id):
        return id


License
=======

This software is BSD licensed; see `LICENSE.rst` for more information.


.. image:: https://d2weczhvl823v0.cloudfront.net/wbolster/flask-uuid/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free
