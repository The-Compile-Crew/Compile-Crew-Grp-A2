import unittest
from datetime import datetime
from App.models import Resident, Request, Drive
from App.controllers.resident_controller import *
from App.database import db

class ResidentControllerUnitTests(unittest.TestCase):

    def setUp(self):
        db.session.rollback()
        db.drop_all()
        db.create_all()

    def test_create_resident(self):
        resident = create_resident("aisha_user", "password123", "Aisha Resident", 1)
        self.assertIsNotNone(resident.residentId)
        self.assertEqual(resident.name, "Aisha Resident")
        self.assertEqual(resident.streetId, 1)

    def test_create_request_and_get_by_resident(self):
        resident = create_resident("dana_user", "password123", "Dana", 1)
        scheduled = datetime(2025, 10, 25, 9, 0)
        drive = Drive(driverId=1, streetId=1, scheduledTime=scheduled)
        db.session.add(drive)
        db.session.commit()

        request = create_request(resident.residentId, drive.driveId)
        self.assertIsNotNone(request.requestId)

        requests = view_my_requests(resident.residentId)
        self.assertEqual(len(requests), 1)
        self.assertEqual(requests[0].residentId, resident.residentId)