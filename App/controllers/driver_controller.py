from App.models import Driver, Drive, Request
from App.database import db

def create_driver(username: str, driverName: str, password: str, location: str, status: str = "available"):
    driver = Driver(username, driverName, password, location, status)
    db.session.add(driver)
    db.session.commit()
    return driver


def update_driver_status(driver_id, status):
    driver = Driver.query.get(driver_id)
    if driver:
        driver.status = status
        db.session.commit()
    return driver

def update_driver_location(driver_id, location):
    driver = Driver.query.get(driver_id)
    if driver:
        driver.location = location
        db.session.commit()
    return driver


def schedule_drive(driver_id, street_id, scheduled_time):
    drive = Drive(driver_id, street_id, scheduled_time)
    db.session.add(drive)
    db.session.commit()
    return drive

def get_drives_by_driver(driver_id):
    drives = Drive.query.filter_by(driverId=driver_id).all()
    return drives

def get_requests_by_driver(driver_id):
    reqs = Request.query.join(Drive).filter(Drive.driverId == driver_id).all()
    return reqs