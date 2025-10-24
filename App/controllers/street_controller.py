from App.models import Street, Drive
from App.database import db

def create_street(name):
    street = Street(name)
    db.session.add(street)
    db.session.commit()
    return street

def get_all_streets():
    return Street.query.all()

def get_drives_by_street(street_id):
    return Drive.query.filter_by(streetId=street_id).all()