import unittest
from datetime import datetime
from App.models import Drive

class DriveModelUnitTests(unittest.TestCase):

    def test_create_drive(self):
        scheduled = datetime(2025, 10, 24, 8, 30)
        drive = Drive(driverId=1, streetId=2, scheduledTime=scheduled)
        self.assertEqual(drive.driverId, 1)
        self.assertEqual(drive.streetId, 2)
        self.assertEqual(drive.scheduledTime, scheduled)

    def test_drive_json(self):
        scheduled = datetime(2025, 10, 24, 8, 30)
        drive = Drive(driverId=1, streetId=2, scheduledTime=scheduled)
        expected = {
            'driveId': None,
            'driverId': 1,
            'streetId': 2,
            'scheduledTime': scheduled.isoformat()
        }
        self.assertDictEqual(drive.toJSON(), expected)