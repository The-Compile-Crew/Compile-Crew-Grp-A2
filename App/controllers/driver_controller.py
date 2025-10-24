from App.models import Driver, Drive, Request
from App.database import db

def create_driver(name):
    driver = Driver(name)
    db.session.add(driver)
    db.session.commit()
    return driver

def get_all_drivers():
    return Driver.query.all()

def get_driver(driver_id):
    return Driver.query.get(driver_id)

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

def get_driver_location(driver_id):
    driver = Driver.query.get(driver_id)
    if driver:
        return driver.location
    return None

def schedule_drive(driver_id, street_id, scheduled_time):
    drive = Drive(driver_id, street_id, scheduled_time)
    db.session.add(drive)
    db.session.commit()
    return drive

def get_drives_by_driver(driver_id):
    return Drive.query.filter_by(driverId=driver_id).all()

def get_requests_by_driver(driver_id):
    return Request.query.join(Drive).filter(Drive.driverId == driver_id).all()