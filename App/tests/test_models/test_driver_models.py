import unittest
from App.models import Driver

class DriverModelUnitTests(unittest.TestCase):

    def test_create_driver(self):
        # Driver requires username, driverName, password, location in current model
        driver = Driver("aisha", "Aisha Driver", "pass", "Unknown")
        self.assertEqual(driver.driverName, "Aisha Driver")
        self.assertEqual(driver.status, "available")
        self.assertEqual(driver.location, "Unknown")

    def test_driver_json(self):
        driver = Driver("aisha", "Aisha Driver", "pass", "Unknown")
        expected = {
            'driverId': None,
            'driverName': 'Aisha Driver',
            'status': 'available',
            'location': 'Unknown'
        }
        self.assertDictEqual(driver.get_json(), expected)