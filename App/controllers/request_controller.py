from App.models import Request, Drive, Resident
from App.database import db

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

def get_all_requests():
    requests= Request.query.all()
    return requests

def get_requests_by_drive(drive_id):
    requests_by_drive = Request.query.filter_by(driveId=drive_id).all()
    return requests_by_drive

#accept or reject request
def update_request_status(request_id, status):
    request = Request.query.get(request_id)
    if request:
        request.status = status
        db.session.commit()
    return request