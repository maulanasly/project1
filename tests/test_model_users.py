import unittest
from flask_fixtures import FixturesMixin
from blogsapi import app, db


class UserModelTest(unittest.TestCase, FixturesMixin):

    app = app
    db = db

    fixtures = ['testing.yaml']

    def tearDown(self):
        db.session.close()