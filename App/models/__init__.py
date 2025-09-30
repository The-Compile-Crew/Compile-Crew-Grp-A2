from .user import *
from .driver import *
from .street import *
from .resident import *
from .drive import *
from .request import *

from App.database import db

def initialize():
    db.drop_all()
    db.create_all()
    
    # Create sample data
    # Add streets
    main_st = Street("Main Street")
    oak_st = Street("Oak Avenue")
    db.session.add(main_st)
    db.session.add(oak_st)
    
    # Add drivers
    driver1 = Driver("John Driver")
    driver2 = Driver("Sarah Driver") 
    db.session.add(driver1)
    db.session.add(driver2)
    
    # Add residents
    resident1 = Resident("Alice Smith", 1)
    resident2 = Resident("Bob Johnson", 1)
    resident3 = Resident("Carol Williams", 2)
    db.session.add(resident1)
    db.session.add(resident2)
    db.session.add(resident3)
    
    db.session.commit()
    print("Database initialized with sample data!")

# Driver controllers
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

# Street controllers
def create_street(name):
    street = Street(name)
    db.session.add(street)
    db.session.commit()
    return street

def get_all_streets():
    return Street.query.all()

# Resident controllers  
def create_resident(name, street_id):
    resident = Resident(name, street_id)
    db.session.add(resident)
    db.session.commit()
    return resident

def get_all_residents():
    return Resident.query.all()

def get_resident(resident_id):
    return Resident.query.get(resident_id)

# Drive controllers
def schedule_drive(driver_id, street_id, scheduled_time):
    from datetime import datetime
    drive = Drive(driver_id, street_id, scheduled_time)
    db.session.add(drive)
    db.session.commit()
    return drive

def get_all_drives():
    return Drive.query.all()

def get_drives_by_street(street_id):
    return Drive.query.filter_by(streetId=street_id).all()

def get_drives_by_driver(driver_id):
    return Drive.query.filter_by(driverId=driver_id).all()

# Request controllers
def create_request(resident_id, drive_id):
    request = Request(resident_id, drive_id)
    db.session.add(request)
    db.session.commit()
    return request

def get_all_requests():
    return Request.query.all()

def get_requests_by_resident(resident_id):
    return Request.query.filter_by(residentId=resident_id).all()

def get_requests_by_drive(drive_id):
    return Request.query.filter_by(driveId=drive_id).all()

def update_request_status(request_id, status):
    request = Request.query.get(request_id)
    if request:
        request.status = status
        db.session.commit()
    return request