import unittest
from App.models import Resident, Street
from App.database import db

class ResidentModelUnitTests(unittest.TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()

    def test_create_resident(self):
        street = Street("Main Street")
        db.session.add(street)
        db.session.commit()

        resident = Resident("aisha_user", "password123", "Aisha", street.streetId)
        db.session.add(resident)
        db.session.commit()

        self.assertIsNotNone(resident.residentId)
        self.assertEqual(resident.name, "Aisha")
        self.assertEqual(resident.streetId, street.streetId)

    def test_resident_json(self):
        street = Street("Main Street")
        db.session.add(street)
        db.session.commit()

        resident = Resident("aisha_user", "password123", "Aisha", street.streetId)
        json_data = resident.get_json()

        self.assertEqual(json_data["name"], "Aisha")
        self.assertEqual(json_data["streetId"], street.streetId)