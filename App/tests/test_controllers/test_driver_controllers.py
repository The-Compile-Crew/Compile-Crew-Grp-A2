import unittest
from datetime import datetime
from App.models import Driver, Drive, Request
from App.controllers.driver_controller import (
    create_driver,
    get_all_drivers,
    get_driver,
    update_driver_status,
    update_driver_location,
    schedule_drive,
    get_drives_by_driver,
    get_requests_by_driver
)
from App.database import db

class DriverControllerUnitTests(unittest.TestCase):

    def setUp(self):
        db.session.rollback()
        db.drop_all()
        db.create_all()

    def test_create_driver(self):
        driver = create_driver("Aisha Driver")
        self.assertIsNotNone(driver.driverId)
        self.assertEqual(driver.name, "Aisha Driver")
        self.assertEqual(driver.status, "available")

    def test_get_all_drivers(self):
        create_driver("John")
        create_driver("Sarah")
        drivers = get_all_drivers()
        self.assertEqual(len(drivers), 2)

    def test_get_driver(self):
        driver = create_driver("Charlie")
        fetched = get_driver(driver.driverId)
        self.assertEqual(fetched.name, "Charlie")

    def test_update_driver_status(self):
        driver = create_driver("Dana")
        updated = update_driver_status(driver.driverId, "busy")
        self.assertEqual(updated.status, "busy")

    def test_update_driver_location(self):
        driver = create_driver("Eli")
        updated = update_driver_location(driver.driverId, "Oak Avenue")
        self.assertEqual(updated.location, "Oak Avenue")

    def test_schedule_driver_and_get_drives(self):
        driver = create_driver("Frank")
        scheduled = datetime(2025, 10, 25, 9, 0)
        drive = schedule_drive(driver.driverId, street_id=1, scheduled_time=scheduled)
        self.assertIsNotNone(drive.driveId)

        drives = get_drives_by_driver(driver.driverId)
        self.assertEqual(len(drives), 1)
        self.assertEqual(drives[0].driverId, driver.driverId)

    def test_get_requests_by_driver(self):
        driver = create_driver("Grace")
        scheduled = datetime(2025, 10, 25, 10, 0)
        drive = Drive(driverId=driver.driverId, streetId=1, scheduledTime=scheduled)
        db.session.add(drive)
        db.session.commit()

        request = Request(residentId=1, driveId=drive.driveId)
        db.session.add(request)
        db.session.commit()

        requests = get_requests_by_driver(driver.driverId)
        self.assertEqual(len(requests), 1)
        self.assertEqual(requests[0].driveId, drive.driveId)