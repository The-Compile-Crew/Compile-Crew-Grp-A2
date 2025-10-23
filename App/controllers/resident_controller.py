from App.models import Resident, Driver, Request
from App.database import db

def create_resident(name, street_id):
  resident = Resident(name, street_id)
  db.session.add(resident)
  db.session.commit()
  return resident 

def get_all_residents():
  return Resident.query.all()

def get_resident(resident_id):
  return Resident.query.get(resident_id)

def get_drives_by_street(street.id):
  return Drive.query.filter_by(streetId = street_id).all()

def create_request(resident_id, drive_id):
  request = Request(resident_id, drive_id)
  db.session.add(resident)
  db.session.commit()
  return request

def get_request_by_resident(resident_id):
  return Request.query.filter_by(residentId = resident_id),all()
