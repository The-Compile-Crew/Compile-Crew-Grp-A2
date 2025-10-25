import unittest
from App.models import Resident
from App.database import db
class ResidentModelUnitTests(unittest.TestCase):

    def test_create_resident(self):
        resident = Resident("aisha_user", "password123", "Aisha", 1)
        db.session.add(resident)
        db.session.commit()
        self.assertIsNotNone(resident.residentId)
        self.assertEqual(resident.name, "Aisha")
        self.assertEqual(resident.streetId, 1)

    def test_resident_json(self):
        resident = Resident("aisha_user", "password123", "Aisha", 1)
        json_data = resident.get_json()
        self.assertEqual(json_data["name"], "Aisha")
        self.assertEqual(json_data["streetId"], 1)