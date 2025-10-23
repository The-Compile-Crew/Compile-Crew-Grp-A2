import unittest
from App.models import Resident

class ResidentModelUnitTests(unittest.TestCase):

    def test_create_resident(self):
        resident = Resident("Aisha", 1)
        self.assertEqual(resident.name, "Aisha")
        self.assertEqual(resident.streetId, 1)

    def test_resident_json(self):
        resident = Resident("Aisha", 1)
        expected = {
            'residentId': None,
            'streetId': 1,
            'name': 'Aisha'
        }
        self.assertDictEqual(resident.toJSON(), expected)