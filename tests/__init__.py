from flask_fixtures import FixturesMixin
from api import db

import unittest

class ApiTest(unittest.TestCase, FixturesMixin):

    app = app
    db = db

    fixtures = ['testing.yaml']

    def setUp(self):
        db.engine.execute('SET GLOBAL sql_mode=""')

    def tearDown(self):
        db.session.close()
        db.engine.execute('SET GLOBAL sql_mode="NO_AUTO_VALUE_ON_ZERO"')

    def assertOK(self, resp):
        self.assertEqual(resp.status_code, 200)