import unittest
from App.models import Street

class StreetModelUnitTests(unittest.TestCase):

    def test_create_street(self):
        street = Street("Main Street")
        self.assertEqual(street.name, "Main Street")

    def test_street_json(self):
        street = Street("Main Street")
        expected = {'streetId': None, 'name': 'Main Street'}
        self.assertDictEqual(street.get_json(), expected)