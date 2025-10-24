import unittest
from datetime import datetime
from App.models import Request, Drive
from App.controllers.request_controller import (
    get_all_requests,
    get_requests_by_drive,
    update_request_status
)
from App.database import db

class RequestControllerUnitTests(unittest.TestCase):

    def setUp(self):
        db.session.rollback()
        db.drop_all()
        db.create_all()

    def test_get_all_requests(self):
        drive = Drive(driverId=1, streetId=1, scheduledTime=datetime(2025, 10, 25, 9, 0))
        db.session.add(drive)
        db.session.commit()

        request1 = Request(residentId=1, driveId=drive.driveId)
        request2 = Request(residentId=2, driveId=drive.driveId)
        db.session.add_all([request1, request2])
        db.session.commit()

        requests = get_all_requests()
        self.assertEqual(len(requests), 2)

    def test_get_requests_by_drive(self):
        drive = Drive(driverId=1, streetId=1, scheduledTime=datetime(2025, 10, 25, 9, 0))
        db.session.add(drive)
        db.session.commit()

        request = Request(residentId=1, driveId=drive.driveId)
        db.session.add(request)
        db.session.commit()

        results = get_requests_by_drive(drive.driveId)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].driveId, drive.driveId)

    def test_update_request_status(self):
        drive = Drive(driverId=1, streetId=1, scheduledTime=datetime(2025, 10, 25, 9, 0))
        db.session.add(drive)
        db.session.commit()

        request = Request(residentId=1, driveId=drive.driveId)
        db.session.add(request)
        db.session.commit()

        updated = update_request_status(request.requestId, "approved")
        self.assertEqual(updated.status, "approved")