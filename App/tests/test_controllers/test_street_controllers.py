import unittest
from App.models import Street
from App.controllers.street_controller import create_street, get_all_streets
from App.database import db

class StreetControllerUnitTests(unittest.TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()

    def test_create_street(self):
        street = create_street("Sunset Boulevard")
        self.assertIsNotNone(street.streetId)
        self.assertEqual(street.name, "Sunset Boulevard")

    def test_get_all_streets(self):
        create_street("Main Street")
        create_street("Oak Avenue")
        streets = get_all_streets()
        names = [s.name for s in streets]
        self.assertIn("Main Street", names)
        self.assertIn("Oak Avenue", names)
        self.assertEqual(len(streets), 2)
        