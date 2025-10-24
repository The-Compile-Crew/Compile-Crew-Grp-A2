import unittest
from datetime import datetime
from App.main import create_app
from App.database import db
from App.controllers import (
    create_user, login,
    create_driver, update_driver_status, update_driver_location, get_driver,
    create_street, create_resident, get_resident,
    schedule_drive, get_drives_by_street, get_driver_location,
    create_request, get_requests_by_driver, update_request_status
)

class IntegrationTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_schedule_and_notify(self):
        create_street("Main Street")
        create_resident("Alice", 1)
        create_driver("John")
        drive = schedule_drive(1, 1, datetime.now())
        inbox = get_drives_by_street(1)
        self.assertIn(drive, inbox)

    def test_request_flow(self):
        create_street("Oak Avenue")
        create_resident("Bob", 1)
        create_driver("Sarah")
        drive = schedule_drive(1, 1, datetime.now())
        request = create_request(1, drive.driveId)
        requests = get_requests_by_driver(1)
        self.assertIn(request, requests)

    def test_authentication(self):
        create_user("testuser", "testpass")
        token = login("testuser", "testpass")
        self.assertIsNotNone(token)

    def test_status_update(self):
        create_driver("Mike")
        schedule_drive(1, 1, datetime.now())
        update_driver_status(1, "active")
        driver = get_driver(1)
        self.assertEqual(driver.status, "active")

    def test_driver_location_flow(self):
        create_driver("Nina")
        schedule_drive(1, 1, datetime.now())
        update_driver_location(1, "Corner of Main")
        location = get_driver_location(1)
        self.assertEqual(location, "Corner of Main")

    def test_resident_inbox_flow(self):
        create_street("Elm Street")
        create_resident("Carol", 1)
        create_driver("Jake")
        drive = schedule_drive(1, 1, datetime.now())
        inbox = get_drives_by_street(1)
        self.assertTrue(any(d.driveId == drive.driveId for d in inbox))

    def test_signup_and_login(self):
        create_user("newuser", "newpass")
        token = login("newuser", "newpass")
        self.assertIsNotNone(token)

    def test_request_visibility(self):
        create_street("Birch Road")
        create_resident("Dana", 1)
        create_driver("Leo")
        drive = schedule_drive(1, 1, datetime.now())
        create_request(1, drive.driveId)
        inbox = get_drives_by_street(1)
        self.assertTrue(any(d.driveId == drive.driveId for d in inbox))