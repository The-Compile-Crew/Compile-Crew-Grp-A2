from App.models import Street, Drive, Driver
from App.database import db

def create_street(name):
    street = Street(name)
    db.session.add(street)
    db.session.commit()
    return street

def get_all_streets():
    # Return all Street model instances
    streets = Street.query.all()
    return streets

def get_drives_by_street(street_id):
    street = Street.query.get(street_id)
    if street is None:
        return None
    return Drive.query.filter_by(streetId=street_id).all()