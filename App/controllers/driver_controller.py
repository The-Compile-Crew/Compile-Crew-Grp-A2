from App.models import Driver
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
  driver  = Driver.query.get(driver_id)
  if driver:
    driver.status = status
    db.session.commit()
  return driver

def update_driver_location(driver_id, location):
  driver  = Driver.query.get(driver_id)
  if driver:
    driver.location = location
    db.session.commit()
  return driver

def schedule_driver(Driver_id, street_id, scheduled_time):
  driver = Drive(driver_id, street_id, scheduled_time)
  db.session.add(driver)
  db.session.commit()
  return driver

def get_drives_by_driver(driver_id):
  return Drive.query.filter_by(driverId = driver_id).all()

def get_requests_by_driver(driver_id):
    return Request.query.join(Drive).filter(Drive.driverId == driver_id).all()
