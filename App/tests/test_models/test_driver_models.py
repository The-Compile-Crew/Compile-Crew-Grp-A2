import unittest
from App.models import Driver

class DriverModelUnitTests(unittest.TestCase):

    def test_create_driver(self):
        driver = Driver("Aisha Driver")
        self.assertEqual(driver.name, "Aisha Driver")
        self.assertEqual(driver.status, "available")
        self.assertIsNone(driver.location)

    def test_driver_json(self):
        driver = Driver("Aisha Driver")
        expected = {
            'driverId': None,
            'name': 'Aisha Driver',
            'status': 'available',
            'location': None
        }
        self.assertDictEqual(driver.toJSON(), expected)