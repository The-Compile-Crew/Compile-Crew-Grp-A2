import unittest
from datetime import datetime
from App.models import Resident, Request, Drive
from App.controllers.resident_controller import (
    create_resident,
    get_all_residents,
    get_resident,
    get_drives_by_street,
    create_request,
    get_request_by_resident
)
from App.database import db

class ResidentControllerUnitTests(unittest.TestCase):

    def setUp(self):
        db.session.rollback()
        db.drop_all()
        db.create_all()

    def test_create_resident(self):
        resident = create_resident("Aisha Resident", street_id=1)
        self.assertIsNotNone(resident.residentId)
        self.assertEqual(resident.name, "Aisha Resident")
        self.assertEqual(resident.streetId, 1)

    def test_get_all_residents(self):
        create_resident("Alice", 1)
        create_resident("Bob", 2)
        residents = get_all_residents()
        self.assertEqual(len(residents), 2)

    def test_get_resident(self):
        resident = create_resident("Charlie", 1)
        fetched = get_resident(resident.residentId)
        self.assertEqual(fetched.name, "Charlie")

    def test_create_request_and_get_by_resident(self):
        resident = create_resident("Dana", 1)
        scheduled = datetime(2025, 10, 25, 9, 0)
        drive = Drive(driverId=1, streetId=1, scheduledTime=scheduled)
        db.session.add(drive)
        db.session.commit()

        request = create_request(resident.residentId, drive.driveId)
        self.assertIsNotNone(request.requestId)

        requests = get_request_by_resident(resident.residentId)
        self.assertEqual(len(requests), 1)
        self.assertEqual(requests[0].residentId, resident.residentId)