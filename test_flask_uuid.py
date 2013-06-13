#!/usr/bin/env python

# Loosely based on https://github.com/rhyselsmore/flask-reggie

import unittest

from flask import Flask, request
from flask.ext.uuid import FlaskUUID

UUID_VALID = '48c00ee9-4dbe-413f-9fc3-d5f12a91de1c'
UUID_VALID_UPPER = '48C00EE9-4DBE-413F-9FC3-D5F12A91DE1C'
UUID_INVALID = 'foobar'


class FlaskUUIDTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        FlaskUUID(self.app)

        @self.app.route('/strict/<uuid:test>')
        def index(test):
            return "success"

        @self.app.route('/non-strict/<uuid(strict=False):test>')
        def non_strict(test):
            return "success"

        self.client = self.app.test_client()

    def test_strict(self):
        with self.client as c:

            rv = c.get('/strict/%s' % UUID_VALID)
            assert rv.data == b"success"
            assert str(request.view_args['test']) == UUID_VALID

            rv = c.get('/strict/%s' % UUID_INVALID)
            assert rv.status_code == 404

    def test_non_strict(self):
        with self.client as c:

            rv = c.get('/non-strict/%s' % UUID_VALID)
            assert rv.data == b"success"

            rv = c.get('/non-strict/%s' % UUID_VALID_UPPER)
            assert rv.data == b"success"


if __name__ == '__main__':
    unittest.main()
