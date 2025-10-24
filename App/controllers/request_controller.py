from App.models import Request
from App.database import db

def create_request(resident_id, drive_id, description=None):
    request = Request(residentId=resident_id, driveId=drive_id, description=description)
    db.session.add(request)
    db.session.commit()
    return request

def get_all_requests():
    return Request.query.all()

def get_requests_by_drive(drive_id):
    return Request.query.filter_by(driveId=drive_id).all()

def update_request_status(request_id, status):
    request = Request.query.get(request_id)
    if request:
        request.status = status
        db.session.commit()
    return request