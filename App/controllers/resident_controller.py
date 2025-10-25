from App.models import Resident, Driver, Request, Drive
from App.database import db

def create_resident(username, password, name, street_id):
    resident = Resident(username, password, name, street_id)
    db.session.add(resident)
    db.session.commit()
    return resident

#view inbox
def get_drives_by_street(street_id):
    drives = Drive.query.filter_by(streetId=street_id).all()
    return drives

def create_request(resident_id, drive_id):
    resident = Resident.query.get(resident_id)
    if not resident:
        return None

    drive = Drive.query.get(drive_id)
    if not drive:
        return None

    request = Request(residentId=resident_id, driveId=drive_id)
    db.session.add(request)
    db.session.commit()
    return request

def view_my_requests(resident_id):
    resident = Resident.query.get(resident_id)
    if not resident:
        return None
    
    requests = Request.query.filter_by(residentId=resident_id).all()
    return requests